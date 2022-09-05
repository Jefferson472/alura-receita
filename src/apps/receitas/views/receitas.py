from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.generic.edit import CreateView

from apps.receitas.models import Receita


class ReceitaListView(generic.ListView):
    model = Receita
    queryset = Receita.objects.order_by('-create_at').filter(status=True)[:6]


class ReceitaDetailView(generic.DetailView):
    model = Receita


class ReceitaCreateView(CreateView):
    model = Receita
    fields = [
        'nome_receita', 'ingredientes', 'modo_preparo',
        'tempo_preparo', 'rendimento', 'categoria', 'foto_receita'
    ]
    success_url = 'dashboard'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')


def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {
        'receita': receita
    }
    return render(request, 'receitas/edita_receita.html', receita_a_editar)


def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        receita = Receita.objects.get(pk=receita_id)
        receita.nome_receita = request.POST.get('nome_receita')
        receita.ingredientes = request.POST.get('ingredientes')
        receita.mode_preparo = request.POST.get('modo_preparo')
        receita.tempo_preparo = request.POST.get('tempo_preparo')
        receita.rendimento = request.POST.get('rendimento')
        receita.categoria = request.POST.get('categoria')
        if request.FILES.get('foto_receita'):
            receita.foto_receita = request.FILES.get('foto_receita')
        receita.save()
    return redirect('dashboard')
