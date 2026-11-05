import unittest

from estoque.itens import Estoque, EstoqueInsuficiente


class TestRetirada(unittest.TestCase):
    def test_subtrai_do_saldo(self):
        estoque = Estoque()
        estoque.adicionar("luva", 5)
        estoque.retirar("luva", 2)
        self.assertEqual(estoque.saldo("luva"), 3)

    def test_saldo_insuficiente(self):
        self.assertTrue(issubclass(EstoqueInsuficiente, Exception))
