# Verificação — SDD-COBAIA-0008

- **Veredito:** PASS
- **Diff verificado:** 5a43450516d3327ed4b765aa563600e0530553e1..0e824c7d72da7aae8f2d844bcf6f46c1ed768a11
- **Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_limites -v` | Ran 14 tests in 0.001s OK (exit 0) | Mutações em estoque/limites.py, cada uma restaurada com git checkout: 'limite <= 0' -> 'limite < 0' => FAILED (failures=2); validação removida (if False) => FAILED (failures=3); 'quantidade <= limite' -> '<' => FAILED (failures=5); item sem limite devolve False => FAILED (failures=5); não guardar limite => FAILED (failures=5); pode_retirar sempre True => FAILED (failures=5). Depois de restaurar, v | Sim | tests/test_limites.py:21 | automatizado |
| 2 | `python3 -m unittest discover -s tests -v` | Ran 34 tests in 0.001s OK (exit 0) | Regressão: as mesmas mutações de estoque/limites.py fazem a suíte falhar pelos testes de TestLimites. Depois de restaurar (git status limpo), a suíte completa volta a OK. | Sim | tests/test_limites.py:43 | automatizado |

## Descompassos encontrados

nenhum
