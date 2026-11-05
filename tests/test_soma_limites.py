import unittest

from estoque.soma_limites import somar_limites


class TestSomaLimites(unittest.TestCase):
    def test_soma_de_valores(self):
        r = somar_limites([1, 2, 3])
        self.assertEqual(r, 6)
        self.assertIsInstance(r, int)

    def test_um_valor(self):
        self.assertEqual(somar_limites([5]), 5)

    def test_negativos(self):
        self.assertEqual(somar_limites([-2, 5, -1]), 2)

    def test_lista_vazia(self):
        r = somar_limites([])
        self.assertEqual(r, 0)
        self.assertIsInstance(r, int)

    def test_zeros(self):
        r = somar_limites([0, 0, 0])
        self.assertEqual(r, 0)
        self.assertIsInstance(r, int)

    def test_soma_que_zera(self):
        self.assertEqual(somar_limites([3, -3]), 0)

    def test_todos_negativos(self):
        self.assertEqual(somar_limites([-1, -2, -3]), -6)

    def test_valores_grandes(self):
        self.assertEqual(somar_limites([10**12, 10**12, 1]), 2 * 10**12 + 1)

    def test_lista_longa(self):
        self.assertEqual(somar_limites(list(range(1, 101))), 5050)

    def test_nao_altera_entrada(self):
        v = [4, 5, 6]
        somar_limites(v)
        self.assertEqual(v, [4, 5, 6])


if __name__ == "__main__":
    unittest.main()
