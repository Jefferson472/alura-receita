from django.contrib import admin

from apps.receitas.models import Receita

@admin.register(Receita)
class ReceitasAdmin(admin.ModelAdmin):
    list_display = (
        'id','nome_receita', 'categoria',
        'tempo_preparo', 'status'
    )

    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('status',)
    list_per_page = 5
