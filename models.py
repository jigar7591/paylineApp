from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    card_number = db.Column(db.String(150), unique=True, nullable=False)
    membership_number = db.Column(db.String(150), unique=True, nullable=False)
    date_of_birth = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150), nullable=False)
