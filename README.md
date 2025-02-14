# API de Contas Bancárias

Esta é uma API RESTful desenvolvida em Flask para gerenciar contas bancárias. Agora, a aplicação utiliza **Uvicorn** para rodar de forma assíncrona e um **proxy reverso Nginx** para melhor desempenho e escalabilidade.

## 🚀 Tecnologias Utilizadas
- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite (banco de dados leve para testes)
- Uvicorn (ASGI Server)
- Nginx (Proxy reverso)
- Docker & Docker Compose

---

## 📁 Estrutura do Projeto
```
MinhaApi/
│── app.py               # Arquivo principal da API
│── models.py            # Modelo do banco de dados
│── routes/
│   ├── __init__.py      # Inicialização do Blueprint
│   ├── contas.py        # Rotas para CRUD de contas
│── venv/                # Ambiente virtual (ignorar no Git)
│── contas.db            # Banco de dados SQLite
│── requirements.txt     # Dependências do projeto
│── Dockerfile           # Configuração do container Flask/Uvicorn
│── nginx.conf           # Configuração do Nginx
│── docker-compose.yml   # Arquivo para subir os containers
│── README.md            # Documentação da API
```

---

## ⚙️ Configuração e Execução com Docker

### 1️⃣ Construir e subir os containers
```bash
docker-compose up --build -d
```

### 2️⃣ Parar os containers
```bash
docker-compose down
```

A API estará disponível em:
```
http://localhost/
```

---

## 🛠 Endpoints da API

### 1️⃣ Criar uma Conta
**POST /contas**
```json
{
    "nome": "João Silva",
    "conta_corrente": "123456",
    "saldo": 1500.75,
    "email": "joao@email.com",
    "telefone": "11987654321"
}
```
**Resposta (201 Created):**
```json
{
    "message": "Conta criada com sucesso!",
    "id": 1
}
```

---

### 2️⃣ Listar Todas as Contas
**GET /contas**

**Resposta:**
```json
[
    {
        "id": 1,
        "nome": "João Silva",
        "conta_corrente": "123456",
        "saldo": 1500.75,
        "email": "joao@email.com",
        "telefone": "11987654321"
    }
]
```

---

### 3️⃣ Buscar Conta por ID
**GET /contas/{id}**

**Exemplo:**
`GET /contas/1`

**Resposta:**
```json
{
    "id": 1,
    "nome": "João Silva",
    "conta_corrente": "123456",
    "saldo": 1500.75,
    "email": "joao@email.com",
    "telefone": "11987654321"
}
```

---

### 4️⃣ Atualizar Conta
**PUT /contas/{id}**

**Exemplo:**
`PUT /contas/1`
```json
{
    "saldo": 2000.00
}
```
**Resposta:**
```json
{
    "message": "Conta atualizada com sucesso!"
}
```

---

### 5️⃣ Excluir Conta
**DELETE /contas/{id}**

**Exemplo:**
`DELETE /contas/1`

**Resposta:**
```json
{
    "message": "Conta excluída com sucesso!"
}
```

---

## 🛠 Banco de Dados
A API usa **SQLite** para armazenar os dados. Caso precise recriar o banco de dados:
```bash
rm contas.db  # No Linux/macOS
DEL contas.db  # No Windows
python app.py  # Para recriar as tabelas automaticamente
```

---

## 📌 Observações
✅ Código modularizado com **Blueprints** para melhor organização.  
✅ Utiliza **Flask-SQLAlchemy** para gerenciar o banco de dados.  
✅ Agora roda com **Uvicorn** para melhor desempenho.  
✅ Proxy reverso configurado com **Nginx**.  
✅ Dockerizado para facilitar a implantação.  

Se tiver alguma dúvida, entre em contato! 🚀

