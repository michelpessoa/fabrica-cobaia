import datetime
import unittest

from estoque.movimentacoes import registrar_entrada, registrar_saida, saldo_por_item

D1 = datetime.date(2026, 1, 1)
D2 = datetime.date(2026, 1, 2)
D3 = datetime.date(2026, 1, 3)


class TestEntrada(unittest.TestCase):
    def test_acrescenta_dict(self):
        h = []
        self.assertIsNone(registrar_entrada(h, "a", 3, D1))
        self.assertEqual(h, [{"tipo": "entrada", "item": "a", "quantidade": 3, "data": D1}])

    def test_acrescenta_ao_fim(self):
        h = []
        registrar_entrada(h, "a", 1, D1)
        registrar_entrada(h, "b", 2, D2)
        self.assertEqual([m["item"] for m in h], ["a", "b"])
        self.assertEqual(set(h[0]), {"tipo", "item", "quantidade", "data"})

    def test_invalidos(self):
        for q in (True, False, 1.0, 2.5, 0, -1, "1", None):
            h = []
            with self.assertRaises(ValueError, msg=repr(q)):
                registrar_entrada(h, "a", q, D1)
            self.assertEqual(h, [])
        for it in ("", "   ", "\t"):
            h = []
            with self.assertRaises(ValueError):
                registrar_entrada(h, it, 1, D1)
            self.assertEqual(h, [])

    def test_quantidade_um_valida(self):
        h = []
        registrar_entrada(h, "a", 1, D1)
        self.assertEqual(len(h), 1)


class TestSaida(unittest.TestCase):
    def test_saida_valida(self):
        h = []
        registrar_entrada(h, "a", 5, D1)
        self.assertIsNone(registrar_saida(h, "a", 2, D2))
        self.assertEqual(h[-1], {"tipo": "saida", "item": "a", "quantidade": 2, "data": D2})
        self.assertEqual(saldo_por_item(h), {"a": 3})

    def test_saida_igual_ao_saldo(self):
        h = []
        registrar_entrada(h, "a", 5, D1)
        registrar_saida(h, "a", 5, D2)
        self.assertEqual(saldo_por_item(h)["a"], 0)
        self.assertEqual(len(h), 2)

    def test_saida_acima_do_saldo(self):
        h = []
        registrar_entrada(h, "a", 5, D1)
        with self.assertRaises(ValueError):
            registrar_saida(h, "a", 6, D2)
        self.assertEqual(len(h), 1)

    def test_saida_sem_movimentacao(self):
        h = []
        with self.assertRaises(ValueError):
            registrar_saida(h, "a", 1, D1)
        self.assertEqual(h, [])

    def test_saldo_de_outro_item_nao_conta(self):
        h = []
        registrar_entrada(h, "b", 10, D1)
        with self.assertRaises(ValueError):
            registrar_saida(h, "a", 1, D1)
        self.assertEqual(len(h), 1)

    def test_saida_apos_saida_considera_todas(self):
        h = []
        registrar_entrada(h, "a", 5, D1)
        registrar_saida(h, "a", 3, D2)
        with self.assertRaises(ValueError):
            registrar_saida(h, "a", 3, D3)
        self.assertEqual(len(h), 2)

    def test_invalidos(self):
        for q in (True, 1.0, 0, -1):
            h = []
            registrar_entrada(h, "a", 5, D1)
            with self.assertRaises(ValueError, msg=repr(q)):
                registrar_saida(h, "a", q, D2)
            self.assertEqual(len(h), 1)
        for it in ("", "  "):
            h = []
            with self.assertRaises(ValueError):
                registrar_saida(h, it, 1, D1)
            self.assertEqual(h, [])


class TestSaldoPorItem(unittest.TestCase):
    def setUp(self):
        self.h = []
        registrar_entrada(self.h, "a", 5, D1)
        registrar_entrada(self.h, "b", 2, D1)
        registrar_saida(self.h, "a", 2, D2)
        registrar_entrada(self.h, "a", 10, D3)

    def test_sem_ate(self):
        self.assertEqual(saldo_por_item(self.h), {"a": 13, "b": 2})

    def test_vazio(self):
        self.assertEqual(saldo_por_item([]), {})

    def test_ate_inclusivo(self):
        self.assertEqual(saldo_por_item(self.h, D1), {"a": 5, "b": 2})
        self.assertEqual(saldo_por_item(self.h, D2), {"a": 3, "b": 2})
        self.assertEqual(saldo_por_item(self.h, D3), {"a": 13, "b": 2})

    def test_ate_antes_de_tudo(self):
        self.assertEqual(saldo_por_item(self.h, datetime.date(2025, 12, 31)), {})

    def test_ate_nomeado(self):
        self.assertEqual(saldo_por_item(self.h, ate=D2), {"a": 3, "b": 2})


class TestFronteirasExtras(unittest.TestCase):
    def test_saida_usa_saldo_de_todas_as_movimentacoes(self):
        h = []
        registrar_entrada(h, "a", 5, D3)
        registrar_saida(h, "a", 3, D1)
        self.assertEqual(len(h), 2)
        self.assertEqual(saldo_por_item(h), {"a": 2})

    def test_saida_invalida_nao_altera_historico(self):
        h = []
        registrar_entrada(h, "a", 5, D1)
        copia = [dict(m) for m in h]
        for q in (6, 2.5, True, 0, -3):
            with self.assertRaises(ValueError):
                registrar_saida(h, "a", q, D2)
        self.assertEqual(h, copia)

    def test_saldo_negativo_por_saida_ate(self):
        h = []
        registrar_entrada(h, "a", 5, D1)
        registrar_saida(h, "a", 5, D2)
        registrar_entrada(h, "a", 1, D3)
        self.assertEqual(saldo_por_item(h, D2), {"a": 0})
        self.assertEqual(saldo_por_item(h), {"a": 1})
