from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        senha2 = request.POST.get('password2')
        if not nome.strip() or not email.strip():
            print('O campo nome e email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não conferem')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('E-mail já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(
            username=nome, email=email, password=senha)
        user.save()
        return redirect('login.html')
    else:
        return render(request, 'usuario/cadastro.html')


def login(request):
    return render(request, 'usuario/login.html')


def logout(request):
    pass


def dashboard(request):
    pass
