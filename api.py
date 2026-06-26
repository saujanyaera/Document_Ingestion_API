from fastapi import FastAPI, UploadFile, File
from pydantic import Field
import shutil
from pydantic import BaseModel
from pipeline import ingest_document
from rag.document_store import get_vectorstore
from metadata_db import db, Metadata, app_flask
import os

app=FastAPI()



class Ingest(BaseModel):
    index_name:str='rag-index'
    query: str = Field(default='', description="User query for similarity search")

@app.post('/uploads')
def ingestion(file:UploadFile=File(...), query:str=''):

    index_name:str='rag-index'
    vectorstore=get_vectorstore(index_name)
    


    file_path=f"temp/{file.filename}"
    os.makedirs("temp", exist_ok=True)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    result=ingest_document(file_path, index_name)
    
    datas=vectorstore.similarity_search(
        query,
        k=1
    )

    with app_flask.app_context():
     for doc in datas:
        meta = doc.metadata
        # meta =  (doc.author, doc.creator, doc.page)
        
        db.session.add(
            Metadata(
                author=meta.get("author", "unknown"),
                creator=meta.get("creator", "unknown"),
                page=meta.get("page", 0)
            )
        )

        db.session.commit()
    
    return {
        'status': 'success',
        'result': result,
        'metadata': [
            {
                "author": doc.metadata.get("author"),
                "creator": doc.metadata.get("creator"),
                "page": doc.metadata.get("page")
            }
            for doc in datas
        ]
    }






 

