from django import forms
from .models import Numero

class NumeroForm(forms.ModelForm):
    class Meta:
        model = Numero
        fields = ['numero']


class NumeroSomadoForm(forms.Form):
    numero_compara = forms.IntegerField()