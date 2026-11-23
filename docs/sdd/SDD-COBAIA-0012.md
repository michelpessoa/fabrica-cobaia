---
id: SDD-COBAIA-0012
type: SDD
title: "Mínimos de estoque com reposição sugerida e persistência em JSON"
status: approved
approved_by:
  kind: policy
  actor: fabrica-agentica
  at: "2026-11-23T11:29:25Z"
  content_sha256: "6568f90d762f8d26f6382568c073079fef606308b233172ee43c770f194ee60b"
  transitions:
    - {from: draft, to: in_review, at: "2026-11-23T11:29:25Z"}
    - {from: in_review, to: approved, at: "2026-11-23T11:29:25Z"}
project: "COBAIA"
owner: "Michel Pessoa"
created: "2026-11-23"
updated: "2026-11-23"
relates_to: []
source_docs:
  - id: "SPEC-COBAIA-0001"
    url: "https://github.com/michelpessoa/fabrica-central-teste/blob/main/docs/COBAIA/03-spec/SPEC-COBAIA-0001.md"
consumption_instructions: "Leia a SDD inteira antes de implementar. Não implemente se o status não for approved."
sizing: medium
supersedes: null
superseded_by: null
tags: [fabrica-descoberta]
---

# Mínimos de estoque com reposição sugerida e persistência em JSON

## Resumo executivo

Biblioteca em Python 3, só com a biblioteca padrão, no pacote estoque/. Traz a classe Minimos, que guarda um mínimo e uma margem por item, e três funções: itens_abaixo_do_minimo, que lista os itens abaixo do mínimo ordenados pela falta; sugerir_reposicao, que sugere quanto repor até o mínimo mais a margem; e salvar_minimos/carregar_minimos, que salvam e carregam a configuração em JSON. O saldo vem de Estoque.saldo(nome). O desenho e os critérios EARS estão na SPEC-COBAIA-0001.

## Requisitos consolidados

Desenho, decisão e critério EARS na SPEC e na ADR de source_docs, por referência.

| RF-ID | Origem | Requisito (resumo) | Arquivos |
|---|---|---|---|
| RF01 | SPEC-COBAIA-0001 | Classe Minimos com definir_minimo, minimo, definir_margem e margem; mínimo <= 0 e margem < 0 lançam ValueError com a mensagem da SPEC; a leitura devolve None se o valor não foi definido. | `estoque/minimos.py`, `tests/test_minimos.py` |
| RF02 | SPEC-COBAIA-0001 | itens_abaixo_do_minimo(estoque, minimos, nomes) em estoque/consultas.py devolve [(nome, falta)] para saldo < minimo, ordenada por (-falta, nome); itens sem mínimo ficam de fora. | `estoque/consultas.py`, `tests/test_consultas.py` |
| RF03 | SPEC-COBAIA-0001 | sugerir_reposicao(estoque, minimos, nomes) devolve {nome: minimo + margem - saldo} (margem 0 se ausente) só para itens com mínimo e saldo < minimo; sem itens, {}. | `estoque/reposicao_sugerida.py`, `tests/test_reposicao_sugerida.py` |
| RF04 | SPEC-COBAIA-0001 | salvar_minimos grava JSON UTF-8 com sort_keys, só itens com mínimo e margem omitida se ausente; carregar_minimos devolve Minimos novo e lança ValueError se faltar minimo. | `estoque/persistencia_minimos.py`, `tests/test_persistencia_minimos.py` |

## Decomposição em tasks

| # | Task | RF(s) de origem | Arquivos tocados | Depende de (#) |
|---|---|---|---|---|
| 1 | Criar a classe Minimos em estoque/minimos.py e os testes dela | RF01 | `estoque/minimos.py`, `tests/test_minimos.py` | - |
| 2 | Acrescentar itens_abaixo_do_minimo em estoque/consultas.py e estender tests/test_consultas.py | RF02 | `estoque/consultas.py`, `tests/test_consultas.py` | 1 |
| 3 | Criar sugerir_reposicao em estoque/reposicao_sugerida.py e os testes dela | RF03 | `estoque/reposicao_sugerida.py`, `tests/test_reposicao_sugerida.py` | 1 |
| 4 | Criar salvar_minimos e carregar_minimos em estoque/persistencia_minimos.py e os testes delas | RF04 | `estoque/persistencia_minimos.py`, `tests/test_persistencia_minimos.py` | 1 |

## Critérios de aceite / definição de pronto

| # | Critério (origem: RF-ID / contrato) | Comando de verificação | Resultado esperado | Perfil esperado |
|---|---|---|---|---|
| 1 | RF01: testes de Minimos (definir, ler, None, ValueError e mensagens, margem 0 aceita) | `python3 -m unittest tests.test_minimos -v` | Todos os testes passam, exit 0 | automatizado |
| 2 | RF02: testes de itens_abaixo_do_minimo em tests/test_consultas.py | `python3 -m unittest tests.test_consultas -v` | Todos os testes passam, incluindo os de itens_zerados que já existem, exit 0 | automatizado |
| 3 | RF03: testes de sugerir_reposicao | `python3 -m unittest tests.test_reposicao_sugerida -v` | Todos os testes passam, exit 0 | automatizado |
| 4 | RF04: testes de salvar_minimos e carregar_minimos com tempfile | `python3 -m unittest tests.test_persistencia_minimos -v` | Todos os testes passam, exit 0 | automatizado |
| 5 | Regressão: suíte inteira, incluindo Estoque, Limites e itens_zerados | `python3 -m unittest discover -s tests -v` | Todos os testes passam, exit 0 | automatizado |

## Instruções específicas para a IA implementadora

Toque só nos arquivos listados. Use só a biblioteca padrão do Python 3 (json, tempfile, unittest). Não adicione dependências. Não crie CLI, banco ou outra interface. Não altere Estoque, Limites nem itens_zerados. Estenda o tests/test_consultas.py que já existe e não crie tests/test_consultas_minimos.py. Os testes usam unittest em tests/test_*.py. Não cheque tipos e não converta FileNotFoundError nem json.JSONDecodeError em outro erro. As mensagens de ValueError têm que ser exatamente as da SPEC-COBAIA-0001. Siga o padrão de estoque/limites.py e estoque/consultas.py.

## Verificação de escopo (nada a mais, nada a menos)

- [ ] Todo requisito consolidado acima tem código correspondente.
- [ ] Todo arquivo tocado aparece nesta SDD.
- [ ] Nenhuma abstração, config, feature flag ou refactor extra.

## Evidência de verificação (preencher antes de status `implemented`)

**Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|

## Rastreabilidade

| Campo | Valor |
|---|---|
| source_docs | SPEC-COBAIA-0001 |
