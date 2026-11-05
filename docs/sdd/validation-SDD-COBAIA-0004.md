# Verificação — SDD-COBAIA-0004

- **Veredito:** PASS
- **Diff verificado:** 01b7d5b6c84fa5a43ec6b3b1f85e2f2531e28b99..c881afda4dc0406692ad6158d0fec995b5c62f07
- **Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_consultas -v` | Ran 6 tests in 0.000s OK (exit 0): test_devolve_lista, test_devolve_so_zerados_na_ordem_recebida, test_item_desconhecido_tem_saldo_zero, test_lista_vazia, test_nenhum_zerado, test_saldo_um_nao_e_zerado | Mutação 1: '== 0' trocado por '!= 0' em estoque/consultas.py:2 -> FAILED (failures=4). Mutação 2: iteração em reversed(list(nomes)) -> FAILED (failures=1). Mutação 3: filtro removido -> FAILED (failures=3). Depois do git checkout, volta a OK. | Sim | tests/test_consultas.py:12 | automatizado |
| 2 | `python3 -m unittest discover -s tests -v` | Ran 8 tests in 0.000s OK (exit 0): os 6 de TestItensZerados mais test_itens.TestAdicionar (test_recusa_quantidade_nao_positiva, test_soma_ao_saldo) | Mutação em estoque/itens.py:6 ('<= 0' trocado por '< 0') -> FAILED (failures=1). Mutação de consultas.py com '!= 0' também faz a suíte falhar. Depois do git checkout, volta a OK. | Sim | tests/test_itens.py:14 | automatizado |

## Descompassos encontrados

nenhum
