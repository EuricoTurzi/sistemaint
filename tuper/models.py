from django.db import models
from produto.models import Produto

class Transportadora(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)

    def __str__(self):
        return self.nome

class formulario_divisao(models.Model):
    transport = [
        ('Transportadora Peregrina', 'Transportadora Peregrina'),
        ('Valor Transportes', 'Valor Transportes'),
        ('transjk Transportes Rodoviarios', 'transjk Transportes Rodoviarios'),
        ('JVG Transportes', 'JVG Transportes'),
        ('JP Transportes', 'JP Transportes'),
        ('Cooperleste Cooperativa dos Transportes', 'Cooperleste Cooperativa dos Transportes'),
        ('Astran Transportes', 'Astran Transportes'),
        ('Asavel Transportes', 'Asavel Transportes'),
        ('AGR Transportes', 'AGR Transportes'),
        ('A.Alves Correa Ligeirinho Transportes', 'A.Alves Correa Ligeirinho Transportes'),
        ('Dolci & Dolci Transporte', 'Dolci & Dolci Transporte'),
    ]

    transportadora = models.CharField(choices=transport, null=True, blank=True, max_length=50)
    destino = models.CharField(max_length=255, blank=True, null=True)
    quantidade = models.IntegerField(null=True, blank=True)
    tipo_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='produtotuper')
    Id_equipamentos = models.TextField(max_length=250, blank=True, default='')

    def __str__(self):
        return f"Requisição {self.id} - {self.transportadora}"

class estoque_tuper(models.Model):
    tipo_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='modelo')
    quantidade = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f"Requisição {self.id} - {self.quantidade}"