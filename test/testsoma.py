import unittest
from documento.main import soma

class Testsoma(unittest.TestCase):
    def test_retorno_soma_10_10(self):
        self.assertEqual(soma(10, 10), 20)