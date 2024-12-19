from django import forms
from .models import Mensagem
from django.core.exceptions import ValidationError

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['nome', 'email', 'telefone', 'cidade', 'mensagem']
        
def clean_ciade(self):
    data = self.cleaned_data["cidade"]
    cidades_validas = ["SPP", "São Pedro", "Bom Jesus"]
    
    if not data in cidades_validas:
        raise ValidationError("Não aceitamos a sua cidade.")
    
    return data