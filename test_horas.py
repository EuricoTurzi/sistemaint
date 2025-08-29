#!/usr/bin/env python
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from horas.models import horas
from horas.views import parse_datetime_flexible

print("=== TESTE DE DADOS DE HORAS ===")
print(f"Total de registros: {horas.objects.count()}")
print(f"Registros não aprovados: {horas.objects.exclude(status_choice='Aprovado').count()}")

qs = horas.objects.exclude(status_choice='Aprovado')
print(f"\nFuncionários distintos: {list(qs.values_list('funcionario', flat=True).distinct())}")

print("\nRegistros não aprovados:")
for h in qs:
    hi = parse_datetime_flexible(h.hora_inicial)
    hf = parse_datetime_flexible(h.hora_final)
    valido = hi and hf and hf > hi
    print(f"ID: {h.id}, Funcionário: {h.funcionario}, HI: {h.hora_inicial} -> {hi}, HF: {h.hora_final} -> {hf}, Válido: {valido}")

print("\n=== TESTE DA FUNÇÃO DE CONSULTA ===")
employee_data = []
grand_seconds = 0

for func_id in qs.values_list('funcionario', flat=True).distinct():
    records = qs.filter(funcionario=func_id)
    total_seconds = 0
    
    for item in records:
        hi = parse_datetime_flexible(item.hora_inicial)
        hf = parse_datetime_flexible(item.hora_final)
        if hi and hf and hf > hi:
            total_seconds += int((hf - hi).total_seconds())
    
    grand_seconds += total_seconds
    
    h, resto = divmod(total_seconds, 3600)
    m, s = divmod(resto, 60)
    formatted = f"{h:02d}:{m:02d}:{s:02d}"
    
    employee_data.append({
        'funcionario': records.first().funcionario if records.exists() else '',
        'records': records,
        'total': formatted,
    })

print(f"Employee data length: {len(employee_data)}")
for emp in employee_data:
    print(f"Funcionário: {emp['funcionario']}, Total: {emp['total']}, Records: {emp['records'].count()}")
