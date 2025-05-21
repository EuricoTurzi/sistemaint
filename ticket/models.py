from django.contrib.auth.models import User
from django.db import models

class ticketmodel(models.Model):
    setores = [
        ('Diretoria', 'Diretoria'),
        ('Inteligência', 'Inteligência'),
        ('Faturamento', 'Faturamento'),
        ('Expedição', 'Expedição'),
        ('Configuração', 'Configuração'),
        ('Quality', 'Quality'),
        ('Área Técnica', 'Área Técnica'),
        ('Comercial', 'Comercial'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='tickets')
    setor = models.CharField(choices=setores, max_length=255, blank=True, null=True)
    erro = models.CharField(max_length=255, blank=True, null=True)
    correcao = models.CharField(max_length=255, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True, default='Pendente')
    devolutiva = models.TextField(blank=True, null=True)  # Campo de texto para devolutiva

    def __str__(self):
        return f"Ticket {self.id} - {self.usuario.username}"