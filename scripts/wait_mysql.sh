#!/bin/bash

# Espera o MySQL ficar disponível
until nc -z -v -w30 mysql_service 3306
do
  echo "Aguardando MySQL iniciar..."
  sleep 60
done

echo "MySQL está disponível. Continuando com o processo."



