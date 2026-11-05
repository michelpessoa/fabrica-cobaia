---
id: SDD-COBAIA-0004
type: SDD
title: "Consulta de itens zerados"
status: approved
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

# Consulta de itens zerados

## Resumo executivo

Lista os itens sem saldo.

## Decisão(ões) de arquitetura aplicável(is)

Sem ADR: sizing `small`.

## Requisitos consolidados

| RF-ID | Requisito | Critério de aceite (EARS) | Arquivos |
|---|---|---|---|
| RF01 | Itens zerados | Quando `itens_zerados(estoque, nomes)` for chamado, o sistema deve devolver, na ordem recebida, os nomes com saldo igual a zero. | `estoque/consultas.py`, `tests/test_consultas.py` |

## Especificação técnica consolidada

`itens_zerados(estoque, nomes)` é função de `estoque/consultas.py` e devolve uma lista.

## Critérios de aceite / definição de pronto

| # | Critério (origem: RF-ID / contrato) | Comando de verificação | Resultado esperado | Perfil esperado |
|---|---|---|---|---|
| 1 | RF01: devolve só os itens com saldo zero, na ordem recebida | `python3 -m unittest tests.test_consultas -v` | exit 0 | automatizado |
| 2 | Regressão | `python3 -m unittest discover -s tests -v` | exit 0 | automatizado |

## Instruções específicas para a IA implementadora

Toque só nos arquivos listados. Testes na classe `TestItensZerados`.

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
| source_docs | nenhum (sizing small) |
