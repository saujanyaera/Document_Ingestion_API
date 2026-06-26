from rag.document_ingestion import docs_loader
from rag.document_splitting import docs_splitter_recursive 
from rag.document_store import get_vectorstore

def ingest_document(filename, index_name='rag-index', strategy='recursive'):
    documents=docs_loader(filename)
    chunks=docs_splitter_recursive(documents, strategy=strategy)
    vectorstore=get_vectorstore(index_name)
    vectorstore.add_documents(chunks)
    return{
        'status':'success',
        'file':filename,
        'strategy': strategy,
        'chunks':len(chunks)
        
    }
    
# result=ingest_document('saujanyacv2026.pdf')
# print(result)