from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Especialidade
from django.contrib.auth.mixins import LoginRequiredMixin

class EspecialidadeList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    model = Especialidade
    template_name = 'especialidades/listar_especialidades.html'
    #paginate_by= 50

    def get_queryset(self):
        especialidades = Especialidade.objects.all()
        return Especialidade.objects.all().order_by('pk')

