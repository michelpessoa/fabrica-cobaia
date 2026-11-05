import unittest

from estoque.nomes import normalizar


class TestNormalizar(unittest.TestCase):
    def test_remove_espacos_nas_pontas(self):
        self.assertEqual(normalizar("  luva  "), "luva")

    def test_converte_para_minusculas(self):
        self.assertEqual(normalizar("LuVa"), "luva")

    def test_nome_ja_normalizado(self):
        self.assertEqual(normalizar("luva"), "luva")

    def test_preserva_espacos_internos(self):
        self.assertEqual(normalizar(" Bota  Longa "), "bota  longa")

    def test_so_espacos_devolve_vazio(self):
        self.assertEqual(normalizar("   "), "")

    def test_devolve_string(self):
        self.assertIsInstance(normalizar("  LUVA "), str)

    def test_string_vazia(self):
        self.assertEqual(normalizar(""), "")

    def test_remove_tabs_e_quebras_de_linha(self):
        self.assertEqual(normalizar("\t\nLuva\r\n "), "luva")

    def test_so_pontas_removidas_apenas_de_um_lado(self):
        self.assertEqual(normalizar("  Luva"), "luva")
        self.assertEqual(normalizar("Luva  "), "luva")

    def test_acentos_em_minusculas(self):
        self.assertEqual(normalizar(" ÁGUA Ção "), "água ção")

    def test_idempotente(self):
        once = normalizar("  BoTa Longa ")
        self.assertEqual(normalizar(once), once)
