from django.db import models

class Formulario(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    inicio_de_contrato = models.DateField()
    vigencia = models.CharField(max_length=14)
    
    def __str__(self):
        return self.razao_social