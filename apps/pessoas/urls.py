from django.contrib import admin
from django.urls import path
from .views import PessoaEdit, PessoaCreate

urlpatterns = [
    path('editar/pessoa/', PessoaEdit.as_view(), name='editar_pessoa'),
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='cadastrar_pessoa'),
]

