#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.db import connection

def debug_emails_detailed():
    print("=== DEBUG EMAILS DETALHADO ===")
    
    with connection.cursor() as cursor:
        # Verificar todos os valores únicos de email
        cursor.execute("""
            SELECT DISTINCT email, COUNT(*) as count
            FROM faturamento_faturamento 
            GROUP BY email
            ORDER BY count DESC
        """)
        
        print("=== TODOS OS VALORES ÚNICOS DE EMAIL ===")
        for email, count in cursor.fetchall():
            if email is None:
                print(f"NULL: {count} registros")
            else:
                print(f"'{email}': {count} registros")
        
        # Verificar se há emails válidos que não estão sendo capturados
        cursor.execute("""
            SELECT DISTINCT email 
            FROM faturamento_faturamento 
            WHERE email IS NOT NULL 
            AND email != '' 
            AND email != 'email'
            AND email LIKE '%@%'
            ORDER BY email
        """)
        
        print(f"\n=== EMAILS VÁLIDOS (com @) ===")
        emails_validos = cursor.fetchall()
        print(f"Total de emails válidos: {len(emails_validos)}")
        
        for i, (email,) in enumerate(emails_validos):
            print(f"{i+1}. {email}")

if __name__ == "__main__":
    debug_emails_detailed()

