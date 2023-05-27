from django.contrib import admin
from django.urls import path
from .views import SetorList, SetorCreate, SetorUpdate, SetorDelete

urlpatterns = [
    path('listar/setores/', SetorList.as_view(), name='listar_setores'),
    path('cadastrar/setor/', SetorCreate.as_view(), name='cadastrar_setor'),
    path('editar/setor/<int:pk>/', SetorUpdate.as_view(), name='editar_setor'),
    path('excluir/setor/<int:pk>/', SetorDelete.as_view(), name='excluir_setor'),
]
