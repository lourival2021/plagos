from django.contrib import admin
from django.urls import path
from .views import EspecialidadeList

urlpatterns = [
    path('listar/especialidades/', EspecialidadeList.as_view(), name='listar_especialidades'),
]
