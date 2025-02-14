# Flask API de Usuários

Esta é uma API simples criada com Flask para fornecer informações sobre usuários armazenados em um banco de dados SQLite. Os dados são gerados aleatoriamente utilizando a biblioteca Faker.

## Criação do Projeto

1. Crie um diretório para o projeto e acesse-o:
   ```sh
   mkdir flask_api_users
   cd flask_api_users
   ```

2. Inicialize um repositório Git (opcional):
   ```sh
   git init
   ```

3. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

4. Instale as dependências necessárias:
   ```sh
   pip install flask flask-sqlalchemy faker
   ```

5. Crie um arquivo `requirements.txt` para facilitar futuras instalações:
   ```sh
   pip freeze > requirements.txt
   ```

## Instalação e Configuração

1. Clone o repositório:
   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. Ative o ambiente virtual:
   ```sh
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Execute a API:
   ```sh
   python app.py
   ```

## Uso

A API disponibiliza o seguinte endpoint:

### Obter todos os usuários
```
GET /users
```
- Retorna uma lista de usuários cadastrados no banco de dados.

Exemplo de resposta:
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "age": 30
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "age": 25
    }
]
```

## Autor
Criado por [Cleilson Brito]

