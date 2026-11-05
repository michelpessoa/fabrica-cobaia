# Verificação — SDD-COBAIA-0009

- **Veredito:** PASS
- **Diff verificado:** d4f21467a9adec675bc9c176efe8739b78f44ee0..69942585a2cbdab19acdee3f648f051605f15def
- **Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_reposicao -v` | Ran 12 tests in 0.001s OK (exit 0) | Mutações em estoque/reposicao.py: 'or'->'and' na checagem de vazio => FAILED (failures=1); remover checagem de vazio (if False) => FAILED (failures=2); trocar compare_digest por '==' => FAILED (failures=2); negar compare_digest => FAILED (failures=7). Restaurado com git checkout, volta a OK. | Sim | tests/test_reposicao.py:9 | automatizado |
| 2 | `python3 -m unittest discover -s tests -v` | Ran 57 tests in 0.003s OK (exit 0) | Regressão: a suíte inclui tests/test_reposicao.py, que falhou sob as mesmas mutações do critério 1; restaurado e verde. | Sim | tests/test_reposicao.py:9 | automatizado |

## Descompassos encontrados

nenhum
