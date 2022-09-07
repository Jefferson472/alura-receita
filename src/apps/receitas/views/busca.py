from django.shortcuts import render

from apps.receitas.models import Receita


def buscar(request):
    receitas = Receita.objects.order_by('-create_at').filter(status=True)

    if 'buscar' in request.GET:
        termo = request.GET['buscar']
        if buscar:
            receitas = receitas.filter(nome_receita__icontains=termo)

    return render(request, 'receitas/buscar.html', {'receitas': receitas})
