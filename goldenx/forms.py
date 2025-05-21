from django import forms
from .models import Cadastro, Pesquisa

class cadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = [
            'empresa', 'data_entrada', 'pesquisa', 'estado1', 'estado2', 'estado3',
            'estado4', 'estado5', 'status', 'hora_devolutiva', 'sla', 'periodo', 'estados'
        ]
        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'data_entrada': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'pesquisa': forms.TextInput(attrs={'class': 'form-control'}),
            'estado1': forms.TextInput(attrs={'class': 'form-control'}),
            'estado2': forms.TextInput(attrs={'class': 'form-control'}),
            'estado3': forms.TextInput(attrs={'class': 'form-control'}),
            'estado4': forms.TextInput(attrs={'class': 'form-control'}),
            'estado5': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_devolutiva': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'sla': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'periodo': forms.TextInput(attrs={'class': 'form-control'}),
            'estados': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Garante formatação correta ao editar um registro
        for field in ['data_entrada', 'hora_devolutiva']:
            if self.initial.get(field):
                self.initial[field] = self.initial[field].strftime('%Y-%m-%dT%H:%M')

class pesquisaForm(forms.ModelForm):
    class Meta:
        model = Pesquisa
        fields = [
            'empresa','data','modo','plano','perfil','placa','resultado','periodo'
        ]
        widgets ={
            'empresa' : forms.TextInput(attrs={'class':'form-control'}),
            'data' : forms.TextInput(attrs={'class':'form-control'}),
            'modo' : forms.Select(attrs={'class':'form-control'}),
            'plano' : forms.Select(attrs={'class':'form-control'}),
            'perfil' : forms.TextInput(attrs={'class':'form-control'}),
            'placa' : forms.TextInput(attrs={'class':'form-control'}),
            'resultado' : forms.Select(attrs={'class':'form-control'}),
            'periodo' : forms.Select(attrs={'class':'form-control'}), 
        }
