from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from .models import Pessoa
from django.contrib.auth.mixins import LoginRequiredMixin

class PessoaEdit(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = Pessoa
    fields = ['nome','crm','data_cadastro','data_nascimento','sexo','grupo_sanguineo','telefone','nome_mae','nome_pai',
              'cpf','rg','especialidade','setor','convenio']
    template_name = 'core/form_pessoa.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Pessoa, pessoa=self.request.user)
        return self.object

class PessoaCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = Pessoa
    fields = ['nome', 'crm', 'data_cadastro', 'data_nascimento', 'sexo', 'grupo_sanguineo', 'telefone', 'nome_mae', 'nome_pai',
              'cpf', 'rg', 'especialidade','setor','convenio']
    template_name = 'core/form_pessoa.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Antes do super não foi criado o objeto nem salvo no banco
        form.instance.pessoa = self.request.user

        url = super().form_valid(form)

        return url






