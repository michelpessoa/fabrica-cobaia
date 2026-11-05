---
id: SDD-COBAIA-0001
type: SDD
title: "Retirada de itens do estoque"
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

# Retirada de itens do estoque

## Resumo executivo

Permite retirar itens do estoque, recusando retirada maior que o saldo.

## Decisão(ões) de arquitetura aplicável(is)

Sem ADR: sizing `small`.

## Requisitos consolidados

| RF-ID | Requisito | Critério de aceite (EARS) | Arquivos |
|---|---|---|---|
| RF01 | Retirada | Quando `Estoque.retirar(nome, quantidade)` for chamado com quantidade até o saldo, o sistema deve subtrair a quantidade do saldo. | `estoque/itens.py`, `tests/test_retirada.py` |
| RF02 | Saldo insuficiente | Se a quantidade for maior que o saldo, então o sistema deve lançar `EstoqueInsuficiente` e manter o saldo. | `estoque/itens.py`, `tests/test_retirada.py` |

## Especificação técnica consolidada

`EstoqueInsuficiente` é subclasse de `Exception`, definida em `estoque/itens.py`.
`retirar` é método de `Estoque` e não retorna valor.

## Critérios de aceite / definição de pronto

| # | Critério (origem: RF-ID / contrato) | Comando de verificação | Resultado esperado | Perfil esperado |
|---|---|---|---|---|
| 1 | RF01: retirada subtrai do saldo | `python3 -m unittest tests.test_retirada.TestRetirada.test_subtrai_do_saldo -v` | exit 0 | automatizado |
| 2 | RF02: retirada acima do saldo lança erro e mantém o saldo | `python3 -m unittest tests.test_retirada.TestRetirada.test_saldo_insuficiente -v` | exit 0 | automatizado |
| 3 | Regressão | `python3 -m unittest discover -s tests -v` | exit 0 | automatizado |

## Instruções específicas para a IA implementadora

Toque só nos arquivos listados. Sem dependência nova. Testes em `tests/test_retirada.py`,
na classe `TestRetirada`.

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
