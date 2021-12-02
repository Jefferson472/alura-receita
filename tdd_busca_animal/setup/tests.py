from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from animais.models import Animal


class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

        self.animal = Animal.objects.create(
            nome_animal='Leão',
            predador='Sim',
            venenoso='Não',
            domestico='Não'
        )

    def tearDown(self) -> None:
        self.browser.quit()

    def test_busca_animal(self):
        """Teste se um usuário pode buscar um animal pelo nome"""
        home_page = self.browser.get(self.live_server_url)
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), "Exemplo: leão, urso...")

        buscar_animal_input.send_keys('leão')
        self.browser.find_element_by_css_selector('form button').click()

        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)
