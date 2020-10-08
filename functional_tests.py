from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Edith ouviu falar de uma nova aplicação online interessante para
        # lista de tarefas. Ela então decide verificar sua homepage 
        self.browser.get('http://localhost:8000')

        # Ela percebe que o título da página e o cabeçalho mencionam listas de tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # Ela é convidada a inserir um item imediatamente
        
        # Ela digita "Buy peacock feathers" (Comprar penas de pavão) em uma caixa de texto
        # (o hobby de Edith é fazer iscas de pescas com fly)

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro item
        # Ela insere "Use peacock feathers to make a fly" (Usar as penas de pavão para fazer
        # um fly)

        # A pagina é atualizada novamente e agora mostra os dois itens em su lista

        # Edith se pergunta se o site lembrará de sua lista. Então ela anota que o site gerou um
        # URL único para ela -- há um pequeno texto explicativo para isso

        # Satisfeita, ela volta a dormir

        if __name__ == 'main':
            unittest.main(warnings='ignore')

