from flask import Blueprint, request, jsonify
from models import db, Conta

contas_bp = Blueprint('contas', __name__)  # Criamos um Blueprint para as rotas

# Rota para criar uma nova conta
@contas_bp.route('/contas', methods=['POST'])
def create_conta():
    data = request.get_json()
    if not all(key in data for key in ['nome', 'conta_corrente', 'saldo', 'email', 'telefone']):
        return jsonify({'error': 'Todos os campos são obrigatórios!'}), 400

    nova_conta = Conta(
        nome=data['nome'],
        conta_corrente=data['conta_corrente'],
        saldo=data['saldo'],
        email=data['email'],
        telefone=data['telefone']
    )

    db.session.add(nova_conta)
    db.session.commit()

    return jsonify({'message': 'Conta criada com sucesso!', 'id': nova_conta.id}), 201

# Rota para listar todas as contas
@contas_bp.route('/contas', methods=['GET'])
def get_contas():
    contas = Conta.query.all()
    return jsonify([{
        'id': c.id,
        'nome': c.nome,
        'conta_corrente': c.conta_corrente,
        'saldo': c.saldo,
        'email': c.email,
        'telefone': c.telefone
    } for c in contas])

# Rota para obter uma conta específica
@contas_bp.route('/contas/<int:id>', methods=['GET'])
def get_conta(id):
    conta = Conta.query.get_or_404(id)
    return jsonify({
        'id': conta.id,
        'nome': conta.nome,
        'conta_corrente': conta.conta_corrente,
        'saldo': conta.saldo,
        'email': conta.email,
        'telefone': conta.telefone
    })

# Rota para atualizar uma conta
@contas_bp.route('/contas/<int:id>', methods=['PUT'])
def update_conta(id):
    conta = Conta.query.get_or_404(id)
    data = request.get_json()
    
    conta.nome = data.get('nome', conta.nome)
    conta.conta_corrente = data.get('conta_corrente', conta.conta_corrente)
    conta.saldo = data.get('saldo', conta.saldo)
    conta.email = data.get('email', conta.email)
    conta.telefone = data.get('telefone', conta.telefone)

    db.session.commit()
    return jsonify({'message': 'Conta atualizada com sucesso!'})

# Rota para excluir uma conta
@contas_bp.route('/contas/<int:id>', methods=['DELETE'])
def delete_conta(id):
    conta = Conta.query.get_or_404(id)
    db.session.delete(conta)
    db.session.commit()
    return jsonify({'message': 'Conta excluída com sucesso!'})
