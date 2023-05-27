from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Agenda
from django.contrib.auth.mixins import LoginRequiredMixin

class AgendaList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    model = Agenda
    template_name = 'agendas/listar_agendas.html'
    #paginate_by= 50

    def get_queryset(self):

        self.object_list = Agenda.objects.filter(pessoa=self.request.user)
        return self.object_list

class AgendaCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = Agenda
    fields = ['profissional', 'dia', 'horario']
    template_name = 'core/form_agenda.html'
    success_url = reverse_lazy('listar_agendas')

    def form_valid(self, form):
        # Antes do super não foi criado o objeto nem salvo no banco
        form.instance.pessoa = self.request.user

        url = super().form_valid(form)

        return url

class AgendaUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = Agenda
    fields = ['profissional', 'dia', 'horario']
    template_name = 'core/form_agenda.html'
    success_url = reverse_lazy('listar_agendas')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Agenda, pk=self.kwargs['pk'], pessoa=self.request.user)
        return self.object

class AgendaDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login'
    model = Agenda
    template_name = 'core/excluir.html'
    success_url = reverse_lazy('listar_agendas')