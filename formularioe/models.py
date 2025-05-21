from django.db import models
from acompanhamento.models import Clientes   
from produto.models import Produto    


class formularioe(models.Model):
    entrada = [

        ('Manutenção' , 'Manutenção'),
        ('Devolução/Estoque' , 'Devolução/Estoque' ),
        
    ]

    customizacoes = [

        ('Sem custumização' , 'Sem custumização'),
        ('Caixa de papelão' , 'Caixa de papelão' ),
        ('Caixa de papelão (bateria desacoplada)' , 'Caixa de papelão (bateria desacoplada)'),
        ('Caixa de papelão + DF' , 'Caixa de papelão + DF'),
        ('Termo branco' , 'Termo branco'),
        ('Termo branco + D.F ' , 'Termo branco + D.F'),
        ('Termo branco slim ' , 'Termo branco slim'),
        ('Termo branco slim + D.F +EQT  ' , 'Termo branco slim + D.F +EQT'),
        ('Termo cinza slim + D.F +EQT  ' , 'Termo cinza slim + D.F +EQT'),
        ('Termo branco  (isopor) ' , 'Termo branco  (isopor)'),
        ('Termo branco - bateria externa ' , 'Termo branco - bateria externa'),
        ('Termo marrom + imã' , 'Termo marrom + imã'),
        ('Termo cinza' , 'Termo cinza'),
        ('Termo cinza + imã' , 'Termo cinza + imã'),
        ('Termo preto' , 'Termo preto'),
        ('Termo preto + imã' , 'Termo preto + imã'),
        ('Termo brabco |marrim-slim' , 'Termo brabco |marrim-slim'),
        ('Termo marrom slim +D.F + EQT' , 'Termo marrom slim +D.F + EQT'),
        ('Termo marrom' , 'Termo marrom'),
        ('Caixa blindada' , 'Caixa blindada'),
        ('Tênis/ Sapato' , 'Tênis/ Sapato'),
        ('Projetor' , 'Projetor'),
        ('Caixa de som' , 'Caixa de som'),
        ('Luminaria' , 'Luminaria'),
        ('Alexa' , 'Alexa'),
        ('Video Game' , 'Video Game'),
        ('Secador de cabelo' , 'Secador de cabelo'),
        ('Roteador' , 'Roteador'),
        ('Relogio digital' , 'Relogio digital'),


    ]
    recebimento_tipo = [

        ('Correios/Transportadora' , 'Correios/Transportadora'),
        ('Entrga na base' , 'Entrga na base' ),
        ('Retirado pelo cliente' , 'Retirado pelo cliente'),
       
        
    ]

    nome = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='formularioe_nome') 
    tipo_entrada = models.CharField(choices= entrada, null=True , blank=True, max_length=50)
    tipo_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='formularioe_produto')
    tipo_customizacao = models.CharField(choices=customizacoes ,null=True,blank=True, max_length=50)
    recebimento = models.CharField(choices=recebimento_tipo ,null=True,blank=True, max_length=50)
    entregue_por_retirado_por = models.CharField(max_length= 100)
    id_equipamentos = models.CharField(max_length=100, blank=True, default='')
    



    def __str__(self):
        return f"Manutencaoe {self.id} - {self.nome}"
