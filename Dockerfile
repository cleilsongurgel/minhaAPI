# Usar imagem do Python como base
FROM python:3.9

# Definir diretório de trabalho no container
WORKDIR /app

# Copiar arquivos para dentro do container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta 8000 usada pelo Uvicorn
EXPOSE 8000

# Comando para iniciar o servidor com Uvicorn e Gunicorn
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "app:app"]
