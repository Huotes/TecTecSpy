import unittest
import os
from tecspy.logger import Logger

class TestLogger(unittest.TestCase):

    def setUp(self):
        # Cria um arquivo temporário para armazenar os logs
        self.log_file = '/tmp/test_keylogger.log'
        self.logger = Logger(self.log_file)

    def tearDown(self):
        # Remove o arquivo de log após cada teste
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_key(self):
        # Testa se o log de uma tecla pressionada é salvo corretamente
        self.logger.log_key('a')

        # Verifica se a tecla 'a' foi registrada no arquivo de log
        with open(self.log_file, 'r') as f:
            log_content = f.read()

        self.assertIn('a', log_content)

    def test_log_special_event(self):
        # Testa se eventos especiais são registrados corretamente
        self.logger.log_special_event('Special event triggered')

        # Verifica se o evento especial foi registrado
        with open(self.log_file, 'r') as f:
            log_content = f.read()

        self.assertIn('Special event triggered', log_content)

if __name__ == '__main__':
    unittest.main()
