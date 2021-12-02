from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from datetime import datetime
from . import classes_voo
from passagens.validation import *


class PassagemForm(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Data Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Data Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(
        label='Data Pesquisa',
        disabled=True,
        initial=datetime.today()
        )
    classe_viagem = forms.ChoiceField(
        label='Classe de Viagem',
        choices=classes_voo.CLASSE_VOO
        )
    informacoes = forms.CharField(
        label='Informações adicionais',
        max_length=100,
        widget=forms.Textarea()
        )
    email = forms.EmailField(label='Email', max_length=100)

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        lista_de_erros = {}
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)            
        return self.cleaned_data
