FROM python:3.11.3-alpine3.18
LABEL mantainer="luisfilipecab@gmail.com"

# Instalar o cliente MySQL
RUN apk update && apk add mysql-client


# Continuar com as demais configurações do Dockerfile...

# Essa variável de ambiente é usada para controlar se o Python deve 
# gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE=1

# Define que a saída do Python será exibida imediatamente no console ou em 
# outros dispositivos de saída, sem ser armazenada em buffer.
# Em resumo, você verá os outputs do Python em tempo real.
ENV PYTHONUNBUFFERED=1

# Entra na pasta djangoapp no container
WORKDIR /djangoApps

# Copia a pasta "djangoapp" e "scripts" para dentro do container.
COPY djangoApps /djangoApps
COPY scripts /scripts



# A porta 8000 estará disponível para conexões externas ao container
# É a porta que vamos usar para o Django.
EXPOSE 8000

# RUN executa comandos em um shell dentro do container para construir a imagem. 
# O resultado da execução do comando é armazenado no sistema de arquivos da 
# imagem como uma nova camada.
# Agrupar os comandos em um único RUN pode reduzir a quantidade de camadas da 
# imagem e torná-la mais eficiente.
RUN chmod -R +x /scripts && \
    python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /djangoApps/requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    mkdir -p /data/web/static /data/web/media && \
    chown -R duser:duser /venv /data/web/static /data/web/media /scripts && \
    chmod -R 755 /data/web/static /data/web/media

# Adiciona a pasta scripts e venv/bin 
# no $PATH do container.
ENV PATH="/scripts:/venv/bin:$PATH"

# Muda o usuário para duser
USER duser

# Executa o arquivo scripts/commands.sh
CMD ["/bin/sh", "/scripts/commands.sh"]



