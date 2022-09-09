from django.contrib.auth.models import User
from django.test import TestCase, Client

from apps.receitas.models import Receita


class TestReceitaModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.user.set_password('123456')
        self.user.save()

        self.receita = Receita.objects.create(
            user=self.user, 
            nome_receita='Receita Teste',
            ingredientes='Ingredientes Teste',
            modo_preparo='Modo de preparo Teste',
            tempo_preparo=10,
            rendimento='Uma Porção',
            categoria='Sobremesa',
            status=True,
            foto_receita='',
        )

    def test_get_absolute_url(self):
        self.assertEqual(self.receita.get_absolute_url(), '/receita/1')

    def test_title(self):
        self.assertEqual(self.receita.nome_receita, 'Receita Teste')

    def test_login_logout(self):
        client = Client()
        logged_in = client.login(username='test_user', password='123456')
        self.assertTrue(logged_in)
        logout = client.logout()
        self.assertFalse(logout)
        