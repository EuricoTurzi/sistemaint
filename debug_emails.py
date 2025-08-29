#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.db import connection

def debug_emails():
    print("=== DEBUG EMAILS ===")
    
    with connection.cursor() as cursor:
        # Verificar total de registros
        cursor.execute("SELECT COUNT(*) FROM faturamento_faturamento")
        total = cursor.fetchone()[0]
        print(f"Total de registros: {total}")
        
        # Verificar emails únicos
        cursor.execute("""
            SELECT DISTINCT email 
            FROM faturamento_faturamento 
            WHERE email IS NOT NULL 
            AND email != '' 
            AND email != 'email'
            ORDER BY email
        """)
        
        emails = cursor.fetchall()
        print(f"Emails únicos encontrados: {len(emails)}")
        
        for i, (email,) in enumerate(emails[:20]):  # Mostrar apenas os primeiros 20
            print(f"{i+1}. {email}")
        
        if len(emails) > 20:
            print(f"... e mais {len(emails) - 20} emails")
        
        # Verificar valores NULL ou vazios
        cursor.execute("""
            SELECT COUNT(*) 
            FROM faturamento_faturamento 
            WHERE email IS NULL OR email = '' OR email = 'email'
        """)
        null_count = cursor.fetchone()[0]
        print(f"Registros com email NULL/vazio/email: {null_count}")
        
        # Verificar alguns exemplos de emails
        cursor.execute("""
            SELECT email, COUNT(*) as count
            FROM faturamento_faturamento 
            WHERE email IS NOT NULL AND email != '' AND email != 'email'
            GROUP BY email
            ORDER BY count DESC
            LIMIT 10
        """)
        
        print("\n=== TOP 10 EMAILS MAIS FREQUENTES ===")
        for email, count in cursor.fetchall():
            print(f"{email}: {count} registros")

if __name__ == "__main__":
    debug_emails()
