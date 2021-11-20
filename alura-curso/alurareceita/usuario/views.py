from django.shortcuts import render

# Create your views here.


def cadastro(request):
    return render(request, 'usuario/cadastro.html')


def login(request):
    return render(request, 'usuario/login.html')


def logout(request):
    pass


def dashboard(request):
    pass
