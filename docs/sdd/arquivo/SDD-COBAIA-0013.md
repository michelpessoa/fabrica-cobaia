---
id: SDD-COBAIA-0013
type: SDD
title: "Histórico de movimentações de estoque e consultas de saldo calculadas a partir dele"
status: implemented
approved_by:
  kind: policy
  actor: fabrica-agentica
  at: "2026-11-23T21:27:03Z"
  content_sha256: "4185ae6e37d958f7d03e60d5c84dfdeed9c06d83ffbbb03840b36151aa7958e4"
  transitions:
    - {from: draft, to: in_review, at: "2026-11-23T21:27:03Z"}
    - {from: in_review, to: approved, at: "2026-11-23T21:27:03Z"}
project: "COBAIA"
owner: "Michel Pessoa"
created: "2026-11-23"
updated: "2026-11-23"
relates_to: []
source_docs:
  - id: "SPEC-COBAIA-0002"
    url: "https://github.com/michelpessoa/fabrica-central-teste/blob/main/docs/COBAIA/03-spec/SPEC-COBAIA-0002.md"
consumption_instructions: "Leia a SDD inteira antes de implementar. Não implemente se o status não for approved."
sizing: medium
supersedes: null
superseded_by: null
tags: [fabrica-descoberta]
---

# Histórico de movimentações de estoque e consultas de saldo calculadas a partir dele

## Resumo executivo

Cria estoque/movimentacoes.py com registrar_entrada, registrar_saida e saldo_por_item sobre um histórico em memória (lista de dicts passada por quem chama) e faz saldo_total, itens_zerados e itens_com_saldo calcularem o saldo a partir desse histórico, com novas assinaturas (historico, nomes). A classe Estoque e os outros módulos não mudam. Desenho e critérios EARS na SPEC-COBAIA-0002.

## Requisitos consolidados

Desenho, decisão e critério EARS na SPEC e na ADR de source_docs, por referência.

| RF-ID | Origem | Requisito (resumo) | Arquivos |
|---|---|---|---|
| RF01 | SPEC-COBAIA-0002 | registrar_entrada(historico, item, quantidade, data) acrescenta {tipo: entrada, item, quantidade, data} ao fim do histórico; ValueError sem alterar para quantidade inválida ou item vazio | `estoque/movimentacoes.py`, `tests/test_movimentacoes.py` |
| RF02 | SPEC-COBAIA-0002 | registrar_saida(historico, item, quantidade, data) acrescenta movimentação de saída; ValueError sem alterar se deixar saldo negativo ou entrada inválida como em RF01 | `estoque/movimentacoes.py`, `tests/test_movimentacoes.py` |
| RF03 | SPEC-COBAIA-0002 | saldo_por_item(historico, ate=None) devolve dict item -> entradas menos saídas, só com data <= ate, ou todas quando ate for None | `estoque/movimentacoes.py`, `tests/test_movimentacoes.py` |
| RF04 | SPEC-COBAIA-0002 | saldo_total(historico, nomes) soma os saldos de saldo_por_item(historico) para os nomes, contando 0 para nome sem movimentação | `estoque/totais.py`, `tests/test_totais.py` |
| RF05 | SPEC-COBAIA-0002 | itens_zerados(historico, nomes) lista, na ordem de nomes, os nomes com saldo calculado 0, contando 0 para nome sem movimentação | `estoque/consultas.py`, `tests/test_consultas.py` |
| RF06 | SPEC-COBAIA-0002 | itens_com_saldo(historico, nomes) lista, na ordem de nomes, os nomes com saldo calculado maior que 0; nome sem movimentação não entra | `estoque/disponiveis.py`, `tests/test_disponiveis.py` |

## Decomposição em tasks

| # | Task | RF(s) de origem | Arquivos tocados | Depende de (#) |
|---|---|---|---|---|
| 1 | Criar estoque/movimentacoes.py com registrar_entrada, registrar_saida e saldo_por_item, e tests/test_movimentacoes.py | RF01, RF02, RF03 | `estoque/movimentacoes.py`, `tests/test_movimentacoes.py` | - |
| 2 | Mudar saldo_total para (historico, nomes) calculando via saldo_por_item e atualizar tests/test_totais.py | RF04 | `estoque/totais.py`, `tests/test_totais.py` | 1 |
| 3 | Mudar itens_zerados para (historico, nomes) calculando via saldo_por_item e atualizar tests/test_consultas.py | RF05 | `estoque/consultas.py`, `tests/test_consultas.py` | 1 |
| 4 | Mudar itens_com_saldo para (historico, nomes) calculando via saldo_por_item e atualizar tests/test_disponiveis.py | RF06 | `estoque/disponiveis.py`, `tests/test_disponiveis.py` | 1 |

## Critérios de aceite / definição de pronto

| # | Critério (origem: RF-ID / contrato) | Comando de verificação | Resultado esperado | Perfil esperado |
|---|---|---|---|---|
| 1 | RF01: registrar_entrada acrescenta o dict correto e recusa quantidade bool, float, 0, negativa e item vazio ou só espaços sem alterar o histórico | `python3 -m unittest tests.test_movimentacoes -v` | exit 0, todos os testes OK | automatizado |
| 2 | RF02: registrar_saida aceita saída até o saldo (saldo 0 quando igual) e recusa saída acima do saldo e entrada inválida sem alterar o histórico | `python3 -m unittest tests.test_movimentacoes -v` | exit 0, todos os testes OK | automatizado |
| 3 | RF03: saldo_por_item devolve entradas menos saídas por item, com e sem ate | `python3 -m unittest tests.test_movimentacoes -v` | exit 0, todos os testes OK | automatizado |
| 4 | RF04: saldo_total soma os saldos calculados do histórico, com 0 para nome sem movimentação | `python3 -m unittest tests.test_totais -v` | exit 0, todos os testes OK | automatizado |
| 5 | RF05: itens_zerados devolve os nomes com saldo 0 na ordem de nomes, incluindo nome sem movimentação | `python3 -m unittest tests.test_consultas -v` | exit 0, todos os testes OK | automatizado |
| 6 | RF06: itens_com_saldo devolve os nomes com saldo maior que 0 na ordem de nomes, sem nome sem movimentação | `python3 -m unittest tests.test_disponiveis -v` | exit 0, todos os testes OK | automatizado |
| 7 | Regressão: build compila pacote e testes sem erro | `python3 -m compileall -q estoque tests` | exit 0, sem erros de compilação | automatizado |
| 8 | Regressão: suíte inteira passa | `python3 -m unittest discover -s tests -v` | exit 0, todos os testes OK | automatizado |

## Instruções específicas para a IA implementadora

Toque só nos arquivos listados. Python 3.10+ e só biblioteca padrão: nenhuma dependência nova (sem pytest, pydantic etc.). Testes com unittest, em tests/test_<modulo>.py, classes unittest.TestCase e métodos test_*. Não alterar a classe Estoque (estoque/itens.py) nem módulos fora dos listados. Sem estado global, singleton ou persistência; o histórico é a lista passada por quem chama. Validar antes do append: em erro, ValueError e histórico intacto. Movimentação com exatamente as chaves tipo, item, quantidade, data. As três consultas chamam saldo_por_item(historico) sem ate e usam .get(nome, 0). Não validar tipo de data nem de item além de vazio/só espaços. Nos testes de totais, consultas e disponiveis, montar o histórico com registrar_entrada/registrar_saida no lugar de Estoque.adicionar.

## Verificação de escopo (nada a mais, nada a menos)

- [x] Todo requisito consolidado acima tem código correspondente.
- [x] Todo arquivo tocado aparece nesta SDD.
- [x] Nenhuma abstração, config, feature flag ou refactor extra.

## Evidência de verificação (preencher antes de status `implemented`)

Verificação independente em `validation-SDD-COBAIA-0013.md`. Veredito: **PASS**.

**Verificador independente:** sim

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

## Rastreabilidade

| Campo | Valor |
|---|---|
| source_docs | SPEC-COBAIA-0002 |
