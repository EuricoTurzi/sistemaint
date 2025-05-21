from django.db import models

# Create your models here.
class Cadastro(models.Model):
    empresa = models.CharField(max_length=50,null=True,blank=True)
    data_entrada = models.CharField(max_length=50,null=True,blank=True)
    pesquisa = models.CharField(max_length=50,null=True,blank=True)
    estado1 = models.CharField(max_length=50,null=True,blank=True)
    estado2 = models.CharField(max_length=50,null=True,blank=True)
    estado3 = models.CharField(max_length=50,null=True,blank=True)
    estado4 = models.CharField(max_length=50,null=True,blank=True)
    estado5 = models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=50,null=True,blank=True)
    hora_devolutiva = models.CharField(max_length=50,null=True,blank=True)
    sla = models.CharField(max_length=50,null=True,blank=True)
    periodo = models.CharField(max_length=50,null=True,blank=True)
    estados = models.CharField(max_length=50,null=True,blank=True)
    cpfcnpj = models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return {self.empresa} - {self.data_entrada} - {self.hora_devolutiva}
    
    
class Pesquisa (models.Model):
    
    modo_choices = [
        ('Pesquisa','Pesquisa'),
        ('consulta','Consulta'),
    ]
    plano_choice = [
        ('Individual','Individual'),
        ('Combo','Combo'),
    ]
    resultado_choice = [
        ('Adequado','Adequado'),
        ('Inadequado','Inadequado'),
    ]
    periodo_choice = [
        ('Matutino','Matutino'),
        ('Vespertino','Vespertino'),
        ('Noturno','Noturno'),
    ]
    empresa = models.CharField(max_length=50,null=True,blank=True)
    data = models.CharField(max_length=50,null=True,blank=True)
    modo = models.CharField(choices=modo_choices,max_length=50,null=True,blank=True)
    plano = models.CharField(choices=plano_choice,max_length=50,null=True,blank=True)
    perfil = models.CharField(max_length=50,null=True,blank=True)
    placa = models.CharField(max_length=50,null=True,blank=True)
    resultado = models.CharField(choices=resultado_choice,max_length=50,null=True,blank=True)
    periodo = models.CharField(choices=periodo_choice,max_length=50,null=True,blank=True)
    
    def __str__(self):
        return {self.empresa}
