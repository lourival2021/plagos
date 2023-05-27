from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa

# Create your views here.
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['cnpj']

    def form_valid(self,form):
        obj = form.save()
        pessoa = self.request.user.pessoa
        pessoa.empresa = obj
        pessoa.save()
        return HttpResponse('ok')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['cnpj']




