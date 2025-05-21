from django import forms
from .models import ticketmodel

class ticketForm(forms.ModelForm):
    class Meta:
        model = ticketmodel
        fields = ['setor', 'erro', 'correcao', 'devolutiva']  # Incluindo devolutiva
        widgets = {
            'setor': forms.Select(attrs={'class': 'form-control'}),
            'erro': forms.Textarea(attrs={'class': 'form-control'}),
            'correcao': forms.Textarea(attrs={'class': 'form-control'}),
            
        }