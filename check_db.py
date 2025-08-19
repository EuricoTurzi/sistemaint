import sqlite3
import os

# Conectar ao banco de dados
db_path = 'db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Verificar se a tabela existe
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Nestle_gridinternacional';")
table_exists = cursor.fetchone()

if table_exists:
    print("Tabela Nestle_gridinternacional existe!")
    
    # Verificar a estrutura da tabela
    cursor.execute("PRAGMA table_info(Nestle_gridinternacional);")
    columns = cursor.fetchall()
    
    print("\nColunas na tabela:")
    for col in columns:
        print(f"  {col[1]} ({col[2]})")
        
    # Verificar se a coluna data_envio já existe
    data_envio_exists = any(col[1] == 'data_envio' for col in columns)
    print(f"\nColuna 'data_envio' existe: {data_envio_exists}")
    
else:
    print("Tabela Nestle_gridinternacional não existe!")

conn.close()
