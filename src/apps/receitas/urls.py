from django.urls import path

from apps.receitas.views.busca import buscar
from apps.receitas.views import (
    ReceitaListView, ReceitaDetailView, ReceitaCreateView, ReceitaDeleteView
)
from apps.receitas.views.receitas import (
    edita_receita, atualiza_receita
)


urlpatterns = [
    path('', ReceitaListView.as_view(), name='index'),
    path('receita/<int:pk>', ReceitaDetailView.as_view(), name='receita'),
    path('busca', buscar, name='buscar'),
    path('cria_receita', ReceitaCreateView.as_view(), name='cria_receita'),
    path('deleta/<int:pk>', ReceitaDeleteView.as_view(), name='deleta_receita'),
    path('edita_receita/<int:receita_id>', edita_receita, name='edita_receita'),
    path('atualiza_receita', atualiza_receita, name='atualiza_receita')
]
