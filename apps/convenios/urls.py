from django.contrib import admin
from django.urls import path
from .views import ConvenioList, ConvenioCreate, ConvenioUpdate, ConvenioDelete

urlpatterns = [
    path('listar/convenios/', ConvenioList.as_view(), name='listar_convenios'),
    path('cadastrar/convenio/', ConvenioCreate.as_view(), name='cadastrar_convenio'),
    path('editar/convenio/<int:pk>/', ConvenioUpdate.as_view(), name='editar_convenio'),
    path('excluir/convenio/<int:pk>/', ConvenioDelete.as_view(), name='excluir_convenio'),
]