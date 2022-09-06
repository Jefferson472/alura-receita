from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

from apps.receitas.models import Receita


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        senha2 = request.POST.get('password2')
        if not nome.strip() or not email.strip():
            messages.error(
                request, 'O campo nome e email não pode ficar em branco'
                )
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não conferem')
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(
            username=nome, email=email, password=senha)
        user.save()
        messages.add_message(
            request, messages.SUCCESS, 'Cadastro realizado com sucesso!'
            )
        return redirect('login')
    else:
        return render(request, 'usuario/cadastro.html')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-create_at').filter(user=id)
        dados = {
            'receitas': receitas
        }
        return render(request, 'usuario/dashboard.html', dados)
    else:
        return redirect('receitas')
