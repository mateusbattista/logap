from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_numeros, name='lista_numeros'),
    path('compara/', views.compara_numero, name='compara_numero'),
]