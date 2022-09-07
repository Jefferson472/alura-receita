from django.contrib import messages
from django.shortcuts import redirect, render

from apps.receitas.models import Receita
from apps.usuario.forms import RegisterForm


def cadastro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta cadastrada com sucesso!" )

            return redirect('login')
        else:
            messages.error(request, "Cadastro não realizado. Informações inválidas.")
    else:
        form = RegisterForm()
    return render(request, 'usuario/cadastro.html', {'form': form})

def dashboard(request):
    if request.user.is_authenticated:
        receitas = Receita.objects.order_by('-create_at').filter(user=request.user)
        return render(request, 'usuario/dashboard.html', {'receitas': receitas})
    else:
        return redirect('receitas')
