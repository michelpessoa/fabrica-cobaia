# Verificação — SDD-COBAIA-0005

- **Veredito:** PASS
- **Diff verificado:** d3ea55068b15933a463a559e7741994420a1feb9..be1ae2dcdda28db0c1642329781755c3fe388fbf
- **Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_totais -v` | Ran 6 tests in 0.000s OK EXIT 0 | Mutação 1 (RF01): somar só nomes[:1] em estoque/totais.py:2 -> FAILED (failures=2). Mutação 2 (RF02): retornar 1 para lista vazia -> FAILED (failures=1, test_lista_vazia). Restaurado com git checkout; volta a OK. | Sim | tests/test_totais.py:15 | automatizado |
| 2 | `python3 -m unittest discover -s tests -v` | Ran 14 tests in 0.000s OK EXIT 0 | Com a mutação de RF02 (retornar 1 para lista vazia), a suíte completa resultou em FAILED (failures=1); restaurado com git checkout -- estoque/totais.py, a suíte volta a OK (14 testes). | Sim | tests/test_totais.py:27 | automatizado |

## Descompassos encontrados

nenhum
