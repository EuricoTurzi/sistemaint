import os
import sys
import django
from django.db import connection

# Adicione o diretório do projeto ao sys.path
sys.path.append('C:/Sistema Inteligencia/Projeto Djangomaster')

# Defina a variável de ambiente DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')  # Substitua 'ProjetoDjangomaster' pelo nome do seu projeto

django.setup()

from requisicao.models import Requisicoes  # Substitua 'requisicao' pelo nome do seu aplicativo

def reset_sequence(model_class):
    with connection.cursor() as cursor:
        table_name = model_class._meta.db_table
        cursor.execute(f"UPDATE sqlite_sequence SET seq = (SELECT MAX(id) FROM {table_name}) WHERE name = '{table_name}'")

# Chame a função para o modelo Requisicoes
reset_sequence(Requisicoes)
print("Sequência de IDs redefinida com sucesso!")
