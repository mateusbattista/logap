from django import forms
from .models import Grafico

class GraficoForm(forms.ModelForm):
    class Meta:
        model = Grafico
        fields = ['nome']


class SelectGraficoForm(forms.Form):
    grafico = forms.ModelChoiceField(queryset=Grafico.objects.all(), label='Selecione o Gráfico para plotar')