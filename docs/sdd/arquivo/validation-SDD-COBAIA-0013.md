# Verificação — SDD-COBAIA-0013

- **Veredito:** PASS
- **Diff verificado:** cd4a662af138fa69cfaa36aeaeb821bb999150b3..766d417779486ea5bb220f4d18d15fca27376453
- **Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| Fidelidade à origem (check_source_docs) | `python3 /home/michel/doc-traceability-framework/_framework/scripts/check_source_docs.py docs/sdd/SDD-COBAIA-0013.md /home/michel/fabrica-central-teste/docs/COBAIA (em origin/main)` | { "schema": "dtf.resultado-validador/1", "script": "check_source_docs.py", "framework_version": "2.8.0", "ok": true, "exit_code": 0, "problemas": [], "avisos": [] } | sem teste automatizado (script do kit) | Sim | n/a | n/a |
| Fidelidade à origem | `comparação entre docs/sdd/SDD-COBAIA-0013.md, o contrato e a SPEC-COBAIA-0002` | Os textos de aceite RF01–RF06 no contrato são iguais aos critérios EARS da SPEC. Os 8 critérios da SDD cobrem a estratégia de teste da SPEC (bool, float, 0, negativa, vazio, só espaços, saída acima do saldo, saída igual ao saldo, ate) e usam os mesmos comandos. A 'especificacao' do contrato reproduz a Parte 2 da SPEC sem mudanças. Nada foi relaxado. | sem teste automatizado | Sim | n/a | manual |
| 1 | `python3 -m unittest tests.test_movimentacoes -v` | Ran 19 tests ... OK (exit 0) | Cinco mutações, cada uma rodada à parte; todas fizeram o teste falhar: tirar o 'or isinstance(quantidade, bool)' (3 falhas); trocar 'quantidade <= 0' por '< 0' (3 falhas); trocar 'not item.strip()' por 'not item' (1 falha); tirar a checagem isinstance int (3 falhas); pôr uma chave extra no dict de entrada (2 falhas). Depois de restaurar, o teste passa. | Sim | tests/test_movimentacoes.py:15 | automatizado |
| 2 | `python3 -m unittest tests.test_movimentacoes -v` | Ran 19 tests ... OK (exit 0) | Quatro mutações, todas fizeram o teste falhar: trocar '>' por '>=' na checagem de saldo (2 erros); tirar a checagem de saldo (5 falhas); tirar _validar de registrar_saida (2 falhas); gravar a saída com tipo 'entrada' (8 falhas). Depois de restaurar, o teste passa. | Sim | tests/test_movimentacoes.py:47 | automatizado |
| 3 | `python3 -m unittest tests.test_movimentacoes -v` | Ran 19 tests ... OK (exit 0) | Três mutações, todas fizeram o teste falhar: trocar 'data <= ate' por '<' (3 falhas); ignorar ate (4 falhas); somar a saída com sinal +1 (8 falhas). Depois de restaurar, o teste passa. | Sim | tests/test_movimentacoes.py:114 | automatizado |
| 4 | `python3 -m unittest tests.test_totais -v` | Ran 6 tests ... OK (exit 0) | Duas mutações, ambas fizeram o teste falhar: usar max(saldo, 3) (2 falhas); usar saldos[nome] no lugar de .get(nome, 0) (2 erros). Depois de restaurar, o teste passa. | Sim | tests/test_totais.py:28 | automatizado |
| 5 | `python3 -m unittest tests.test_consultas -v` | Ran 8 tests ... OK (exit 0) | Três mutações, todas fizeram o teste falhar: default .get(nome, 1) (5 falhas); iterar sorted(nomes) (2 falhas); trocar '== 0' por '<= 1' (3 falhas). Depois de restaurar, o teste passa. | Sim | tests/test_consultas.py:19 | automatizado |
| 6 | `python3 -m unittest tests.test_disponiveis -v` | Ran 7 tests ... OK (exit 0) | Três mutações, todas fizeram o teste falhar: trocar '> 0' por '>= 0' (4 falhas); iterar sorted(nomes) (2 falhas); trocar '> 0' por '> 1' (4 falhas). Depois de restaurar, o teste passa. | Sim | tests/test_disponiveis.py:33 | automatizado |
| 7 | `python3 -m compileall -q estoque tests` | exit 0, sem saída | Um erro de sintaxe colocado em estoque/totais.py fez o comando sair com exit 1. Depois de restaurar, exit 0. | Sim | n/a | automatizado |
| 8 | `python3 -m unittest discover -s tests -v` | Ran 89 tests ... OK (exit 0) | Trocar 'else -1' por 'else 1' em movimentacoes.py fez a suíte sair com exit 1. Depois de restaurar e limpar o __pycache__ velho, que vinha da mutação, a suíte voltou a passar com exit 0. | Sim | n/a | automatizado |

## Descompassos encontrados

nenhum
