import unittest

from estoque.consultas import itens_zerados
from estoque.itens import Estoque


class TestItensZerados(unittest.TestCase):
    def test_devolve_so_zerados_na_ordem_recebida(self):
        e = Estoque()
        e.adicionar("luva", 3)
        e.adicionar("bota", 1)
        self.assertEqual(itens_zerados(e, ["capa", "luva", "mascara", "bota", "arnes"]),
                         ["capa", "mascara", "arnes"])

    def test_item_desconhecido_tem_saldo_zero(self):
        self.assertEqual(itens_zerados(Estoque(), ["x"]), ["x"])

    def test_nenhum_zerado(self):
        e = Estoque()
        e.adicionar("luva", 1)
        self.assertEqual(itens_zerados(e, ["luva"]), [])

    def test_lista_vazia(self):
        self.assertEqual(itens_zerados(Estoque(), []), [])

    def test_saldo_um_nao_e_zerado(self):
        e = Estoque()
        e.adicionar("a", 1)
        self.assertEqual(itens_zerados(e, ["a", "b"]), ["b"])

    def test_devolve_lista(self):
        self.assertIsInstance(itens_zerados(Estoque(), iter(["a"])), list)
