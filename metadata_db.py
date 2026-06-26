from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app_flask=Flask(__name__)



app_flask.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:saujanya@localhost/metadata'
app_flask.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False
db=SQLAlchemy(app_flask)

class Metadata(db.Model):
    author=db.Column(db.String(180), nullable=False, primary_key=True)
    creator=db.Column(db.String(180), nullable=False)
    page=db.Column(db.Integer, nullable=False)
 
with app_flask.app_context():
    db.create_all()