from django.test import TestCase, RequestFactory
from animais.models import Animal


class AnimalModeTestCase(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(
            nome_animal='calopsita',
            predador=True,
            venenoso=False,
            domestico=False,
        )

    def test_animal_model(self):
        self.assertEqual(self.animal.nome_animal, 'calopsita')
