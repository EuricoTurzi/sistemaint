from django.db import models
from django.contrib.auth.models import User
from acompanhamento.models import Clientes   
from produto.models import Produto 

class Qualit(models.Model):
    TIPO_PEDIDO_CHOICES = [
        ('Tipo de Faturamento', 'Tipo de Faturamento'),
        ('Aquisicão Nova', 'Aquisicão Nova'),
        ('Manutenção', 'Manutenção'),
        ('Aditivo', 'Aditivo'),
        ('Acessorios', 'Acessorios'),
        ('Extravio', 'Extravio'),
        ('Texte', 'Texte'),
        ('Isca Fast', 'Isca Fast'),
        ('Isca Fast Agente', 'Isca Fast Agente'),
        ('Antenista', 'Antenista'),
        ('Reversa', 'Reversa'),
    ]
    CONTRATO_TIPO_CHOICES = [
        ('', ''),
        ('Descartavel', 'Descartavel'),
        ('Retornavel', 'Retornavel'),
    ]
    TP_CHOICES = [
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('30', '30'),
        ('60', '60'),
        ('360', '360'),
        ('720', '720'),
    ]
    OPERADORA_CHOICES = [
        ('ESEYE', 'ESEYE'),
        ('1NCE', '1NCE'),
    ]

    Data = models.CharField(max_length=50, null=True)
    ID = models.CharField(max_length=50,null=True)
    ID2 = models.CharField(max_length=50,null=True)
    ICCID_NOVO = models.CharField(max_length=50)
    CONTRATO = models.CharField(choices=CONTRATO_TIPO_CHOICES, null=True, blank=True, max_length=50)
   
    OPERADORA = models.CharField(choices=OPERADORA_CHOICES, max_length=100)
    CLIENTE = models.CharField(max_length=50 ,null=True) # Atualize para um usuário válido
   


    def __str__(self):
        return self.ICCID_NOVO
