from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Setor
from django.contrib.auth.mixins import LoginRequiredMixin

class SetorList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    model = Setor
    template_name = 'setores/listar_setores.html'
    #paginate_by= 50

    def get_queryset(self):

        self.object_list = Setor.objects.filter(pessoa=self.request.user)
        return self.object_list

class SetorCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = Setor
    fields = ['descricao']
    template_name = 'core/form_setor.html'
    success_url = reverse_lazy('listar_setores')

    def form_valid(self, form):
        # Antes do super não foi criado o objeto nem salvo no banco
        form.instance.pessoa = self.request.user

        url = super().form_valid(form)

        return url

class SetorUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = Setor
    fields = ['descricao']
    template_name = 'core/form_setor.html'
    success_url = reverse_lazy('listar_setores')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Setor, pk=self.kwargs['pk'], pessoa=self.request.user)
        return self.object

class SetorDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login'
    model = Setor
    template_name = 'core/excluir.html'
    success_url = reverse_lazy('listar_setores')


