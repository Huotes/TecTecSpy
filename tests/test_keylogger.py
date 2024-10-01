import unittest
from unittest.mock import MagicMock
from tecspy.keylogger import KeyLogger

class TestKeyLogger(unittest.TestCase):

    def setUp(self):
        # Cria um mock para simular o comportamento do callback de log
        self.mock_logger = MagicMock()
        self.keylogger = KeyLogger(log_callback=self.mock_logger)

    def test_key_logging(self):
        # Simula uma tecla normal sendo pressionada
        self.keylogger.on_press('a')

        # Verifica se o logger foi chamado com o caractere correto
        self.mock_logger.assert_called_with('a')

    def test_special_key_logging(self):
        # Simula uma tecla especial sendo pressionada (como Shift)
        from pynput.keyboard import Key
        self.keylogger.on_press(Key.shift)

        # Verifica se o logger foi chamado com a representação correta da tecla especial
        self.mock_logger.assert_called_with('Special key Key.shift pressed')

if __name__ == '__main__':
    unittest.main()
