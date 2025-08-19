# models.py
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from datetime import timedelta # Necessário para calcular_slas
import requests

class GridInternacional(models.Model):
    STATUS_CHOICES = [
        ('Aguardando Liberação RFB', 'Aguardando Liberação RFB'),
        ('Aguardando Chegada na Base', 'Aguardando Chegada na Base'),
        ('Aguardando Coleta', 'Aguardando Coleta'),
        ('Aguardando Embarque Internacional', 'Aguardando Embarque Internacional'),
        ('Em reversa para o Brasil', 'Em reversa para o Brasil'),
        ('Retirado, Ag. Envio', 'Retirado, Ag. Envio'),
        ('Em viagem', 'Em viagem'),
        ('No destino', 'No destino'),
        ('Estoque Cliente', 'Estoque Cliente'),
        ('Danificado', 'Danificado'),
        ('Extraviado', 'Extraviado'),
        ('Reversa Finalizada', 'Reversa Finalizada'),
    ]

    id = models.BigAutoField(primary_key=True) 
    data_envio                  = models.DateField("Data de Envio", null=True, blank=True)
    requisicao                  = models.CharField("Requisição", max_length=255, null=True, blank=True)
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
    status_operacao             = models.CharField("Status / Operação", max_length=255, null=True, blank=True, choices=STATUS_CHOICES)
    sla_operacao                = models.CharField("SLA da Operação", max_length=255, null=True, blank=True)
    reposicao                   = models.CharField("Reposição", max_length=255, null=True, blank=True)
    observacao                  = models.TextField("Observação", null=True, blank=True)
    data_chegada_porto          = models.DateField("Data / Chegada no Porto", null=True, blank=True)
    data_embarque_maritimo      = models.DateField("Data / Embarque Marítimo", null=True, blank=True)
    data_desembarque_maritimo   = models.DateField("Data / Desembarque Marítimo", null=True, blank=True)
    data_envoice                = models.DateField("Data / envoice", null=True, blank=True)
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
    rf_invoice                  = models.CharField("RF Invoice", max_length=255, null=True, blank=True)
    data_envoice                = models.DateField("Data / envoice", null=True, blank=True)
    coleta                      = models.DateField("Coleta", null=True, blank=True)
    liberacao                  = models.DateField("Liberacao", null=True, blank=True)
    golden_sat                  = models.DateField("GoldenSat", null=True, blank=True)
    sla_destino                 = models.CharField("SLA Destino", max_length=255, null=True, blank=True)
   

    def __str__(self):
        return f"{self.cliente} — {self.container or 'sem container'}"

    def calcular_slas(self):
        def diff_days(a, b):
            if a and b:
                return (a - b).days
            return ''
        self.sla_insercao = diff_days(self.data_insercao, self.data_envio)
        self.sla_viagem = diff_days(self.data_chegada_destino, self.data_insercao)
        self.sla_retirada = diff_days(self.data_retirada, self.data_chegada_destino)
        self.sla_envio_brasil = diff_days(self.data_envio_brasil, self.data_retirada)
        self.sla_chegada_brasil = diff_days(self.data_brasil, self.data_envio_brasil)
        self.sla_terrestre_nacional = diff_days(self.data_chegada_porto, self.data_insercao)
        self.sla_embarque = diff_days(self.data_embarque_maritimo, self.data_chegada_porto)
        self.sla_maritimo = diff_days(self.data_desembarque_maritimo, self.data_embarque_maritimo)
        self.sla_terrestre_internacional = diff_days(self.data_chegada_destino, self.data_desembarque_maritimo)
        self.sla_terrestre = diff_days(self.data_chegada_destino, self.data_desembarque_maritimo)
        self.sla_internacional = diff_days(self.data_retirada, self.data_chegada_destino)
       
        # Soma total dos SLAs exibidos
        sla_soma = 0
        for v in [
            self.sla_insercao, self.sla_retirada, self.sla_envio_brasil, self.sla_chegada_brasil,
            self.sla_terrestre_nacional, self.sla_embarque, self.sla_maritimo,
            self.sla_terrestre_internacional, self.sla_terrestre, self.sla_internacional,
           
        ]:
            if v not in [None, '', ' ']:
                try:
                    sla_soma += int(v)
                except Exception:
                    pass
        self.sla_operacao = sla_soma

    def save(self, *args, **kwargs):
        self.calcular_slas()
        super().save(*args, **kwargs)

    def get_status_automatico(self):
        # Se o status for Danificado, retorna Danificado independente das datas
        if self.status_operacao == 'Danificado':
            return 'Danificado'
            
        # NOVA LÓGICA: Se todas as datas relevantes estiverem vazias, retorna 'Equipamento na Base'
        datas = [
            self.data_envio,
            self.data_insercao,
            self.data_chegada_destino,
            self.data_retirada,
            self.data_envio_brasil,
            self.data_brasil,
            self.data_chegada_porto,
            self.data_embarque_maritimo,
            self.data_desembarque_maritimo,
            self.data_chegada_terminal,
            self.data_saida_terminal,
            self.data_desembarque,
            self.coleta,
            self.liberacao,
            self.golden_sat,
            self.data_envoice,
        ]
        if all(d is None or d == '' for d in datas):
            if self.status_operacao != 'Equipamento na Base':
                self.status_operacao = 'Equipamento na Base'
                self.save(update_fields=['status_operacao'])
            return 'Equipamento na Base'
        status = None
        
        if self.status_operacao == 'Extraviado':
            status = 'Extraviado'
        elif self.golden_sat:
            status = 'Reversa Finalizada'
        elif self.liberacao:
            status = 'Aguardando Chegada na Base'
        elif self.coleta:
            status = 'Aguardando Embarque Internacional'
        elif self.data_brasil:
            status = 'Aguardando Liberação RFB'
        elif self.data_envoice:
            status = 'Aguardando Coleta'
        elif self.data_envio_brasil:
            status = 'Em reversa para o Brasil'
        elif self.data_retirada:
            status = 'Retirado, Ag. Envio'
        elif self.data_chegada_destino:
            status = 'No destino'
        elif self.data_envio and not self.data_insercao and not self.data_envio_brasil and not self.data_chegada_destino:
            status = 'Estoque Cliente'
        elif self.data_envio and self.data_insercao and not self.data_envio_brasil and not self.data_chegada_destino:
            status = 'Em viagem'
        elif self.status_operacao == 'Estoque Cliente':
            status = 'Estoque Cliente'
        else:
            status = 'GoldenSat'

        # Se o status foi alterado, atualiza o status_operacao no banco de dados
        if status != self.status_operacao:
            self.status_operacao = status
            self.save(update_fields=['status_operacao'])

        return status

    @classmethod
    def atualizar_status_existentes(cls):
        """
        Atualiza os status existentes no banco de dados para os novos valores padronizados.
        """
        # Mapeamento de status antigos para novos
        mapeamento_status = {
            'Aguardando Liberação': 'Aguardando Liberação RFB',
            'Em Viagem': 'Em viagem',
            'Estoque Golden': 'Estoque Cliente',
            'Aguardando Envio': 'Aguardando Embarque Internacional',
            # Adicione outros mapeamentos conforme necessário
        }

        # Atualiza todos os registros
        for registro in cls.objects.all():
            status_antigo = registro.status_operacao
            if status_antigo in mapeamento_status:
                registro.status_operacao = mapeamento_status[status_antigo]
                registro.save(update_fields=['status_operacao'])
            # Se o status não estiver no mapeamento, recalcula usando get_status_automatico
            else:
                registro.get_status_automatico()

    def sla_operacao_dias(self):
        if self.golden_sat and self.data_envio:
            return (self.golden_sat - self.data_envio).days
        return ''

    def rejeitar(self):
        """Rejeita a cotação"""
        self.status = 'rejeitado'
        self.save(update_fields=['status'])




class clientesNestle(models.Model):
    cliente = models.CharField("Cliente", max_length=255, null=True, blank=True)
    cnpj = models.CharField("CNPJ", max_length=255, null=True, blank=True)
    endereco = models.CharField("Endereço", max_length=255, null=True, blank=True)
    quantidade = models.IntegerField("Quantidade",  null=True, blank=True)
    valor = models.DecimalField("Valor", max_digits=10, decimal_places=2, null=True, blank=True)
    local = models.CharField("Local", max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.cliente} — {self.cnpj or 'sem cnpj'}"




class ValorMensalCliente(models.Model):
    MESES_CHOICES = [
        ('01', 'Janeiro'),
        ('02', 'Fevereiro'),
        ('03', 'Março'),
        ('04', 'Abril'),
        ('05', 'Maio'),
        ('06', 'Junho'),
        ('07', 'Julho'),
        ('08', 'Agosto'),
        ('09', 'Setembro'),
        ('10', 'Outubro'),
        ('11', 'Novembro'),
        ('12', 'Dezembro'),
    ]

    cliente = models.ForeignKey('clientesNestle', on_delete=models.CASCADE)
    mes = models.CharField(max_length=2, choices=MESES_CHOICES)
    ano = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    enviado = models.BooleanField(default=False)
    data_envio = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ['cliente', 'mes', 'ano']
        ordering = ['cliente__cliente', 'ano', 'mes']

    def __str__(self):
        return f"{self.cliente.cliente} - {self.get_mes_display()}/{self.ano}"

from decimal import Decimal
from django.db import models

CURRENCY_CHOICES = [
    ('EUR', 'Euro'),
    ('USD', 'Dólar'),
    ('BRL', 'Real'),
]












class Carga(models.Model):
    TIPO_CHOICES = [
        ('FEDEX', 'FedEx'),
        ('DHL', 'DHL'),
        ('Agente', 'Agente'),
    ]

    data                = models.DateField()
    tipo_transportadora = models.CharField("Transportadora", max_length=15, choices=TIPO_CHOICES, default='Agente')
    
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Aprovada', 'Aprovada'),
        ('Reprovada', 'Reprovada'),
    ]
    status = models.CharField("Status da Cotação", max_length=10, choices=STATUS_CHOICES, default='Pendente')

    # ─── FRETE ALL IN ───────────────────────────
    frete_all_in_valor  = models.DecimalField("Frete ALL IN (EUR)", max_digits=12, decimal_places=2)
    frete_all_in_usd    = models.DecimalField("Frete ALL IN (USD)", max_digits=12, decimal_places=2, null=True, blank=True)
    frete_all_in_moeda  = models.CharField("Moeda", max_length=3, choices=CURRENCY_CHOICES)
    frete_all_in_brl    = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    cotacao_usada       = models.DecimalField(max_digits=10, decimal_places=4, editable=False)
    cotacao_dolar_na_data = models.DecimalField(max_digits=10, decimal_places=4, editable=False, null=True, blank=True)
    cotacao_euro_na_data = models.DecimalField(max_digits=10, decimal_places=4, editable=False, null=True, blank=True)
    frete_all_in_eur_brl = models.DecimalField(max_digits=12, decimal_places=2, editable=False, null=True, blank=True)
    frete_all_in_usd_brl = models.DecimalField(max_digits=12, decimal_places=2, editable=False, null=True, blank=True)

    # ─── DEMAIS CUSTOS (em BRL) ────────────────
    honorarios          = models.DecimalField(max_digits=12, decimal_places=2)
    frete_rodoviario    = models.DecimalField(max_digits=12, decimal_places=2)
    licenca_importacao  = models.DecimalField(max_digits=12, decimal_places=2)
    taxa_siscomex       = models.DecimalField(max_digits=12, decimal_places=2)
    taxa_armazenagem    = models.DecimalField(max_digits=12, decimal_places=2)

    # ─── Qtd & totais ──────────────────────────
    qtd_equipamento     = models.PositiveIntegerField()
    total               = models.DecimalField(max_digits=14, decimal_places=2, editable=False)
    valor_por_equip     = models.DecimalField(max_digits=14, decimal_places=2, editable=False)
    
    rf_invoice          = models.CharField("RF Invoice", max_length=255, null=True, blank=True)
    data_invoice        = models.DateField("Data Invoice", null=True, blank=True)
    origem              = models.CharField("Origem", max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Converte frete ALL IN para BRL na hora de salvar e calcula total/valor-unit.
        """
        self.cotacao_dolar_na_data = self.get_rate_to_brl('USD')
        self.cotacao_euro_na_data = self.get_rate_to_brl('EUR')
        
        # Garante que os campos de valor de entrada sejam Decimal, tratando None como 0
        frete_eur_input = self.frete_all_in_valor if self.frete_all_in_valor is not None else Decimal('0.00')
        frete_usd_input = self.frete_all_in_usd if self.frete_all_in_usd is not None else Decimal('0.00')

        # Calcula o frete ALL IN em BRL para EUR e USD separadamente
        self.frete_all_in_eur_brl = (frete_eur_input * self.cotacao_euro_na_data).quantize(Decimal('0.01'))
        self.frete_all_in_usd_brl = (frete_usd_input * self.cotacao_dolar_na_data).quantize(Decimal('0.01'))

        # Define a cotacao_usada baseada na moeda principal do frete_all_in_valor
        if self.frete_all_in_moeda == 'EUR':
            self.cotacao_usada = self.cotacao_euro_na_data
        elif self.frete_all_in_moeda == 'USD':
            self.cotacao_usada = self.cotacao_dolar_na_data
        else:
            self.cotacao_usada = Decimal('1.0000') # Se for BRL

        # O frete_all_in_brl agora será a soma das conversões de EUR e USD
        self.frete_all_in_brl = (self.frete_all_in_eur_brl + self.frete_all_in_usd_brl).quantize(Decimal('0.01'))

        self.total = (
            self.frete_all_in_brl + self.honorarios + self.frete_rodoviario +
            self.licenca_importacao + self.taxa_siscomex + self.taxa_armazenagem
        ).quantize(Decimal('0.01'))

        self.valor_por_equip = (self.total / self.qtd_equipamento).quantize(Decimal('0.01'))
        super().save(*args, **kwargs)

    # ─── util ──────────────────────────────────
    @staticmethod
    def get_rate_to_brl(code: str) -> Decimal:
        """
        Busca a cotação atual → BRL usando a API do Banco Central do Brasil.
        Retorna 1 se já for BRL.
        """
        if code == 'BRL':
            return Decimal('1')
        
        try:
            # API do Banco Central do Brasil
            r = requests.get(
                'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos/1?formato=json',
                timeout=10
            )
            r.raise_for_status()
            data = r.json()
            
            if not data or not isinstance(data, list) or len(data) == 0:
                raise ValueError("Invalid response format from BCB API")
            
            # O valor retornado é a cotação do dólar
            usd_rate = Decimal(str(data[0]['valor']))
            
            if code == 'USD':
                return usd_rate
            elif code == 'EUR':
                # Para EUR, precisamos fazer uma segunda chamada
                r = requests.get(
                    'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21619/dados/ultimos/1?formato=json',
                    timeout=10
                )
                r.raise_for_status()
                eur_data = r.json()
                
                if not eur_data or not isinstance(eur_data, list) or len(eur_data) == 0:
                    raise ValueError("Invalid response format from BCB API for EUR")
                
                eur_rate = Decimal(str(eur_data[0]['valor']))
                return eur_rate
            
            raise ValueError(f"Unsupported currency code: {code}")
            
        except (requests.RequestException, ValueError, KeyError, IndexError) as e:
            # Em caso de erro, retorna uma cotação padrão
            print(f"Error fetching exchange rate: {str(e)}")
            if code == 'USD':
                return Decimal('5.00')  # Cotação padrão USD
            elif code == 'EUR':
                return Decimal('5.50')  # Cotação padrão EUR
            return Decimal('1.00')  # Fallback
