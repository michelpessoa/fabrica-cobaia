---
id: SDD-COBAIA-0005
type: SDD
title: "Saldo total do estoque"
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

# Saldo total do estoque

## Resumo executivo

Soma os saldos dos itens informados.

## Decisão(ões) de arquitetura aplicável(is)

Sem ADR: sizing `small`.

## Requisitos consolidados

| RF-ID | Requisito | Critério de aceite (EARS) | Arquivos |
|---|---|---|---|
| RF01 | Saldo total | Quando `saldo_total(estoque, nomes)` for chamado, o sistema deve devolver a soma dos saldos dos nomes informados. | `estoque/totais.py`, `tests/test_totais.py` |
| RF02 | Lista vazia | Se `nomes` for vazio, então o sistema deve devolver 0. | `estoque/totais.py`, `tests/test_totais.py` |

## Especificação técnica consolidada

`saldo_total(estoque, nomes)` é função de `estoque/totais.py` e devolve um inteiro.

## Critérios de aceite / definição de pronto

| # | Critério (origem: RF-ID / contrato) | Comando de verificação | Resultado esperado | Perfil esperado |
|---|---|---|---|---|
| 1 | RF01 e RF02: soma os saldos e devolve 0 para lista vazia | `python3 -m unittest tests.test_totais -v` | exit 0 | automatizado |
| 2 | Regressão | `python3 -m unittest discover -s tests -v` | exit 0 | automatizado |

## Instruções específicas para a IA implementadora

Toque só nos arquivos listados. Testes na classe `TestSaldoTotal`.

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
