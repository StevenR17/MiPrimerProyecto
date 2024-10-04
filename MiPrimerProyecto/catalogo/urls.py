from django.urls import path
from . import views 

from .views import (home,
        #Vistas Pais
        PaisListView, PaisCreateView, PaisUpdateView,PaisDeleteView,
        DepartamentoListView, DepartamentoCreateView,
        DepartamentoUpdateView, DepartamentoDeleteView,
        MunicipioCreateView, MunicipioListView, MunicipioUpdateView,
        MunicipioDeleteView,
        )

urlpatterns = [

    path('home/', home, name='home'),

    #PAIS
    path('pais/', PaisListView.as_view(), name='pais-list'),
    path('pais/add/', PaisCreateView.as_view(), name='pais-add'),
    path('pais/<int:pk>/update/', PaisUpdateView.as_view(), name='pais-update'),
    path('pais/<int:pk>/delete/', PaisDeleteView.as_view(), name='pais-delete'),

    #DEPARTAMENTO
    path('departamento/', DepartamentoListView.as_view(), name='departamento-list'),
    path('departamento/add/', DepartamentoCreateView.as_view(), name='departamento-add'),
    path('departamento/<int:pk>/update/', DepartamentoUpdateView.as_view(), name='departamento-update'),
    path('departamento/<int:pk>/delete/', DepartamentoDeleteView.as_view(), name='departamento-delete'),

    #MUNICIPIO
    path('municipio/', MunicipioListView.as_view(), name='municipio-list'),
    path('municipio/add/', MunicipioCreateView.as_view(), name='municipio-add'),
    path('municipio/<int:pk>/update/', MunicipioUpdateView.as_view(), name='municipio-update'),
    path('municipio/<int:pk>/delete/', MunicipioDeleteView.as_view(), name='municipio-delete'),

]