from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Conta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    conta_corrente = db.Column(db.String(20), unique=True, nullable=False)
    saldo = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

# Criar as tabelas antes de iniciar a aplicação
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "API está rodando!"

if __name__ == '__main__':
    app.run(debug=True)
