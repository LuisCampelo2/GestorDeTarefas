# Usa a imagem oficial do Python
FROM python:3.11.3-alpine3.18

# Atualiza o sistema e instala dependências para o MySQL e pacotes de construção
RUN apk update && apk add --no-cache mysql-client gcc musl-dev mariadb-dev build-base

# Define o diretório de trabalho
WORKDIR /djangoApps

# Copia a pasta "djangoApps" e "scripts" para dentro do container.
COPY djangoApps /djangoApps
COPY scripts /scripts/
RUN chmod +x /scripts/wait_mysql.sh /scripts/commands.sh


# Cria um ambiente virtual e instala as dependências
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /djangoApps/requirements.txt

# Adiciona a pasta scripts e venv/bin 
# no $PATH do container.
ENV PATH="/scripts:/venv/bin:$PATH"

# Expõe a porta 8000, que é a porta padrão do Django
EXPOSE 8000

# Definindo variável para o WSGI (garante que o Gunicorn seja executado com o WSGI do Django)
ENV DJANGO_SETTINGS_MODULE=project.settings

# Executa a pasta script
CMD ["/bin/sh", "/scripts/commands.sh"]