from django.shortcuts import redirect, render, get_object_or_404
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
            messages.error(request, 'O campo nome e email não pode ficar em branco')
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
        messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso!')
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
            print(user, nome, senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
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


def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST.get('nome_receita')
        ingredientes = request.POST.get('ingredientes')
        modo_preparo = request.POST.get('modo_preparo')
        tempo_preparo = request.POST.get('tempo_preparo')
        rendimento = request.POST.get('rendimento')
        categoria = request.POST.get('categoria')
        foto_receita = request.FILES.get('foto_receita')
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(
            pessoa=user,
            nome_receita=nome_receita,
            ingredientes=ingredientes,
            mode_preparo=modo_preparo,
            tempo_preparo=tempo_preparo,
            rendimento=rendimento,
            categoria=categoria,
            foto_receita=foto_receita
            )
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuario/cria_receita.html')
