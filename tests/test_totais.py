import unittest

from estoque.itens import Estoque
from estoque.totais import saldo_total


class TestSaldoTotal(unittest.TestCase):
    def setUp(self):
        self.e = Estoque()
        self.e.adicionar("a", 3)
        self.e.adicionar("b", 5)
        self.e.adicionar("c", 7)

    def test_soma_varios(self):
        self.assertEqual(saldo_total(self.e, ["a", "b", "c"]), 15)

    def test_soma_subconjunto(self):
        self.assertEqual(saldo_total(self.e, ["a", "c"]), 10)

    def test_um_item(self):
        self.assertEqual(saldo_total(self.e, ["b"]), 5)

    def test_item_inexistente_vale_zero(self):
        self.assertEqual(saldo_total(self.e, ["a", "x"]), 3)

    def test_lista_vazia(self):
        self.assertEqual(saldo_total(self.e, []), 0)
        self.assertEqual(saldo_total(Estoque(), []), 0)

    def test_retorna_inteiro(self):
        self.assertIsInstance(saldo_total(self.e, ["a"]), int)
        self.assertIsInstance(saldo_total(self.e, []), int)
