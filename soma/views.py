from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def adiciona_numero():
    pass

def deleta_lista():
    pass

def lista_numeros(request):
    numeros = Numero.objects.all()
    number_2_form = NumeroSomadoForm()
    return render(request,"numero.html", {'numeros': numeros, 'number_2_form': number_2_form})

def compara_numero(request):
    print("to aqui")
    if request.method == "GET":
            numero = int(request.GET.get('numero_compara'))
            numeros = Numero.objects.all()
            lista_numeros = []
            for i in numeros:
                lista_numeros.append(i.numero)
            print(lista_numeros)
            cont = 0
            lista_soma = []
            for i in range(len(lista_numeros)):
                for j in range(len(lista_numeros)):
                    if i != j:
                        print(type(lista_numeros[i]))
                        if lista_numeros[i] + lista_numeros[j] == numero:
                            print('aqui nao')
                            cont +=1
                            if lista_numeros[i] and lista_numeros[j] in lista_soma:
                                pass
                            else:
                                lista_soma.append(lista_numeros[i])
                                lista_soma.append(lista_numeros[j])
    return render(request,"compara_numero.html", {'lista_soma':lista_soma, 'cont': cont})
