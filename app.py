from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from pipeline import ingest_document
from rag.document_store import get_vectorstore
app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:saujanya@localhost/metadata'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False
db=SQLAlchemy(app)




vectorstore=get_vectorstore(index_name)






