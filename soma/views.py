from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.



def adiciona_numero(request):
    if request.method == 'POST':
        nform =  NumeroForm(request.POST)
        if nform.is_valid():
            nform.save()
            return redirect('/soma')
    else:
        nform = NumeroForm()
    return render(request, 'numero.html', {'nform': nform})

def apaga_lista(request):
    numb = Numero.objects.all()
    if request.method == "GET":
        numb.delete()
        return redirect('/soma/')
    return(request,'numero.html', {})


def lista_numeros(request):
    nform = NumeroForm()
    numeros = Numero.objects.all()
    number_2_form = NumeroSomadoForm()
    return render(request,"numero.html", {'numeros': numeros, 'number_2_form': number_2_form, 'nform':nform})

def compara_numero(request):
    if request.method == "GET":
            numero = int(request.GET.get('numero_compara'))
            numeros = Numero.objects.all()
            lista_numeros = []
            for i in numeros:
                lista_numeros.append(i.numero)
            cont = 0
            lista_soma = []
            for i in range(len(lista_numeros)):
                for j in range(len(lista_numeros)):
                    if i != j:
                        if lista_numeros[i] + lista_numeros[j] == numero:
                            cont +=1
                            if lista_numeros[i] and lista_numeros[j] in lista_soma:
                                pass
                            else:
                                lista_soma.append(lista_numeros[i])
                                lista_soma.append(lista_numeros[j])
    return render(request,"compara_numero.html", {'lista_soma':lista_soma, 'cont': cont})
