# Usar imagem oficial do Python
FROM python:3.9

# Definir diretório de trabalho
WORKDIR /app

# Copiar os arquivos para dentro do container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta 8000
EXPOSE 8000

# Comando para iniciar o servidor com Uvicorn
CMD ["hypercorn", "app:app", "--bind", "0.0.0.0:8000"]
