from . import db
from flask_login import UserMixin
class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(10000))
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"))
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    fName=db.Column(db.String(10))
    lName=db.Column(db.String(10))
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    note=db.relationship('Note')
    