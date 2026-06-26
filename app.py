from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()
app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']=(
    f"mysql+pymysql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}/"
    f"{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False
db=SQLAlchemy(app)











