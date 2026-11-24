import datetime
import unittest

from estoque.disponiveis import itens_com_saldo
from estoque.movimentacoes import registrar_entrada, registrar_saida

D = datetime.date(2026, 1, 1)


class TestItensComSaldo(unittest.TestCase):
    def test_devolve_so_com_saldo_na_ordem_recebida(self):
        h = []
        registrar_entrada(h, "luva", 3, D)
        registrar_entrada(h, "bota", 1, D)
        self.assertEqual(itens_com_saldo(h, ["capa", "luva", "mascara", "bota", "arnes"]),
                         ["luva", "bota"])

    def test_ordem_recebida_nao_alfabetica(self):
        h = []
        registrar_entrada(h, "a", 1, D)
        registrar_entrada(h, "b", 1, D)
        self.assertEqual(itens_com_saldo(h, ["b", "a"]), ["b", "a"])

    def test_item_sem_movimentacao_nao_entra(self):
        self.assertEqual(itens_com_saldo([], ["x"]), [])

    def test_saida_total_remove(self):
        h = []
        registrar_entrada(h, "a", 2, D)
        registrar_saida(h, "a", 2, D)
        registrar_entrada(h, "b", 2, D)
        registrar_saida(h, "b", 1, D)
        self.assertEqual(itens_com_saldo(h, ["a", "b"]), ["b"])

    def test_saldo_um_conta(self):
        h = []
        registrar_entrada(h, "a", 1, D)
        self.assertEqual(itens_com_saldo(h, ["a", "b"]), ["a"])

    def test_lista_vazia(self):
        self.assertEqual(itens_com_saldo([], []), [])

    def test_devolve_lista(self):
        self.assertIsInstance(itens_com_saldo([], iter(["x"])), list)
