from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

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
    success_url = 'usuario/dashboard'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReceitaDeleteView(DeleteView):
    model = Receita
    success_url = reverse_lazy('dashboard')


class ReceitaUpdateView(UpdateView):
    model = Receita
    fields = [
        'nome_receita', 'ingredientes', 'modo_preparo',
        'tempo_preparo', 'rendimento', 'categoria', 'foto_receita'
    ]
    success_url = reverse_lazy('dashboard')
    template_name_suffix = '_update_form'
