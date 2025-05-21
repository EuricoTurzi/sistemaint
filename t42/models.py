from django.db import models
from django.utils import timezone
from datetime import timedelta
from acompanhamento.models import Clientes

STATUS_CHOICES = [
    ("",""),
    ("Atualizado e Configurado", "Atualizado e Configurado"),
    
    ("Não Atualizado", "Não Atualizado"),
    ("Não Configurado", "Não Configurado"),
    ("Manutenção", "Manutenção"),
]
STATUS = [
    
    ("Estoque", "Estoque"),
    
    ("Retornando", "Retornando"),
    ("Enviado", "Enviado"),
    ("Estraviado", "Estraviado"),
    ("Manutenção", "Manutenção"),
]



EQUIPAMENTO_CHOICES = [
    ("TETS", "TETS"),
    ("TETS R", "TETS R"),
    ("LOKIES", "LOKIES"),
]
class T42Model(models.Model):
    nome = models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True, related_name='t42_nome')
    equipamento = models.CharField(choices=EQUIPAMENTO_CHOICES, max_length=100, null=True)
    id_equipamento = models.CharField(max_length=100)
    data = models.DateField(auto_now=True)
    fazenda = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, null=True)
    reversa = models.DateField(blank=True, null=True)
    estoque_status = models.CharField(max_length=50, choices=STATUS, blank=True, null=True, default='Estoque')
    quantidade = models.PositiveIntegerField(default=0)  # Novo campo para rastrear a quantidade

    def save(self, *args, **kwargs):
        if self.reversa is not None:
            self.reversa = self.reversa + timedelta(days=90)
        else:
            self.reversa = timezone.now().date() + timedelta(days=90)
        super().save(*args, **kwargs)