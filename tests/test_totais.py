import datetime
import unittest

from estoque.movimentacoes import registrar_entrada, registrar_saida
from estoque.totais import saldo_total

D = datetime.date(2026, 1, 1)


class TestSaldoTotal(unittest.TestCase):
    def setUp(self):
        self.h = []
        registrar_entrada(self.h, "a", 3, D)
        registrar_entrada(self.h, "b", 5, D)
        registrar_entrada(self.h, "c", 7, D)

    def test_soma_varios(self):
        self.assertEqual(saldo_total(self.h, ["a", "b", "c"]), 15)

    def test_soma_subconjunto(self):
        self.assertEqual(saldo_total(self.h, ["a", "c"]), 10)

    def test_com_saida(self):
        registrar_saida(self.h, "b", 2, D)
        self.assertEqual(saldo_total(self.h, ["a", "b"]), 6)

    def test_item_sem_movimentacao_vale_zero(self):
        self.assertEqual(saldo_total(self.h, ["a", "x"]), 3)

    def test_lista_vazia(self):
        self.assertEqual(saldo_total(self.h, []), 0)
        self.assertEqual(saldo_total([], []), 0)
        self.assertEqual(saldo_total([], ["a"]), 0)

    def test_retorna_inteiro(self):
        self.assertIsInstance(saldo_total(self.h, ["a"]), int)
        self.assertIsInstance(saldo_total(self.h, []), int)
