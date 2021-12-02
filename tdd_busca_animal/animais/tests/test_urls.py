from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index


class AnimaisURLSTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_index(self):
        """Testa se a rota index está funcionando corretamente"""
        request = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)
