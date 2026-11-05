import unittest

from estoque.itens import Estoque


class TestAdicionar(unittest.TestCase):
    def test_soma_ao_saldo(self):
        estoque = Estoque()
        estoque.adicionar("luva", 3)
        estoque.adicionar("luva", 2)
        self.assertEqual(estoque.saldo("luva"), 5)

    def test_recusa_quantidade_nao_positiva(self):
        with self.assertRaises(ValueError):
            Estoque().adicionar("luva", 0)
