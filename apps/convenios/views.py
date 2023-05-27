from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Convenio
from django.contrib.auth.mixins import LoginRequiredMixin

class ConvenioList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    model = Convenio
    template_name = 'convenios/listar_convenios.html'
    #paginate_by= 50

    def get_queryset(self):

        self.object_list = Convenio.objects.filter(pessoa=self.request.user)
        return self.object_list

class ConvenioCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = Convenio
    fields = ['cd_convenio','descricao']
    template_name = 'core/form_convenio.html'
    success_url = reverse_lazy('listar_convenios')

    def form_valid(self, form):
        # Antes do super não foi criado o objeto nem salvo no banco
        form.instance.pessoa = self.request.user

        url = super().form_valid(form)

        return url

class ConvenioUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = Convenio
    fields = ['cd_convenio','descricao']
    template_name = 'core/form_convenio.html'
    success_url = reverse_lazy('listar_convenios')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Convenio, pk=self.kwargs['pk'], pessoa=self.request.user)
        return self.object

class ConvenioDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login'
    model = Convenio
    template_name = 'core/excluir.html'
    success_url = reverse_lazy('listar_convenios')