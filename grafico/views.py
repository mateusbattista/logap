from django.shortcuts import render
import logging
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import GraficoForm, SelectGraficoForm
from .models import *
import random


# Create your views here.

def index(request):
	return render(request, 'index.html',{})

def upload_csv(request):
	form = GraficoForm()
	graphform = SelectGraficoForm()
	graficos = Grafico.objects.all()

	def convert_list_string_to_int(lista):
		for pos in range(0, len(lista)):
			lista[pos].replace(",",".")
			lista[pos] = float(lista[pos])
		return lista

	def replace_comma_to_dot(lista):
		lista_2 = []
		for i in range(len(lista)):
			word = ''
			new_list = list(lista[i])
			for j in range(len(new_list)):
				if new_list[j] == ',':
					new_list[j] = '.'
			for w in range(len(new_list)):
				word += str(new_list[w])
			lista_2.append(word)
			lista[i] = lista_2 [i]
		return lista


	if request.method == 'POST':
		try:
			csv_file = request.FILES["csv_file"]
			if not csv_file.name.endswith('.csv'):
				messages.error(request,'O Arquivo não é um arquivo do tipo csv')
				return HttpResponseRedirect(reverse("upload_csv"))
			#if file is too large, return
			if csv_file.multiple_chunks():
				messages.error(request,"Arquivo não pode ultrapassar (%.2f MB)." % (csv_file.size/(1000*1000),))
				return HttpResponseRedirect(reverse("upload_csv"))

			file_data = csv_file.read().decode("utf-8")	

			lines = file_data.split("\n")
			coord_x = []
			coord_y = []
			for line in lines:						
				fields = line.split(";")
				coord_x.append(fields[0])
				coord_y.append(fields[1])
			print(len(coord_x))
			print(len(coord_y))
			coord_x.pop(0)
			coord_y.pop(0)
			try:
				form = GraficoForm(request.POST)
				if form.is_valid():
					form.save()
					g = Grafico.objects.get(nome=request.POST.get('nome'))
					replace_comma_to_dot(coord_x)
					replace_comma_to_dot(coord_y)
					coord_nova_x = convert_list_string_to_int(coord_x)
					coord_nova_y = convert_list_string_to_int(coord_y)
					g.coo_x = coord_nova_x
					g.coo_y = coord_nova_y
					g.save()					
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())												
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))					
		except Exception as e:
			logging.getLogger("error_logger").error("Não é possível fazer o upload do arquivo. "+repr(e))
			messages.error(request,"Não é possível fazer o upload do arquivo. "+repr(e))
	else:
		return render(request, "grafico_index.html",  {'form': form, 'graficos': graficos, 'graphform':graphform})

	return HttpResponseRedirect(reverse("upload_csv"))


def build_graph(request):
	graphform = SelectGraficoForm()
	form = GraficoForm()
	dict_coo = []
	if request.method == "GET":
		pk = request.GET.get('grafico')
		grafico = Grafico.objects.get(pk=pk)
		coord_x = list(grafico.coo_x.split(", "))
		coord_x[-1] = coord_x[-1].replace(']','')
		coord_y = list(grafico.coo_y.split(", "))
		coord_y[-1] = coord_y[-1].replace(']','')
		if len(coord_x) == len(coord_y):
			for i in range(len(coord_x)):
				dict_coo.append(
					{"x":coord_x[i],"y": coord_y[i]}
				)
		print(dict_coo)	
		return render(request, "construir_grafico.html",  {'form': form,'grafico': grafico, 'graphform':graphform, 'dict_coo':dict_coo})
