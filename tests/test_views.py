from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.test import TestCase, Client

from apps.receitas.models import Receita


class TestReceitasViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.user.set_password('123456')
        self.user.save()

        self.img = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('docs/alura_receita_tour.gif', 'rb').read(),
            content_type='image/gif'
        )

        self.receita = Receita.objects.create(
            user=self.user, 
            nome_receita='Receita Teste',
            ingredientes='Ingredientes Teste',
            modo_preparo='Modo de preparo Teste',
            tempo_preparo=10,
            rendimento='Uma Porção',
            categoria='Sobremesa',
            status=True,
            foto_receita=self.img,
        )
    
    def logged_in(self):
        client = Client()
        client.login(username='test_user', password='123456')
        return client

    def test_index(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['receita_list']), 1)

    def test_detail(self):
        resp = self.client.get('/receita/1')
        self.assertEqual(resp.status_code, 200)

    def test_create(self):
        client = Client()
        client.login(username='test_user', password='123456')
        resp = client.get('/receita/criar')
        self.assertEqual(resp.status_code, 200)

        resp = client.post(
            '/receita/criar',
            {
                'nome_receita': 'Nova Receita',
                'ingredientes': 'Ingredientes Teste',
                'modo_preparo': 'Modo de preparo Teste',
                'tempo_preparo': 10,
                'rendimento': 'Uma Porção',
                'categoria': 'Sobremesa',
                'foto_receita': '',
            },
            follow=True,
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Nova Receita')

    def test_create_field_required(self):
        client = self.logged_in()
        resp = client.get('/receita/criar')
        self.assertEqual(resp.status_code, 200)

        resp = client.post(
            '/receita/criar',
            {
                'nome_receita': '',
                'ingredientes': 'Ingredientes Teste',
                'modo_preparo': 'Modo de preparo Teste',
                'tempo_preparo': 10,
                'rendimento': 'Uma Porção',
                'categoria': 'Sobremesa',
                'foto_receita': '',
            },
            follow=True,
        )
        self.assertFormError(resp, 'form', 'nome_receita', 'Este campo é obrigatório.')

    def test_update(self):
        client = self.logged_in()
        resp = client.post(
            '/receita/editar/1',
            {
                'nome_receita': 'Receita Atualizada',
                'ingredientes': 'Ingredientes Teste',
                'modo_preparo': 'Modo de preparo Teste',
                'tempo_preparo': 10,
                'rendimento': 'Uma Porção',
                'categoria': 'Sobremesa',
                'foto_receita': self.img,
            },follow=True,
        )

        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Receita Atualizada')

    def test_delete(self):
        resp = self.client.post('/receita/deletar/1', follow=True)
        self.assertEqual(resp.status_code, 200)