from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['razao_social', 'cnpj', 'inicio_de_contrato', 'vigencia']
        widgets = {
            'razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'inicio_de_contrato': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'vigencia': forms.TextInput(attrs={'class': 'form-control'}),
        }
        permissions = [
            ("view_formulario", "Can view formulario"),
            ("add_formulario", "Can add formulario"),
            ("change_formulario", "Can change formulario"),
            ("delete_formulario", "Can delete formulario"),
        ]
        
        
from django import forms
from .models import Faturamento

class FaturamentoForm(forms.ModelForm):
    class Meta:
        model = Faturamento
        fields = [
            'faturamento', 'emissao', 'reajustado', 'reajuste', 'contrato', 'tempo',
            'comercial', 'n_contrato', 'sistema_omie', 'empresa',
            'cliente', 'nome_fantasia', 'email', 'tipo_servico', 'descricao',
            'forma_pagamento', 'vecimento_documento', 'valor_bruto', 'coluna1',
            'valor_liquido', 'juros', 'data_pgto', 'valor_pago', 'status2', 'situacao'
        ]
        widgets = {
            'faturamento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Data de Faturamento'
            }),
            'emissao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Data de Emissão'
            }),
            'reajustado': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Selecione o reajuste'
            }),
            'reajuste': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Data de Reajuste'
            }),
            'contrato': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Tem contrato?'
            }),
            'tempo': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Tempo de contrato'
            }),
            'comercial': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Selecione o comercial'
            }),
            'n_contrato': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número do contrato'
            }),
            'sistema_omie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sistema Omie'
            }),
            'empresa': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Selecione a empresa'
            }),
            'cliente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do cliente'
            }),
            'nome_fantasia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome fantasia'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email do cliente'
            }),
            'tipo_servico': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tipo de serviço'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descrição do serviço'
            }),
            'forma_pagamento': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Forma de pagamento'
            }),
            'vecimento_documento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Data de vencimento'
            }),
        
            'valor_bruto': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Valor bruto'
            }),
            'coluna1': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Coluna 1'
            }),
            'valor_liquido': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Valor líquido'
            }),
            'juros': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Juros'
            }),
            'data_pgto': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Data de pagamento'
            }),
            'valor_pago': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Valor pago'
            }),
            'status2': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Status'
            }),
            'situacao': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Situação'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar as choices dos campos
        self.fields['reajustado'].choices = [('', 'Selecione o reajuste')] + list(Faturamento.reajuste_choice)
        self.fields['contrato'].choices = [('', 'Tem contrato?')] + list(Faturamento.contrato_choices)
        self.fields['tempo'].choices = [('', 'Tempo de contrato')] + list(Faturamento.temp_choices)
        self.fields['comercial'].choices = [('', 'Selecione o comercial')] + list(Faturamento.comercial_choices)
        self.fields['empresa'].choices = [('', 'Selecione a empresa')] + list(Faturamento.empresa_choicea)
        self.fields['forma_pagamento'].choices = [('', 'Forma de pagamento')] + list(Faturamento.forma_ágamento_choices)
        self.fields['documento'].choices = [('', 'Tipo de documento')] + list(Faturamento.tipo_documento_choices)
        self.fields['status2'].choices = [('', 'Status')] + list(Faturamento.status2_choices)
        self.fields['situacao'].choices = [('', 'Situação')] + list(Faturamento.situacao_choices)
        
        # Adicionar classes CSS adicionais para campos obrigatórios
        required_fields = ['cliente', 'valor_bruto', 'vecimento_documento']
        for field_name in required_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['class'] += ' required'
                self.fields[field_name].widget.attrs['required'] = 'required'

class FaturamentoFilterForm(forms.Form):
    """Formulário para filtros de faturamento"""
    
    # Filtros de texto
    n_contrato = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Número do contrato'
        })
    )
    
    nome_fantasia = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome fantasia'
        })
    )
    
    # Filtros de select
    comercial = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos os comerciais')] + list(Faturamento.comercial_choices),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    status2 = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos os status')] + list(Faturamento.status2_choices),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    situacao = forms.ChoiceField(
        required=False,
        choices=[('', 'Todas as situações')] + list(Faturamento.situacao_choices),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    contrato = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos os contratos')] + list(Faturamento.contrato_choices),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    # Filtros de data
    data_inicio = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'Data início'
        })
    )
    
    data_fim = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'Data fim'
        })
    )
    
    # Filtros de valor
    valor_min = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.01',
            'placeholder': 'Valor mínimo'
        })
    )
    
    valor_max = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.01',
            'placeholder': 'Valor máximo'
        })
    )

class FaturamentoUpdateForm(forms.ModelForm):
    """Formulário para atualização de faturamento"""
    
    class Meta:
        model = Faturamento
        fields = [
            'faturamento', 'emissao', 'reajustado', 'reajuste', 'contrato', 'tempo',
            'comercial', 'n_contrato', 'sistema_omie', 'empresa',
            'cliente', 'nome_fantasia', 'email', 'tipo_servico', 'descricao',
            'forma_pagamento', 'vecimento_documento', 'valor_bruto', 'coluna1',
            'valor_liquido', 'juros', 'data_pgto', 'valor_pago', 'status2', 'situacao'
        ]
        widgets = {
            'faturamento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'emissao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'reajustado': forms.Select(attrs={'class': 'form-select'}),
            'reajuste': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'contrato': forms.Select(attrs={'class': 'form-select'}),
            'tempo': forms.Select(attrs={'class': 'form-select'}),
            'comercial': forms.Select(attrs={'class': 'form-select'}),
            'n_contrato': forms.TextInput(attrs={'class': 'form-control'}),
            'sistema_omie': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-select'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_fantasia': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tipo_servico': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'forma_pagamento': forms.Select(attrs={'class': 'form-select'}),
            'vecimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'documento': forms.Select(attrs={'class': 'form-select'}),
            'valor_bruto': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'coluna1': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'valor_liquido': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'juros': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'data_pgto': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'valor_pago': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'status2': forms.Select(attrs={'class': 'form-select'}),
            'situacao': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configurar as choices
        self.fields['reajustado'].choices = [('', 'Selecione o reajuste')] + list(Faturamento.reajuste_choice)
        self.fields['contrato'].choices = [('', 'Tem contrato?')] + list(Faturamento.contrato_choices)
        self.fields['tempo'].choices = [('', 'Tempo de contrato')] + list(Faturamento.temp_choices)
        self.fields['comercial'].choices = [('', 'Selecione o comercial')] + list(Faturamento.comercial_choices)
        self.fields['empresa'].choices = [('', 'Selecione a empresa')] + list(Faturamento.empresa_choicea)
        self.fields['forma_pagamento'].choices = [('', 'Forma de pagamento')] + list(Faturamento.forma_ágamento_choices)
        self.fields['documento'].choices = [('', 'Tipo de documento')] + list(Faturamento.tipo_documento_choices)
        self.fields['status2'].choices = [('', 'Status')] + list(Faturamento.status2_choices)
        self.fields['situacao'].choices = [('', 'Situação')] + list(Faturamento.situacao_choices)