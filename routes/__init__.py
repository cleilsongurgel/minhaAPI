from flask import Blueprint

# Criamos um Blueprint de nome 'contas_bp'
contas_bp = Blueprint('contas', __name__)

from .contas import *  # Importa as rotas do arquivo contas.py
