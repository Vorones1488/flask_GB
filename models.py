
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    invisible = db.Column(db.Boolean, default=True)

    
    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.password})'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.String(80), db.ForeignKey('register.id'), nullable=False)
    name = db.Column(db.String(50))
    firstname = db.Column(db.String(50) )
    group = db.Column(db.String(8))
    shool_asses = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    invisible = db.Column(db.Boolean, default=True)
    

