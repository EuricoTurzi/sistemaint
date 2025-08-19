from django.db import models
from django.contrib.auth.models import User
from acompanhamento.models import Clientes  # Verifique se o caminho está correto

class Reativacao(models.Model):
    STATUS_CHOICES = [
        ('Faturado', 'Faturado'),
        ('Não Faturado', 'Não Faturado'),
	('Sem Custo','Sem Custo'),
    ]
    MOTIVO_CHOICES = [
        ('Retornavel', 'Retornavel'),
        ('Descartavel', 'Descartavel'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)  # Usuário responsável pela reativação
    nome = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='reativacao_nome')
    motivo_reativacao = models.CharField(choices=MOTIVO_CHOICES, max_length=50, null=True, blank=True)
    canal_solicitacao = models.CharField(max_length=100, null=True, blank=True)
    cnpj = models.CharField(max_length=100, null=True, blank=True)
    observacoes = models.CharField(max_length=100)
    data_hora_criacao = models.DateTimeField(auto_now_add=True,null=True,blank=True)  # Data e hora de criação (preenchido automaticamente)
    status_reativacao = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Não Faturado', null=True, blank=True)
    
    def __str__(self):
        return f"Reativacao {self.id} - {self.nome}"

class IdIccid(models.Model):
    reativacao = models.ForeignKey(Reativacao, on_delete=models.CASCADE, related_name='id_iccids')
    id_equipamentos = models.CharField(max_length=8000, blank=True, default='')
    ccid_equipamentos = models.CharField(max_length=8000, blank=True, default='')
    quantidade = models.IntegerField(default=0, null=True, blank=True)  # Será preenchido com a contagem de linhas
    
    def __str__(self):
        return f"IdIccid {self.id} - ID: {self.id_equipamentos}, ICCID: {self.ccid_equipamentos}, Quantidade: {self.quantidade}"
