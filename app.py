from flask import Flask
from models import db
from routes import contas_bp  # Importamos o Blueprint de rotas

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Inicializa o banco de dados

# Criar as tabelas antes de iniciar a aplicação
with app.app_context():
    db.create_all()

# Registramos o Blueprint de rotas
app.register_blueprint(contas_bp)

@app.route('/')
def home():
    return "API está rodando!"

if __name__ == '__main__':
    app.run(debug=True)
