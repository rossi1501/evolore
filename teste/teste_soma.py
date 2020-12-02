import pytest
from src.main import soma


class TestSoma(pytest.TesteCase):
    def test_retorno_soma_10_10(self):
        self.assertEqual(soma(10, 10), 20)
