from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_numeros, name='lista_numeros'),
    path('compara/', views.compara_numero, name='compara_numero'),
    path('apaga/', views.apaga_lista, name='apaga_lista'),
    path('add/', views.adiciona_numero, name='add_numero'),

]