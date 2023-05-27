from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.pessoas.models import Pessoa

@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'home.html', data)



