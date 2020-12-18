from django.shortcuts import render
import logging
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import GraficoForm, SelectGraficoForm
from .models import *
import random


# Create your views here.

def upload_csv(request):
	form = GraficoForm()
	graphform = SelectGraficoForm()
	graficos = Grafico.objects.all()

	def convert_list_string_to_int(lista):
		for pos in range(0, len(lista)):
			lista[pos].replace(",",".")
			lista[pos] = float(lista[pos])
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
			coord_x.pop(0)
			coord_y.pop(0)
			try:
				form = GraficoForm(request.POST)
				if form.is_valid():
					form.save()
					g = Grafico.objects.get(nome=request.POST.get('nome'))
					coord_nova_x = convert_list_string_to_int(coord_x)
					coord_nova_y = convert_list_string_to_int(coord_y)
					g.coo_x = coord_nova_x
					g.coo_y = coord_nova_y
					print(coord_nova_x)
					g.save()					
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())												
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))					
		except Exception as e:
			logging.getLogger("error_logger").error("Não é possível fazer o upload do arquivo. "+repr(e))
			messages.error(request,"Não é possível fazer o upload do arquivo. "+repr(e))
	else:
		return render(request, "index.html",  {'form': form, 'graficos': graficos, 'graphform':graphform})

	return HttpResponseRedirect(reverse("upload_csv"))


def build_graph(request):
	graphform = SelectGraficoForm()
	print("pelomenos eu")
	if request.method == "GET":
		print("aqui vem")
		pk = request.GET.get('grafico')
		grafico = Grafico.objects.get(pk=pk)
		print(grafico)
		"""
		scatterchart page
		"""
		nb_element = 50
		xdata = [i + random.randint(1, 10) for i in range(nb_element)]
		print(xdata)
		ydata1 = [i * random.randint(1, 10) for i in range(nb_element)]

		kwargs1 = {'shape': 'circle'}

		extra_serie1 = {"tooltip": {"y_start": "", "y_end": " balls"}}

		chartdata = {
			'x': xdata,
			'name1': 'series 1', 'y1': ydata1, 'kwargs1': kwargs1, 'extra1': extra_serie1,
		}
		charttype = "scatterChart"
		data = {
			'charttype': charttype,
			'chartdata': chartdata,
		}
		#return render_to_response('scatterchart.html', data)
		return render(request, "construir_grafico.html",  {'grafico': grafico, 'graphform':graphform})
