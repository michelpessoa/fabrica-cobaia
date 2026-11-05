# Verificação — SDD-COBAIA-0011

- **Veredito:** PASS
- **Diff verificado:** 88ede27ac9da2808b311bccaee27eaa34af717b3..83a606de0b8eefdde8fd2ced8f532287a63b8015
- **Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_soma_limites -v` | Ran 10 tests in 0.000s OK EXIT 0 | Mutação 1: estoque/soma_limites.py:3 trocado por int(sum(valores[1:])) -> FAILED (failures=7). Mutação 2: devolver None para lista vazia -> FAIL test_lista_vazia (failures=1). Restaurado com git checkout, volta para OK. | Sim | tests/test_soma_limites.py:9 | automatizado |
| 2 | `python3 -m unittest discover -s tests -v` | Ran 67 tests in 0.003s OK EXIT 0 | Mutação int(sum(valores[1:])) em estoque/soma_limites.py:3 -> discover FAILED (failures=7); restaurado, volta para OK. | Sim | tests/test_soma_limites.py:20 | automatizado |

## Descompassos encontrados

nenhum
