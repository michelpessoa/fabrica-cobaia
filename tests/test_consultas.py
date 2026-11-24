import datetime
import unittest

from estoque.consultas import itens_zerados
from estoque.movimentacoes import registrar_entrada, registrar_saida

D = datetime.date(2026, 1, 1)


class TestItensZerados(unittest.TestCase):
    def test_devolve_so_zerados_na_ordem_recebida(self):
        h = []
        registrar_entrada(h, "luva", 3, D)
        registrar_entrada(h, "bota", 1, D)
        self.assertEqual(itens_zerados(h, ["capa", "luva", "mascara", "bota", "arnes"]),
                         ["capa", "mascara", "arnes"])

    def test_ordem_nao_alfabetica(self):
        self.assertEqual(itens_zerados([], ["z", "a", "m"]), ["z", "a", "m"])

    def test_item_sem_movimentacao_tem_saldo_zero(self):
        self.assertEqual(itens_zerados([], ["x"]), ["x"])

    def test_saida_total_zera(self):
        h = []
        registrar_entrada(h, "a", 2, D)
        registrar_saida(h, "a", 2, D)
        self.assertEqual(itens_zerados(h, ["a", "b"]), ["a", "b"])

    def test_nenhum_zerado(self):
        h = []
        registrar_entrada(h, "luva", 1, D)
        self.assertEqual(itens_zerados(h, ["luva"]), [])

    def test_lista_vazia(self):
        self.assertEqual(itens_zerados([], []), [])

    def test_saldo_um_nao_e_zerado(self):
        h = []
        registrar_entrada(h, "a", 1, D)
        self.assertEqual(itens_zerados(h, ["a", "b"]), ["b"])

    def test_devolve_lista(self):
        self.assertIsInstance(itens_zerados([], iter(["a"])), list)
