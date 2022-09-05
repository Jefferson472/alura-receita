from django.urls import path

from apps.receitas.views.busca import buscar
from apps.receitas.views import ReceitasView
from apps.receitas.views.receitas import (
    index, receita, cria_receita, deleta_receita, edita_receita, atualiza_receita
)


urlpatterns = [
    path('', ReceitasView.as_view(), name='index'),
    path('receita/<int:receita_id>', receita, name='receita'),
    path('busca', buscar, name='buscar'),
    path('cria_receita', cria_receita, name='cria_receita'),
    path('deleta/<int:receita_id>', deleta_receita, name='deleta_receita'),
    path('edita_receita/<int:receita_id>', edita_receita, name='edita_receita'),
    path('atualiza_receita', atualiza_receita, name='atualiza_receita')
]
