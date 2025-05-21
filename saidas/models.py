from django.db import models
from produto.models import Produto
from django.utils import timezone

class Saidas(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='saida_produto')
    marca = models.TextField(max_length=50, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    descricao = models.TextField(max_length=150, null=True, blank=True)
    preco = models.IntegerField(null=True, blank=True)
    data_criacao = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.data_criacao = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.produto)