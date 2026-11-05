import unittest

from estoque.limites import Limites


class TestLimites(unittest.TestCase):
    def setUp(self):
        self.l = Limites()

    def test_guarda_limite_positivo(self):
        self.l.definir_limite("a", 5)
        self.assertTrue(self.l.pode_retirar("a", 5))
        self.assertFalse(self.l.pode_retirar("a", 6))

    def test_limite_minimo_positivo(self):
        self.l.definir_limite("a", 1)
        self.assertTrue(self.l.pode_retirar("a", 1))
        self.assertFalse(self.l.pode_retirar("a", 2))

    def test_zero_lanca_value_error(self):
        with self.assertRaises(ValueError):
            self.l.definir_limite("a", 0)
        self.assertTrue(self.l.pode_retirar("a", 1000))

    def test_negativo_lanca_value_error(self):
        with self.assertRaises(ValueError):
            self.l.definir_limite("a", -1)
        self.assertTrue(self.l.pode_retirar("a", 1000))

    def test_sem_limite(self):
        self.assertTrue(self.l.pode_retirar("x", 10**6))

    def test_abaixo_do_limite(self):
        self.l.definir_limite("a", 10)
        self.assertTrue(self.l.pode_retirar("a", 9))

    def test_igual_ao_limite(self):
        self.l.definir_limite("a", 10)
        self.assertTrue(self.l.pode_retirar("a", 10))

    def test_acima_do_limite(self):
        self.l.definir_limite("a", 10)
        self.assertFalse(self.l.pode_retirar("a", 11))

    def test_limite_por_item(self):
        self.l.definir_limite("a", 1)
        self.assertTrue(self.l.pode_retirar("b", 50))

    def test_redefinir_limite(self):
        self.l.definir_limite("a", 1)
        self.l.definir_limite("a", 20)
        self.assertTrue(self.l.pode_retirar("a", 20))

    def test_redefinir_invalido_mantem_limite_anterior(self):
        self.l.definir_limite("a", 5)
        with self.assertRaises(ValueError):
            self.l.definir_limite("a", 0)
        self.assertTrue(self.l.pode_retirar("a", 5))
        self.assertFalse(self.l.pode_retirar("a", 6))

    def test_redefinir_para_menor(self):
        self.l.definir_limite("a", 20)
        self.l.definir_limite("a", 2)
        self.assertFalse(self.l.pode_retirar("a", 3))

    def test_quantidade_zero_com_limite(self):
        self.l.definir_limite("a", 3)
        self.assertTrue(self.l.pode_retirar("a", 0))

    def test_instancias_independentes(self):
        outro = Limites()
        self.l.definir_limite("a", 1)
        self.assertTrue(outro.pode_retirar("a", 99))


if __name__ == "__main__":
    unittest.main()
