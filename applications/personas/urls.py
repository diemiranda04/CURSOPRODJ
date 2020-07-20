from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        'listar-todo-empleados/', 
        views.ListaAllEmpleados.as_view(),
        name= 'Empleados_all'
    ),
    path(
        'listar-by-area/<shorname>/',
         views.ListByAreaEmpleados.as_view(),
         name ='empleados_area'
    ),
    path(
        'listar-empleados-admin/',
         views.ListaEmpleadosAdmin.as_view(),
         name ='empleados_admin'
    ),
    path('listar-by-trabajo/<job>/', views.ListByTrabajoEmpleados.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('listar-habilidades/', views.ListaHabilidadesEmpleados.as_view()),
    path(
        'detalles-empleados/<pk>',
        views.EmpleadoDetailView.as_view(),
        name='empleados_details'
    ),        
    path(
        'add-empleados/',
        views.EmpleadoCreateView.as_view(),
        name = 'empleados_add'
    ),
    path(
        '',
        views.InicioView.as_view(),
        name = 'Inicio'        
    ),
    path(
        'success',
        views.SuccessView.as_view(),
        name='ok'
    ),
    path(
        'update-empleado/<pk>',
        views.EmpleadoUpdateView.as_view(),
        name = "modificar_empleado"       
    ),
    path(
        'delete-empleado/<pk>',
        views.EmpleadoDeleteView.as_view(),
        name = 'eliminar_empleado'        
    ),

]