from django import forms
from .models import Formacompanhamento, agentes
import datetime
from datetime import timedelta


# Não é necessário importar Cliente aqui, a menos que seja usado em outro lugar do código.

class formacompanhamentoForm(forms.ModelForm):
    class Meta:
        model = Formacompanhamento
        fields = ['data_inicio', 'data_final', 'prestador', 'agente', 'placa','id_equipamento','km_inicial','km_final','pedagio']
        widgets = {
            'data_inicio': forms.DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'data_final': forms.DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'prestador': forms.Select(attrs={'class': 'form-control'}),
            'agente': forms.Select(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),
            'id_equipamento': forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),
            'km_inicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'km_final': forms.NumberInput(attrs={'class': 'form-control'}),
            'pedagio':forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
        }


class agentesForm(forms.ModelForm):
    class Meta:
        model = agentes
        fields = ['agente', 'placa', 'franquia_hora', 'franquia_km']
        widgets = {
            'agente': forms.TextInput(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'franquia_hora': forms.NumberInput(attrs={'class': 'form-control'}),  # Use NumberInput para campos numéricos
            'franquia_km': forms.NumberInput(attrs={'class': 'form-control'}),    # Use NumberInput para campos numéricos
        }


from django import forms
from datetime import timedelta
from .models import RegistroPagamento
from django import forms
from datetime import timedelta
from .models import RegistroPagamento
import re
from django import forms
from .models import Registro

class RegistroPagamentoForm(forms.ModelForm):
    class Meta:
        model = RegistroPagamento
        fields = ['cliente', 'protocolo', 'prestador', 'acionamento', 'franquia_hora', 'km_franquia', 'valor_hora_excedente', 'valor_km_excedente']
        
    cliente = forms.ModelChoiceField(queryset=Registro.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


from django import forms
from .models import Registro, RegistroPagamento


class RegistroPagamentoForm(forms.ModelForm):
    class Meta:
        model = RegistroPagamento
        fields = [
            'cliente', 'data_hora_inicial', 'data_hora_final', 'data_hora_chegada', 'prestador', 'protocolo', 'solicitante',
            'tipo', 'tipo_contato', 'operador', 'modelo', 'cor', 'ano', 'ultima_posicao', 'latlong', 'quantidade_agentes',
            'rastreador', 'id_equipamento', 'isca', 'id_isca', 'ultima_posicao_isca', 'latlong_isca', 'acionamento', 'hora_total', 
            'franquia_hora', 'valor_hora_excedente', 'placas', 'agentes', 'hora_excedente', 'km_inicial', 'km_final', 
            'km_total', 'km_excedente', 'km_franquia', 'sla', 'previsa_chegada', 'valor_km_excedente', 'valor_total_km_excedente', 
            'pedagio', 'descricao', 'imagem1', 'imagem2', 'imagem3', 'imagem4', 'imagem5', 'imagem6', 'imagem7', 'imagem8',
            'imagem9', 'imagem10', 'imagem11', 'imagem12', 'imagem13', 'imagem14', 'imagem15', 'imagem16'
        ]
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}), 
            'data_hora_inicial': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'data_hora_final': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'data_hora_chegada': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'prestador': forms.Select(attrs={'class': 'form-control'}),
            'protocolo': forms.TextInput(attrs={'class': 'form-control'}),
            'solicitante': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'tipo_contato': forms.Select(attrs={'class': 'form-control'}),
            'operador': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'cor': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.TextInput(attrs={'class': 'form-control'}),
            'ultima_posicao': forms.TextInput(attrs={'class': 'form-control'}),
            'ultima_posicao_isca': forms.TextInput(attrs={'class': 'form-control'}),
            'id_isca': forms.TextInput(attrs={'class': 'form-control'}),
            'latlong': forms.TextInput(attrs={'class': 'form-control'}),
            'latlong_isca': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade_agentes': forms.NumberInput(attrs={'class': 'form-control'}),
            'rastreador': forms.Select(attrs={'class': 'form-control'}),
            'id_equipamento': forms.TextInput(attrs={'class': 'form-control'}),
            'isca': forms.Select(attrs={'class': 'form-control'}),
            'acionamento': forms.NumberInput(attrs={'class': 'form-control'}),
            'hora_total': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'franquia_hora': forms.NumberInput(attrs={'class': 'form-control'}),
            'previsa_chegada': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'valor_hora_excedente': forms.NumberInput(attrs={'class': 'form-control'}),
            'placas': forms.TextInput(attrs={'class': 'form-control'}),
            'agentes': forms.NumberInput(attrs={'class': 'form-control'}),
            'hora_excedente': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'km_inicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'km_final': forms.NumberInput(attrs={'class': 'form-control'}),
            'km_total': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'km_excedente': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'km_franquia': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_km_excedente': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_total_km_excedente': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'pedagio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'imagem1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem4': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem5': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem6': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem7': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem8': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem9': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem10': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem11': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem12': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem13': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem14': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem15': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem16': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    import re
from datetime import timedelta
from django import forms

class SeuForm(forms.Form):
    sla = forms.CharField()  # ou outro tipo de campo apropriado para 'sla'

    def clean_sla(self):
        sla_str = self.cleaned_data.get('sla', None)
        
        if sla_str:
            try:
                # Caso o usuário insira apenas números (assumimos que seja em minutos)
                if isinstance(sla_str, str) and sla_str.isdigit():
                    minutes = int(sla_str)
                    hours, minutes = divmod(minutes, 60)
                else:
                    # Usa regex para verificar se está no formato HH:MM
                    match = re.match(r'^(\d{1,2}):(\d{2})$', sla_str)
                    if match:
                        hours, minutes = map(int, match.groups())
                    else:
                        raise ValueError('Formato inválido. Use HH:MM ou apenas minutos.')

                # Certifique-se de que os valores de horas e minutos são válidos
                if hours < 0 or minutes < 0 or minutes >= 60:
                    raise ValueError('Horas ou minutos inválidos.')

                # Converte para timedelta e retorna
                return timedelta(hours=hours, minutes=minutes)

            except ValueError as e:
                raise forms.ValidationError(str(e))

        # Caso o campo esteja vazio ou o valor não seja válido
        raise forms.ValidationError('Campo SLA não pode ser vazio.')

    def save(self, commit=True):
        # Salvar a instância do modelo
        instance = super().save(commit=False)

        # Atribuir o valor de `sla` convertido (timedelta) ao campo `sla` do modelo
        sla_timedelta = self.cleaned_data.get('sla', None)
        if sla_timedelta:
            instance.sla = sla_timedelta

        # Calcula a previsão de chegada se `data_hora_inicial` e `sla` estiverem definidos
        if instance.data_hora_inicial and instance.sla:
            instance.previsa_chegada = instance.data_hora_inicial + instance.sla

        if commit:
            instance.save()
        return instance
    


from django import forms
from .models import prestadores

class PrestadoresForm(forms.ModelForm):
    class Meta:
        model = prestadores
        fields = [
            'Nome', 'cpf_cnpj', 'vencimento_cnh','banco', 'agencia','conta','tipo_de_conta','tipo_prestador', 'endereco', 
            'telefone', 'email', 'disponibilidade', 
            'regiao_atuacao', 'status_prestador','franquia_hora','valorh','valorkm','franquia_km','valor_acionamento', 'cnh', 'foto'
        ]
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF ou CNPJ'}),
            'vencimento_cnh': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'tipo_prestador': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de prestador'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço completo'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@dominio.com'}),
            'banco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dados bancários'}),
            'agencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dados Agencia'}),
            'conta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dados conta'}),
            'tipo_de_conta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tipo_de_conta'}),
            'disponibilidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Disponibilidade'}),
            'regiao_atuacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Região de atuação'}),
            'status_prestador': forms.TextInput(attrs={'class': 'form-control'}),
            'franquia_hora': forms.NumberInput(attrs={'class': 'form-control'}),
            'valorh': forms.NumberInput(attrs={'class': 'form-control'}),
            'valorkm': forms.NumberInput(attrs={'class': 'form-control'}),
            'franquia_km': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_acionamento': forms.NumberInput(attrs={'class': 'form-control', }),
            
            'cnh': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }



from django import forms
from .models import clientes_acionamento

from django import forms
from .models import clientes_acionamento

class ClientesAcionamentoForm(forms.ModelForm):
    class Meta:
        model = clientes_acionamento
        fields = ['nome', 'franquiakm', 'franquiahora', 'valordeacionamento', 'valor_km', 'valor_hora']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome completo do cliente',
                'maxlength': '100',
            }),
            'franquiakm': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe a franquia em KM',
                'min': '0',
                'step': '0.01',
            }),
            'franquiahora': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe a franquia em horas',
                'min': '0',
                'step': '0.1',
            }),
            'valordeacionamento': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe o valor do acionamento',
                'min': '0',
                'step': '0.01',
            }),
            'valor_km': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe o valor por KM',
                'min': '0',
                'step': '0.01',
            }),
            'valor_hora': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe o valor por Hora',
                'min': '0',
                'step': '0.01',
            }),
        }


    def clean_nome(self):
        """Validação personalizada para o campo nome."""
        nome = self.cleaned_data.get('nome', '').strip()
        if len(nome) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return nome

    def clean_franquiakm(self):
        """Validação personalizada para o campo franquia KM."""
        franquiakm = self.cleaned_data.get('franquiakm')
        if franquiakm is not None and franquiakm < 0:
            raise forms.ValidationError("A franquia em KM não pode ser negativa.")
        return franquiakm

    def clean_franquiahora(self):
        """Validação personalizada para o campo franquia hora."""
        franquiahora = self.cleaned_data.get('franquiahora')
        if franquiahora is not None and franquiahora < 0:
            raise forms.ValidationError("A franquia em horas não pode ser negativa.")
        return franquiahora

    def clean_valordeacionamento(self):
        """Validação personalizada para o campo valor de acionamento."""
        valordeacionamento = self.cleaned_data.get('valordeacionamento')
        if valordeacionamento is not None and valordeacionamento < 0:
            raise forms.ValidationError("O valor de acionamento não pode ser negativo.")
        return valordeacionamento

