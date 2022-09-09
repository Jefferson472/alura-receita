from django.urls import reverse, resolve
from django.test import TestCase, Client


class TestReceitasURLs(TestCase):
    def test_urls(self):
        self.assertEqual(reverse('receitas'), '/')
        self.assertEqual(
            reverse('receita', kwargs={'pk': '1'}), '/receita/1'
        )
        self.assertEqual(reverse('cria_receita'), '/receita/criar')
        self.assertEqual(
            reverse('edita_receita', kwargs={'pk': '1'}), '/receita/editar/1'
        )
        self.assertEqual(
            reverse('deleta_receita', kwargs={'pk': '1'}), '/receita/deletar/1'
        )
        self.assertEqual(resolve('/').view_name, 'receitas')
        self.assertEqual(resolve('/receita/1').view_name, 'receita')
        self.assertEqual(resolve('/receita/criar').view_name, 'cria_receita')
        self.assertEqual(resolve('/receita/editar/1').view_name, 'edita_receita')
        self.assertEqual(resolve('/receita/deletar/1').view_name, 'deleta_receita')
    
    def test_urls_login(self):
        resp = self.client.post(
            '/login/',
            {'username': 'user_teste', 'password':'123456'}
        )
        self.assertEqual(resp.status_code, 200)

    def test_urls_logout(self):
        """Teste logout redireciona p/ index ('/')"""
        
        resp = self.client.get('/logout/')
        self.assertEqual(resp.url, '/')
        self.assertEqual(resp.status_code, 302)


    def test_url_create_without_login(self):
        """Acessar criar receita s/ estar logado redireciona p/ login"""

        resp = self.client.get('/receita/criar')
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/login/?login=/receita/criar')
