from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()



app_flask=Flask(__name__)






app_flask.config['SQLALCHEMY_DATABASE_URI']=(
    f"mysql+pymysql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}/"
    f"{os.getenv('DB_NAME')}"
)
app_flask.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False
db=SQLAlchemy(app_flask)

class Metadata(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    author=db.Column(db.String(180), nullable=False)
    creator=db.Column(db.String(180), nullable=False)
    page=db.Column(db.Integer, nullable=False)
 
with app_flask.app_context():
    db.create_all()