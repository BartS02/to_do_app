from . import db
from datetime import datetime
#!This class is used to inherit from our db and allows us to map out properties to db columns

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(300), unique = True)
    complete = db.Column(db.Boolean, default= False)
    date = db.Column(db.DateTime, default=datetime.now)
    categories = db.Column(db.String(50))