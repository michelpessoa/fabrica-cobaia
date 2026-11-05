# Verificação — SDD-COBAIA-0010

- **Veredito:** PASS
- **Diff verificado:** a8b1b6e87c1ccc40015f63c9bc415dabb6c5a91e..288fc7c84aa12240efad647d26c4f2087aa3e936
- **Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_nomes -v` | Ran 11 tests in 0.000s OK EXIT=0 | Removido .strip() em estoque/nomes.py:2 -> FAILED (failures=6); removido .lower() -> FAILED (failures=6); restaurado com git checkout, voltou a OK | Sim | tests/test_nomes.py:8 | automatizado |
| 2 | `python3 -m unittest discover -s tests -v` | Ran 45 tests in 0.002s OK EXIT=0 | Mutação em estoque/nomes.py:2 (trunca último caractere do resultado) -> suíte completa FAILED (failures=8); restaurado com git checkout, 45 testes OK | Sim | tests/test_nomes.py:11 | automatizado |

## Descompassos encontrados

nenhum
