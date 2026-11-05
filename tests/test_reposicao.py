import unittest
from unittest import mock

from estoque.reposicao import token_valido


class TestToken(unittest.TestCase):
    def test_tokens_iguais_devolvem_true(self):
        self.assertIs(token_valido("abc123", "abc123"), True)

    def test_tokens_de_um_caractere_iguais(self):
        self.assertIs(token_valido("a", "a"), True)

    def test_tokens_diferentes_devolvem_false(self):
        self.assertIs(token_valido("abc123", "abc124"), False)

    def test_tokens_com_tamanhos_diferentes_devolvem_false(self):
        self.assertIs(token_valido("abc", "abc123"), False)
        self.assertIs(token_valido("abc123", "abc"), False)

    def test_diferenca_de_caixa_devolve_false(self):
        self.assertIs(token_valido("ABC", "abc"), False)

    def test_recebido_vazio_devolve_false(self):
        self.assertIs(token_valido("", "abc"), False)

    def test_esperado_vazio_devolve_false(self):
        self.assertIs(token_valido("abc", ""), False)

    def test_os_dois_vazios_devolvem_false(self):
        self.assertIs(token_valido("", ""), False)

    def test_retorno_e_bool(self):
        self.assertIsInstance(token_valido("abc", "abc"), bool)
        self.assertIsInstance(token_valido("abc", "abd"), bool)
        self.assertIsInstance(token_valido("", "abc"), bool)

    def test_usa_compare_digest(self):
        with mock.patch(
            "estoque.reposicao.hmac.compare_digest", return_value=True
        ) as compare:
            self.assertIs(token_valido("abc", "xyz"), True)
        compare.assert_called_once_with("abc", "xyz")

    def test_resultado_de_compare_digest_e_respeitado(self):
        with mock.patch(
            "estoque.reposicao.hmac.compare_digest", return_value=False
        ) as compare:
            self.assertIs(token_valido("abc", "abc"), False)
        compare.assert_called_once_with("abc", "abc")

    def test_vazio_devolve_false_mesmo_com_compare_digest_true(self):
        with mock.patch(
            "estoque.reposicao.hmac.compare_digest", return_value=True
        ):
            self.assertIs(token_valido("", "abc"), False)
            self.assertIs(token_valido("abc", ""), False)
            self.assertIs(token_valido("", ""), False)


if __name__ == "__main__":
    unittest.main()
