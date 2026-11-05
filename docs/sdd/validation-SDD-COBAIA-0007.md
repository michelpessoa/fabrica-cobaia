# Verificação — SDD-COBAIA-0007

- **Veredito:** PASS
- **Diff verificado:** c748cff8196aa602f23917c301b0aba1fcfed47a..6b4f3eac4d041c0b329dce98ff7b5a24921951be
- **Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_disponiveis -v` | Ran 6 tests in 0.000s OK (exit 0): test_devolve_lista, test_devolve_so_com_saldo_na_ordem_recebida, test_item_desconhecido_sem_saldo, test_lista_vazia, test_ordem_recebida_nao_alfabetica, test_saldo_um_conta, todos ok | Três mutações em estoque/disponiveis.py:2. (a) '> 0' trocado por '>= 0': FAILED (failures=3). (b) resultado passado por sorted() no lugar da ordem recebida: FAILED (failures=2). (c) filtro de saldo removido: FAILED (failures=3). Depois de cada uma, restaurei com git checkout -- estoque/disponiveis.py. Rodei de novo: OK, e git status ficou limpo. | Sim | tests/test_disponiveis.py:12 | automatizado |

## Descompassos encontrados

nenhum
