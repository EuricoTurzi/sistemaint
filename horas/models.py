from django.db import models
from django.conf import settings  # Importa as configurações, inclusive o AUTH_USER_MODEL
from decimal import Decimal
# models.py
import datetime
from django.db import models
from django.conf import settings
class horas(models.Model):
    choices = [
        ('Pendente','Pendente'),
        ('Aprovado','Aprovado')
    ]
    status_choice = models.CharField(choices=choices, max_length=50, null=True, blank=True)
    funcionario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    comprovante1 = models.ImageField(upload_to='imagens/', null=True, blank=True)
    hora_inicial = models.CharField(max_length=50, null=True, blank=True)
    hora_final = models.CharField(max_length=50, null=True, blank=True, default=0)
    comprovante2 = models.ImageField(upload_to='imagens/', null=True, blank=True)
    motivo = models.CharField(max_length=50, null=True, blank=True)
    total = models.CharField(max_length=50, null=True, blank=True)
    total_de_horas = models.CharField(max_length=50,null=True,blank=True)
    
    def save(self, *args, **kwargs):
        if self.hora_inicial and self.hora_final:
            try:
                hi = datetime.datetime.strptime(self.hora_inicial, "%Y-%m-%d %H:%M:%S")
                hf = datetime.datetime.strptime(self.hora_final,  "%Y-%m-%d %H:%M:%S")
                if hf > hi:
                    diff = hf - hi
                    h, rem = divmod(diff.seconds, 3600)
                    m, s   = divmod(rem, 60)
                    self.total_de_horas = f"{h:02d}:{m:02d}:{s:02d}"
            except ValueError:
                # Formato inválido: mantém o valor antigo ou em branco
                pass
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'Horas de {self.funcionario}'
