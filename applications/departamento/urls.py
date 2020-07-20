from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamentos_app"

urlpatterns = [
    path(
        'listar-departamentos/', 
        views.DepartamentosListView.as_view(),
        name = 'Departamentos_all'),
    path(
        'new-departamento/',
         views.NewDepartamentoView.as_view(),
          name = 'Nuevo_Departamwento'),
]