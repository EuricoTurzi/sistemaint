from django import forms
from .models import Requisicoes, Clientes,estoque_antenista
from datetime import datetime

class RequisicaoForm(forms.ModelForm):
    class Meta:
        model = Requisicoes
        fields = [
            'nome', 'endereco', 'data_entrega', 'contrato', 'cnpj', 'inicio_de_contrato', 
            'vigencia', 'motivo', 'antenista', 'envio', 'comercial', 'tipo_produto', 
            'aos_cuidados', 'carregador', 'cabo', 'tipo_fatura', 'valor_unitario', 
            'valor_total', 'forma_pagamento', 'tipo_customizacao', 'numero_de_equipamentos', 
            'observacoes', 'status', 'TP', 'taxa_envio', 'status_faturamento',
        ]
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'numero_de_equipamentos': forms.TextInput(attrs={'class': 'form-control'}),
            'contrato': forms.Select(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'inicio_de_contrato': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'vigencia': forms.Select(attrs={'class': 'form-control'}),
            'data_entrega': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'motivo': forms.Select(attrs={'class': 'form-control'}),
            'antenista': forms.Select(attrs={'class': 'form-control'}),
            'comercial': forms.Select(attrs={'class': 'form-control'}),
            'tipo_produto': forms.Select(attrs={'class': 'form-control'}),
            'envio': forms.Select(attrs={'class': 'form-control'}),
            'taxa_envio': forms.NumberInput(attrs={'class': 'form-control'}),
            'carregador': forms.TextInput(attrs={'class': 'form-control'}),
            'cabo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_customizacao': forms.Select(attrs={'class': 'form-control'}),
            'tipo_fatura': forms.Select(attrs={'class': 'form-control'}),
            'valor_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'forma_pagamento': forms.TextInput(attrs={'class': 'form-control'}),
            'aos_cuidados': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'TP': forms.Select(attrs={'class': 'form-control'}),
            'status_faturamento': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        editable_fields = kwargs.pop('editable_fields', None)
        super().__init__(*args, **kwargs)
        
        self.fields['nome'].queryset = Clientes.objects.all()
        self.fields['nome'].empty_label = "Selecione um cliente"

        if editable_fields:
            for field_name in self.fields:
                if field_name not in editable_fields:
                    self.fields[field_name].widget.attrs['readonly'] = 'readonly'


class requisicaoFormup(forms.ModelForm):
    class Meta:
        model = Requisicoes
        fields = ['nome', 'endereco', 'contrato', 'cnpj', 'inicio_de_contrato', 'vigencia', 
                  'motivo', 'envio', 'comercial', 'tipo_produto', 
                  'carregador', 'cabo', 'tipo_fatura', 'valor_unitario', 'valor_total',
                  'forma_pagamento','tipo_customizacao', 'numero_de_equipamentos', 'observacoes', 'status', 'TP', 'taxa_envio','id_equipamentos']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'numero_de_equipamentos': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'contrato': forms.Select(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'inicio_de_contrato': forms.DateInput(attrs={'class': 'form-control'}),
            'vigencia': forms.Select(attrs={'class': 'form-control'}),
            
            'motivo': forms.Select(attrs={'class': 'form-control'}),
            'comercial': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_produto': forms.Select(attrs={'class': 'form-control'}),
            'envio': forms.Select(attrs={'class': 'form-control'}),
            'taxa_envio': forms.NumberInput(attrs={'class': 'form-control'}),
            'carregador': forms.TextInput(attrs={'class': 'form-control'}),
            'cabo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_customizacao': forms.Select(attrs={'class': 'form-control'}),
            'tipo_fatura': forms.Select(attrs={'class': 'form-control'}),
            'valor_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'forma_pagamento': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'TP': forms.Select(attrs={'class': 'form-control'}),
            
            
            'id_equipamentos': forms.TextInput(attrs={'class': 'form-control'}),
         
        }
        permissions = [
            ("view_requisicoes", "Can view requisicoes"),
            ("add_requisicoes", "Can add requisicoes"),
            ("change_requisicoes", "Can change requisicoes"),
            ("delete_requisicoes", "Can delete requisicoes"),
        ]

    def __init__(self, *args, **kwargs):
        editable_fields = kwargs.pop('editable_fields', None)
        super().__init__(*args, **kwargs)
        self.fields['nome'].queryset = Clientes.objects.all()
        self.fields['nome'].empty_label = "Selecione um cliente"

        if editable_fields:
            for field_name in self.fields:
                if field_name not in editable_fields:
                    self.fields[field_name].widget.attrs['readonly'] = 'readonly'


from django import forms
from django.core.exceptions import ValidationError
from .models import Requisicoes, Clientes, estoque_antenista

class RequisicoesForm(forms.ModelForm):
    class Meta:
        model = Requisicoes
        fields = '__all__'
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.Select(attrs={'class': 'form-control', 'onchange': 'toggleAntenistaField()'}),
            'antenista': forms.Select(attrs={'class': 'form-control', 'style': 'display:none;', 'id': 'antenista-field'}),
            'tipo_produto': forms.Select(attrs={'class': 'form-control'}),
            'numero_de_equipamentos': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_equipamentos': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'contrato': forms.Select(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'inicio_de_contrato': forms.DateInput(attrs={'class': 'form-control'}),
            'vigencia': forms.Select(attrs={'class': 'form-control'}),
            'comercial': forms.TextInput(attrs={'class': 'form-control'}),
            'envio': forms.Select(attrs={'class': 'form-control'}),
            'taxa_envio': forms.NumberInput(attrs={'class': 'form-control'}),
            'carregador': forms.TextInput(attrs={'class': 'form-control'}),
            'cabo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_customizacao': forms.Select(attrs={'class': 'form-control'}),
            'tipo_fatura': forms.Select(attrs={'class': 'form-control'}),
            'valor_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'forma_pagamento': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'TP': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].queryset = Clientes.objects.all()
        self.fields['antenista'].widget = forms.Select(choices=[
            
            ('ALCIDES', 'ALCIDES'),
            ('EZEQUIEL', 'EZEQUIEL'),
            ('NILDO', 'NILDO'),
            ('ALEX', 'ALEX'),
            ('ANDERSON', 'ANDERSON'),
            ('ANTONIEQUE', 'ANTONIEQUE'),
            ('OSNI', 'OSNI'),
            ('ELTON', 'ELTON'),
            ('NEY', 'NEY'),
            ('ANDRÉ', 'ANDRÉ'),
            ('RILDO', 'RILDO'),
            ('WELLINGTHON', 'WELLINGTHON'),
            ('GERSON WALACE', 'GERSON WALACE'),
            ('JUSTINO', 'JUSTINO'),
            ('ANTONIO', 'ANTONIO'),
            ('FRANCISCO', 'FRANCISCO'),
            ('OSMAN', 'OSMAN'),
            ('TONHARA', 'TONHARA'),
            ('EMERSON', 'EMERSON'),
            ('MARCELO', 'MARCELO'),
            ('JEFFERSON', 'JEFFERSON'),
            ('GUILHERME', 'GUILHERME'),
            ('MARCIO', 'MARCIO'),
            ('SAMPAIO', 'SAMPAIO'),
            ('DIOGO', 'DIOGO'),
            ('WESLEY', 'WESLEY'),
            ('EVERALDO / SAMUEL', 'EVERALDO / SAMUEL'),
            ('ERIK', 'ERIK'),
            ('LUCAS CARVALHO', 'LUCAS CARVALHO'),
            ('RODRIGO', 'RODRIGO'),
            ('PITTA', 'PITTA'),
            ('JUSTO', 'JUSTO'),
            ('PAULO HENRIQUE', 'PAULO HENRIQUE'),
            ('EDUARDO', 'EDUARDO'),
            ('YURI', 'YURI'),
            ('RAFAEL', 'RAFAEL'),
        ], attrs={'class': 'form-control'})
        self.fields['antenista'].required = True
        self.fields['id_equipamentos'] = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        motivo = cleaned_data.get('motivo')
        antenista = cleaned_data.get('antenista')
        tipo_produto = cleaned_data.get('tipo_produto')
        numero_de_equipamentos = cleaned_data.get('numero_de_equipamentos')

        if motivo == 'Isca FAST' and antenista and tipo_produto and numero_de_equipamentos:
            try:
                antenista_estoque = estoque_antenista.objects.get(nome=antenista, tipo_produto=tipo_produto)
                quantidade_requisitada = int(numero_de_equipamentos)
                if antenista_estoque.quantidade < quantidade_requisitada:
                    raise ValidationError(f"O antenista {antenista} não tem quantidade suficiente no estoque para o produto {tipo_produto}. Quantidade disponível: {antenista_estoque.quantidade}, quantidade requisitada: {quantidade_requisitada}.")
            except estoque_antenista.DoesNotExist:
                raise ValidationError(f"O antenista {antenista} ou o produto {tipo_produto} não existem no estoque.")

        return cleaned_data

class EstoqueantenistarForm(forms.ModelForm):
    class Meta:
        model = estoque_antenista
        fields = ['nome', 'tipo_produto', 'quantidade', 'endereco']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['tipo_produto'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['endereco'].widget.attrs.update({'class': 'form-control'})


# models.py
# forms.py
from django import forms
from .models import ControleModel

class ControleForm(forms.ModelForm):
    class Meta:
        model = ControleModel
        fields = ['cliente', 'requisicao_id', 'quantidade' ,'iccid_equipamento1', 'id_equipamento1', 'iccid_equipamento2', 'id_equipamento2',
                  'iccid_equipamento3', 'id_equipamento3', 'iccid_equipamento4', 'id_equipamento4', 'iccid_equipamento5',
                  'id_equipamento5', 'iccid_equipamento6', 'id_equipamento6', 'iccid_equipamento7', 'id_equipamento7',
                  'iccid_equipamento8', 'id_equipamento8', 'iccid_equipamento9', 'id_equipamento9', 'iccid_equipamento10',
                  'id_equipamento10']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'requisicao_id': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade': forms.TextInput(attrs={'class': 'form-control'}),
            'iccid_equipamento1': forms.TextInput(attrs={'class': 'form-control'}),
            'id_equipamento1': forms.TextInput(attrs={'class': 'form-control'}),
            'iccid_equipamento2': forms.TextInput(attrs={'class': 'form-control'}),
            'id_equipamento2': forms.TextInput(attrs={'class': 'form-control'}),
            'iccid_equipamento3': forms.TextInput(attrs={'class': 'form-control'}),
            'id_equipamento3': forms.TextInput(attrs={'class': 'form-control'}),
            'iccid_equipamento4': forms.TextInput(attrs={'class': 'form-control'}),
            'id_equipamento4': forms.TextInput(attrs={'class': 'form-control'}),
            'iccid_equipamento5': forms.TextInput(attrs={'class': 'form-control'}),
            'id_equipamento5': forms.TextInput(attrs={'class': 'form-control'}),
            'iccid_equipamento6': forms.TextInput(attrs={'class': 'form-control'}),
            'id_equipamento6': forms.TextInput(attrs={'class': 'form-control'}),
            'iccid_equipamento7': forms.TextInput(attrs={'class': 'form-control'}),
            'id_equipamento7': forms.TextInput(attrs={'class': 'form-control'}),
            'iccid_equipamento8': forms.TextInput(attrs={'class': 'form-control'}),
            'id_equipamento8': forms.TextInput(attrs={'class': 'form-control'}),
            'iccid_equipamento9': forms.TextInput(attrs={'class': 'form-control'}),
            'id_equipamento9': forms.TextInput(attrs={'class': 'form-control'}),
            'iccid_equipamento10': forms.TextInput(attrs={'class': 'form-control'}),
            'id_equipamento10': forms.TextInput(attrs={'class': 'form-control'}),
        }



from .models import antenista_CARD
class antenista_Form(forms.ModelForm):
    class Meta:
        model = antenista_CARD  # Substitua pelo nome do seu modelo
        fields = ['nome', 'tipo_produto', 'solicitante','telefone', 'cliente', 'quantidade','equipamentos','contrato','valor_entrega']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'tipo_produto': forms.Select(attrs={'class': 'form-control'}),
            'solicitante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Solicitante'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o telefone'}),
            'equipamentos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IDS'}),
            'valor_entrega': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'valor'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade'}),
            'contrato': forms.Select(attrs={'class': 'form-control'}),
        }
