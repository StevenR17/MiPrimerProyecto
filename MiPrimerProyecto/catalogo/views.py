from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pais, Departamento, Municipio
from django.db.models import Q  # Para realizar búsquedas con Q objects
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#VISTAS PARA PAIS

#VER
class PaisListView( ListView):
    model = Pais
    #paginate_by = 10  # Agrega paginación
    template_name = 'catalogo/pais_list.html'
    #Definimos como acceder a los datos guardados en 
    #esta vista dentro de la plantilla
    context_object_name = 'paises'

    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')  # Obtén el término de búsqueda desde la URL
        if query:
            # Filtra los municipios que contienen el término de búsqueda en su nombre o en el nombre del país
            queryset = queryset.filter(
                Q(nombre__icontains=query)
            )
        return queryset
    
#AGREGAR
class PaisCreateView(PermissionRequiredMixin, CreateView):
    model = Pais
    fields = ['nombre']
    template_name = 'catalogo/pais_add.html'
    #Redirige a la lista de países después de agregar
    success_url = reverse_lazy('pais-list')
    #Necesita permisos especificos para acceder a esta vista
    permission_required = 'catalogo.pais_add'

#ACTUALIZAR
class PaisUpdateView(PermissionRequiredMixin, UpdateView):
    model = Pais
    fields = ['nombre']
    template_name = 'catalogo/pais_update.html'
    success_url = reverse_lazy('pais-list')
    permission_required = 'catalogo.pais_update'

#BORRAR
class PaisDeleteView(PermissionRequiredMixin, DeleteView):
    model = Pais
    success_url = reverse_lazy('pais-list')
    template_name = 'catalogo/pais_delete.html'
    permission_required = 'catalogo.pais_delete'


#VISTA HOME
#@login_required
#Nos asegura que solo usuarios que han iniciado sesion
#pueden ver esta pagina (vista)
@login_required
def home(request):
    return render(request, 'catalogo/home.html')


#VISTAS PARA DEPARTAMENTO
#VER
class DepartamentoListView(ListView):
    model = Departamento
    paginate_by = 10  # Agrega paginación
    template_name = 'catalogo/departamento_list.html'
    #Definimos como acceder a los datos guardados en 
    #esta vista dentro de la plantilla
    context_object_name = 'departamentos'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')  # Obtén el término de búsqueda desde la URL
        if query:
            # Filtra los municipios que contienen el término de búsqueda en su nombre o en el nombre del país
            queryset = queryset.filter(
                Q(nombre__icontains=query) | 
                Q(pais__nombre__icontains=query)
            )
        return queryset

    
#AGREGAR
class DepartamentoCreateView(PermissionRequiredMixin, CreateView):
    model = Departamento
    fields = ['nombre']
    template_name = 'catalogo/departamento_add.html'
    #Redirige a la lista de países después de agregar
    success_url = reverse_lazy('departamento-list')
    #Necesita permisos especificos para acceder a esta vista
    permission_required = 'catalogo.departamento_add'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paises'] = Pais.objects.all()  # Obtener todos los países
        return context

    def form_valid(self, form):
        # Asignar el país basado en el ID del país seleccionado
        pais_id = self.request.POST.get('pais')
        form.instance.pais_id = pais_id
        return super().form_valid(form)


#ACTUALIZAR
class DepartamentoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Departamento
    fields = ['nombre']
    template_name = 'catalogo/departamento_update.html'
    success_url = reverse_lazy('departamento-list')
    permission_required = 'catalogo.departamento_update'

#BORRAR
class DepartamentoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Departamento
    success_url = reverse_lazy('departamento-list')
    template_name = 'catalogo/departamento_delete.html'
    permission_required = 'catalogo.departamento_delete'



#VISTAS PARA MUNICIPIO
#VER
class MunicipioListView(ListView):
    model = Municipio
    paginate_by = 10  # Agrega paginación
    template_name = 'catalogo/municipio_list.html'
    #Definimos como acceder a los datos guardados en 
    #esta vista dentro de la plantilla
    context_object_name = 'municipios'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')  # Obtén el término de búsqueda desde la URL
        if query:
            # Filtra los municipios que contienen el término de búsqueda en su nombre o en el nombre del departamento o país
            queryset = queryset.filter(
                Q(nombre__icontains=query) | 
                Q(departamento__nombre__icontains=query) | 
                Q(departamento__pais__nombre__icontains=query)
            )
        return queryset
    
#AGREGAR
class MunicipioCreateView(PermissionRequiredMixin, CreateView):
    model = Municipio
    #define que campos de nuestro modelo se mostraran
    fields = ['nombre']
    template_name = 'catalogo/municipio_add.html'
    #Redirige a la lista de municipios después de agregar
    success_url = reverse_lazy('municipio-list')
    #Necesita permisos especificos para acceder a esta vista
    permission_required = 'catalogo.municipio_add'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departamentos'] = Departamento.objects.all()  # Obtener todos los países
        return context

    def form_valid(self, form):
        # Asignar el país basado en el ID del país seleccionado
        departamento_id = self.request.POST.get('departamento')
        form.instance.departamento_id = departamento_id
        return super().form_valid(form)


#ACTUALIZAR
class MunicipioUpdateView(PermissionRequiredMixin, UpdateView):
    model = Municipio
    fields = ['nombre']
    template_name = 'catalogo/municipio_update.html'
    success_url = reverse_lazy('municipio-list')
    permission_required = 'catalogo.municipio_update'

#BORRAR
class MunicipioDeleteView(PermissionRequiredMixin, DeleteView):
    model = Municipio
    success_url = reverse_lazy('municipio-list')
    template_name = 'catalogo/municipio_delete.html'
    permission_required = 'catalogo.municipio_delete'


