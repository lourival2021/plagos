from django.contrib import admin
from django.urls import path
from .views import AgendaList, AgendaCreate, AgendaUpdate, AgendaDelete

urlpatterns = [
    path('listar/agendas/', AgendaList.as_view(), name='listar_agendas'),
    path('cadastrar/agenda/', AgendaCreate.as_view(), name='cadastrar_agenda'),
    path('editar/agenda/<int:pk>/', AgendaUpdate.as_view(), name='editar_agenda'),
    path('excluir/agenda/<int:pk>/', AgendaDelete.as_view(), name='excluir_agenda'),
]