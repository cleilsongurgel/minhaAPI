# Usar uma imagem oficial do Python como base
FROM python:3.9

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta usada pelo Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
