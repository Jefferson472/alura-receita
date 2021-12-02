from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal


class IndexViewTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal='calopsita',
            predador='Não',
            venenoso='Não',
            domestico='Não',
        )

    def test_index_view_retorna_caracteristica_do_anima(self):
        response = self.client.get(
            '/',
            {'buscar': 'calopsita'}
        )
        caracteristica_do_animal = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristica_do_animal[0].nome_animal, 'calopsita')
