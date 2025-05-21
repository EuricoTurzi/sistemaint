# models.py
from django.db import models

class GridInternacional(models.Model):
    cliente                     = models.CharField("Cliente", max_length=255, null=True, blank=True)
    local_de_entrega            = models.CharField("Local de Entrega", max_length=255, null=True, blank=True)
    modelo                      = models.CharField("Modelo", max_length=255, null=True, blank=True)
    id_planilha                 = models.CharField("ID", max_length=255, null=True, blank=True)
    ccid                        = models.CharField("CCID", max_length=255, null=True, blank=True)
    sla_insercao                = models.CharField("SLA de Inserção", max_length=255, null=True, blank=True)
    data_insercao               = models.DateField("Data / Inserção", null=True, blank=True)
    destino                     = models.CharField("Destino", max_length=255, null=True, blank=True)
    bl                          = models.CharField("BL", max_length=255, null=True, blank=True)
    container                   = models.CharField("Container", max_length=255, null=True, blank=True)
    sla_viagem                  = models.CharField("SLA de Viagem", max_length=255, null=True, blank=True)
    data_chegada_destino        = models.DateField("Data / Chegada no Destino", null=True, blank=True)
    sla_retirada                = models.CharField("SLA de Retirada", max_length=255, null=True, blank=True)
    data_retirada               = models.DateField("Data / Retirada", null=True, blank=True)
    sla_envio_brasil            = models.CharField("SLA / Envio ao Brasil", max_length=255, null=True, blank=True)
    data_envio_brasil           = models.DateField("Data / Envio ao Brasil", null=True, blank=True)
    sla_chegada_brasil          = models.CharField("SLA / Chegada ao Brasil", max_length=255, null=True, blank=True)
    data_brasil                 = models.DateField("Data / Brasil", null=True, blank=True)
    status_operacao             = models.CharField("Status / Operação", max_length=255, null=True, blank=True)
    sla_operacao                = models.CharField("SLA da Operação", max_length=255, null=True, blank=True)
    reposicao                   = models.CharField("Reposição", max_length=255, null=True, blank=True)
    observacao                  = models.TextField("Observação", null=True, blank=True)
    data_chegada_porto          = models.DateField("Data / Chegada no Porto", null=True, blank=True)
    data_embarque_maritimo      = models.DateField("Data / Embarque Marítimo", null=True, blank=True)
    data_desembarque_maritimo   = models.DateField("Data / Desembarque Marítimo", null=True, blank=True)
    data_chegada_terminal       = models.DateField("Data / Chegada no Terminal", null=True, blank=True)
    data_saida_terminal         = models.DateField("Data / Saída do Terminal", null=True, blank=True)
    sla_porto_nacional          = models.CharField("SLA Porto Nacional", max_length=255, null=True, blank=True)
    sla_terrestre               = models.CharField("SLA Terrestre", max_length=255, null=True, blank=True)
    sla_maritimo                = models.CharField("SLA Marítimo", max_length=255, null=True, blank=True)
    sla_terminal_internacional  = models.CharField("SLA Terminal Internacional", max_length=255, null=True, blank=True)
    sla_terrestre_internacional = models.CharField("SLA Terrestre Internacional", max_length=255, null=True, blank=True)
    local                       = models.CharField("Local", max_length=255, null=True, blank=True)
    status_container            = models.CharField("Status do Container", max_length=255, null=True, blank=True)
    data_desembarque            = models.DateField("Data do Desembarque", null=True, blank=True)
    sla_internacional           = models.CharField("SLA Internacional", max_length=255, null=True, blank=True)
    ultimo_grid                 = models.CharField("Último Grid", max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.cliente} — {self.container or 'sem container'}"
from django.db import models

# Create your models here.
