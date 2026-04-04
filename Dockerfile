# 1. Baixa um Linux Ubuntu minúsculo que já vem com o Python 3.12.5 instalado
FROM python:3.12.5-slim

# 2. Cria uma pasta chamada /app dentro do contêiner e entra nela
WORKDIR /app

# 3. Copia o seu arquivo de bibliotecas e manda o pip instalar
COPY python/requirements.txt .
# Vamos adicionar o fastapi e o uvicorn no momento da instalação
RUN pip install --no-cache-dir -r requirements.txt fastapi uvicorn pydantic

# 4. Copia toda a pasta api (onde estão main.py, schemas.py e o modelo.pkl) para dentro do contêiner
COPY python/api/ /app/api/

# 5. Define em qual pasta o comando de ligar o servidor será executado
WORKDIR /app/api

# 6. Libera a porta 8000 para podermos acessar do nosso navegador
EXPOSE 8000

# 7. O comando final que liga a API quando o contêiner inicia
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]