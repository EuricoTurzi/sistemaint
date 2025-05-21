from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.nome