# Usa a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da aplicação para dentro do container
COPY . .

# Instala as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Define o comando para iniciar a aplicação
CMD ["python", "run.py"]
