from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Registro(models.Model):
    id_equipamento = models.CharField(max_length=50)
    local = models.CharField(max_length=100)
    data_insercao = models.DateTimeField(default=now)
    operacao = models.CharField(
        max_length=50,
        choices=[
            ('Santa Cruz', 'Santa Cruz'),
            ('Prysmian', 'Prysmian'),
            ('Lauto', 'Lauto'),
            ('Fast Shop', 'Fast Shop'),
        ],
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_equipamento} - {self.operacao}"


