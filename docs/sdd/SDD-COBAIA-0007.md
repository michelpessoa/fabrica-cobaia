---
id: SDD-COBAIA-0007
type: SDD
title: "Itens com saldo"
status: implemented
project: "COBAIA"
owner: "Michel Pessoa"
created: "2026-11-05"
updated: "2026-11-05"
relates_to: []
source_docs: []
consumption_instructions: "Leia a SDD inteira antes de implementar. Não implemente se o status não for approved."
sizing: small
supersedes: null
superseded_by: null
tags: [cobaia]
---

# Itens com saldo

## Resumo executivo

Lista os itens que têm saldo.

## Decisão(ões) de arquitetura aplicável(is)

Sem ADR: sizing `small`.

## Requisitos consolidados

| RF-ID | Requisito | Critério de aceite (EARS) | Arquivos |
|---|---|---|---|
| RF01 | Itens com saldo | Quando `itens_com_saldo(estoque, nomes)` for chamado, o sistema deve devolver, na ordem recebida, os nomes com saldo maior que zero. | `estoque/disponiveis.py`, `tests/test_disponiveis.py` |

## Especificação técnica consolidada

`itens_com_saldo(estoque, nomes)` é função de `estoque/disponiveis.py` e devolve uma lista.

## Critérios de aceite / definição de pronto

| # | Critério (origem: RF-ID / contrato) | Comando de verificação | Resultado esperado | Perfil esperado |
|---|---|---|---|---|
| 1 | RF01: devolve só os itens com saldo, na ordem recebida | `python3 -m unittest tests.test_disponiveis -v` | exit 0 | automatizado |

## Instruções específicas para a IA implementadora

Toque só nos arquivos listados. Testes na classe `TestItensComSaldo`.

## Verificação de escopo (nada a mais, nada a menos)

- [x] Todo requisito consolidado acima tem código correspondente.
- [x] Todo arquivo tocado aparece nesta SDD.
- [x] Nenhuma abstração, config, feature flag ou refactor extra.

## Evidência de verificação (preencher antes de status `implemented`)

Verificação independente em `validation-SDD-COBAIA-0007.md`. Veredito: **PASS**.

**Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_disponiveis -v` | Ran 6 tests in 0.000s OK (exit 0): test_devolve_lista, test_devolve_so_com_saldo_na_ordem_recebida, test_item_desconhecido_sem_saldo, test_lista_vazia, test_ordem_recebida_nao_alfabetica, test_saldo_um_conta, todos ok | Três mutações em estoque/disponiveis.py:2. (a) '> 0' trocado por '>= 0': FAILED (failures=3). (b) resultado passado por sorted() no lugar da ordem recebida: FAILED (failures=2). (c) filtro de saldo removido: FAILED (failures=3). Depois de cada uma, restaurei com git checkout -- estoque/disponiveis.py. Rodei de novo: OK, e git status ficou limpo. | Sim | tests/test_disponiveis.py:12 | automatizado |

## Rastreabilidade

| Campo | Valor |
|---|---|
| source_docs | nenhum (sizing small) |
