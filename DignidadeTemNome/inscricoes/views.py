from django.shortcuts import render, redirect
from .forms import InscricaoForm

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
