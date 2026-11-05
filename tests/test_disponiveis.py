import unittest

from estoque.disponiveis import itens_com_saldo
from estoque.itens import Estoque


class TestItensComSaldo(unittest.TestCase):
    def test_devolve_so_com_saldo_na_ordem_recebida(self):
        e = Estoque()
        e.adicionar("luva", 3)
        e.adicionar("bota", 1)
        self.assertEqual(itens_com_saldo(e, ["capa", "luva", "mascara", "bota", "arnes"]),
                         ["luva", "bota"])

    def test_ordem_recebida_nao_alfabetica(self):
        e = Estoque()
        e.adicionar("a", 1)
        e.adicionar("b", 1)
        self.assertEqual(itens_com_saldo(e, ["b", "a"]), ["b", "a"])

    def test_item_desconhecido_sem_saldo(self):
        self.assertEqual(itens_com_saldo(Estoque(), ["x"]), [])

    def test_saldo_um_conta(self):
        e = Estoque()
        e.adicionar("a", 1)
        self.assertEqual(itens_com_saldo(e, ["a", "b"]), ["a"])

    def test_lista_vazia(self):
        self.assertEqual(itens_com_saldo(Estoque(), []), [])

    def test_devolve_lista(self):
        self.assertIsInstance(itens_com_saldo(Estoque(), ["x"]), list)
