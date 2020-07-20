from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
     ListView,
     DetailView,
     CreateView,
     TemplateView,
     UpdateView,
     DeleteView
)

from .models import Empleado

from .forms import EmpleadoForm

class InicioView(TemplateView):
     """Vista que cargara la pagina de inicio"""
     template_name = 'inicio.html'


class ListaAllEmpleados(ListView):
     template_name= 'persona/list_all.html'
     #paginacion
     paginate_by =4
     #fin paginacion
     context_object_name = 'empleados'
     
     def get_queryset(self):
          palabra_clave= self.request.GET.get('kword','')
          lista = Empleado.objects.filter(
               last_name__icontains = palabra_clave
          )
          return lista


class ListaEmpleadosAdmin(ListView):
     template_name= 'persona/lista_empleados_admin.html'     
     paginate_by =10     
     context_object_name = 'empleados'
     model = Empleado


class ListByAreaEmpleados(ListView):
     """ lista de empleados en un  area"""
     template_name= 'persona/list_by_area.html'        
     context_object_name = 'empleados'

     def get_queryset(self):
          area = self.kwargs['shorname']
          lista = Empleado.objects.filter(
               departamento__shor_name = area
          )
          return lista


class ListByTrabajoEmpleados(ListView):
     """ lista empleados por trabajo"""
     template_name='persona/list_by_trabajo.html'

     def get_queryset(self):
          trabajo = self.kwargs['job']
          lista = Empleado.objects.filter(
               job = trabajo
          )
          return lista


class ListEmpleadosByKword(ListView):
     """ lista empleados por palabra clave """
     template_name = 'persona/by_kword.html'
     context_object_name = 'empleados'

     def get_queryset(self):
          palabra_clave= self.request.GET.get('kword','')
          lista = Empleado.objects.filter(
               first_name = palabra_clave
          )
          return lista


class ListaHabilidadesEmpleados(ListView):
     template_name = "persona/habilidades.html"
     context_object_name = 'habilidades'    

     def get_queryset(self):          
          empleado = Empleado.objects.get(first_name='Juan')                   
          return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
     
     model = Empleado
     template_name = "persona/detail_persona.html"

     def get_context_data(self, **kwargs):
         context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
         context['titulo']='Empleado del mes'
         return context
     

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class= EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
         empleado = form.save()
         empleado.full_name = empleado.first_name + ' ' + empleado.last_name
         empleado.save()
         return super(EmpleadoCreateView,self).form_valid(form)
     

class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
         'first_name',
         'last_name',
         'avatar',
         'job',
         'departamento',
         'habilidades',
    ]    
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
          self.object = self.get_object()          
          print(request.POST['last_name'])
          return super().post(request, *args, **kwargs)

    def form_valid(self, form):
                  
          return super(EmpleadoUpdateView,self).form_valid(form)



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')

# Lista todos los empleados de la empresa
#Lista a todos los empleados que pertenecen a un area de la empresa
#Lista empleados por trabajo
#Lista a todos los empleados por palabra clave
# Lista habilidades de un empleado
