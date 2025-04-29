from django.shortcuts import render, redirect
from .forms import InscricaoForm
from .models import Inscricao
from django.contrib.admin.views.decorators import staff_member_required

def formulario_inscricao(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inscricao_sucesso')
    else:
        form = InscricaoForm()
    return render(request, 'formulario.html', {'form': form})

def inscricao_sucesso(request):
    return render(request, 'sucesso.html')

@staff_member_required
def ranking_view(request):
    inscritos = Inscricao.objects.all().order_by('-pontuacao')
    return render(request, 'ranking.html', {'inscritos': inscritos})