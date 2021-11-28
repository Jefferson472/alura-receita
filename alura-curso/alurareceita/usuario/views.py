from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from receitas.models import Receita
from django.contrib import messages

# Create your views here.


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


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if User.objects.filter(email=email).exists():
            nome = User.objects.get(email=email).username
            user = auth.authenticate(username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
        else:
            print('Usuário não cadastrado')
            messages.error(request, 'Usuário não cadastrado')
            return redirect('login')
    return render(request, 'usuario/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        dados = {
            'receitas': receitas
        }
        return render(request, 'usuario/dashboard.html', dados)
    else:
        return redirect('index')
