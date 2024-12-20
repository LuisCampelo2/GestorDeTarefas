#!/bin/sh

# Ativar o ambiente virtual
source /venv/bin/activate

# Rodar o Gunicorn
echo "Rodando o Gunicorn..."
gunicorn project.wsgi:application --bind 0.0.0.0:8000


