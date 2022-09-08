from django.urls import path

from apps.receitas.views.busca import buscar
from apps.receitas.views import (
    ReceitaListView, ReceitaDetailView, ReceitaCreateView,
    ReceitaDeleteView, ReceitaUpdateView
)


urlpatterns = [
    #  Home
    path('', ReceitaListView.as_view(), name='receitas'),

    # CRUD de Receitas
    path('receita/<int:pk>', ReceitaDetailView.as_view(), name='receita'),
    path('receita/criar', ReceitaCreateView.as_view(), name='cria_receita'),
    path('receita/deletar/<int:pk>', ReceitaDeleteView.as_view(), name='deleta_receita'),
    path('receita/editar/<int:pk>', ReceitaUpdateView.as_view(), name='edita_receita'),

    # Busca
    path('busca/', buscar, name='buscar'),
]
