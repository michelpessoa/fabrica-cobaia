import unittest

from estoque.alertas import itens_em_alerta
from estoque.itens import Estoque


class TestAlertas(unittest.TestCase):
    def test_item_baixo(self):
        estoque = Estoque()
        estoque.adicionar("luva", 3)
        self.assertEqual(itens_em_alerta(estoque, ["luva"]), ["luva"])
