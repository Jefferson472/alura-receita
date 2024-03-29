from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from apps.receitas.models import Receita


class ReceitaListView(generic.ListView):
    model = Receita
    paginate_by = 6
    queryset = Receita.objects.order_by('-create_at').filter(status=True)


class ReceitaDetailView(generic.DetailView):
    model = Receita


class ReceitaCreateView(LoginRequiredMixin, CreateView):
    model = Receita
    login_url = '/login/'
    redirect_field_name = 'login'
    fields = [
        'nome_receita', 'ingredientes', 'modo_preparo',
        'tempo_preparo', 'rendimento', 'categoria', 'foto_receita'
    ]
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReceitaDeleteView(LoginRequiredMixin, DeleteView):
    model = Receita
    success_url = reverse_lazy('dashboard')
    login_url = '/login/'
    redirect_field_name = 'login'


class ReceitaUpdateView(LoginRequiredMixin, UpdateView):
    model = Receita
    fields = [
        'nome_receita', 'ingredientes', 'modo_preparo',
        'tempo_preparo', 'rendimento', 'categoria', 'foto_receita'
    ]
    success_url = reverse_lazy('dashboard')
    template_name_suffix = '_update_form'
    login_url = '/login/'
    redirect_field_name = 'login'
