from django.urls import path

from apps.receitas.views.busca import buscar
from apps.receitas.views import (
    ReceitaListView, ReceitaDetailView, ReceitaCreateView, ReceitaDeleteView,
    ReceitaUpdateView
)
from apps.receitas.views.receitas import (
    atualiza_receita
)


urlpatterns = [
    path('', ReceitaListView.as_view(), name='index'),
    path('receita/<int:pk>', ReceitaDetailView.as_view(), name='receita'),
    path('busca', buscar, name='buscar'),
    path('receita/criar', ReceitaCreateView.as_view(), name='cria_receita'),
    path('receita/deletar/<int:pk>', ReceitaDeleteView.as_view(), name='deleta_receita'),
    # path('editar-receita/<int:receita_id>', edita_receita, name='edita_receita'),
    path('receita/editar/<int:pk>', ReceitaUpdateView.as_view(), name='edita_receita'),
    path('autaliza-receita', atualiza_receita, name='atualiza_receita')
]
