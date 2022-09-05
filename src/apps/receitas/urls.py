from django.urls import path

from apps.receitas.views.busca import buscar
from apps.receitas.views import ReceitaListView, ReceitaDetailView, ReceitaCreateView
from apps.receitas.views.receitas import (
    deleta_receita, edita_receita, atualiza_receita
)


urlpatterns = [
    path('', ReceitaListView.as_view(), name='index'),
    path('receita/<int:pk>', ReceitaDetailView.as_view(), name='receita'),
    path('busca', buscar, name='buscar'),
    path('cria_receita', ReceitaCreateView.as_view(), name='cria_receita'),
    path('deleta/<int:receita_id>', deleta_receita, name='deleta_receita'),
    path('edita_receita/<int:receita_id>', edita_receita, name='edita_receita'),
    path('atualiza_receita', atualiza_receita, name='atualiza_receita')
]
