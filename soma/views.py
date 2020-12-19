from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.


def lista_numeros(request):
    numeros = Numero.objects.all()
    number_2_form = NumeroSomadoForm()
    return render(request,"numero.html", {'numeros': numeros, 'number_2_form': number_2_form})

def compara_numero(request):
    print("to aqui")
    if request.method == "GET":
        numero = request.GET.get('numero_compara')
        numeros = Numero.objects.all()
        lista_numeros = []
        for i in numeros:
            lista_numeros.append(i.numero)
        print(lista_numeros)
    return render(request,"numero.html", {})
