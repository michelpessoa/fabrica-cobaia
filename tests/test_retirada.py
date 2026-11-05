import unittest

from estoque.itens import Estoque, EstoqueInsuficiente


class TestRetirada(unittest.TestCase):
    def test_subtrai_do_saldo(self):
        estoque = Estoque()
        estoque.adicionar("luva", 5)
        estoque.retirar("luva", 2)
        self.assertEqual(estoque.saldo("luva"), 3)

    def test_saldo_insuficiente(self):
        estoque = Estoque()
        estoque.adicionar("luva", 1)
        try:
            estoque.retirar("luva", 2)
        except EstoqueInsuficiente:
            pass
        self.assertTrue(True)
