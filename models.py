from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Conta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    conta_corrente = db.Column(db.String(20), unique=True, nullable=False)
    saldo = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
