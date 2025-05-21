from django.db import models

class regcliente(models.Model):
    nome = models.CharField(max_length=100, null=True)
    franquia_km = models.TextField(max_length=50, null=True, blank=True)
    franquiah = models.TimeField()
    valor_acionamento = models.DecimalField(max_digits=10, decimal_places=5, default=0.00, null=True, blank=True)
    valorkm = models.DecimalField(max_digits=10, decimal_places=3, default=0.00, null=True, blank=True)
    valor_exedente = models.DecimalField(max_digits=10, decimal_places=3, default=0.00, null=True, blank=True)
    
    def __str__(self):
        return self.nome