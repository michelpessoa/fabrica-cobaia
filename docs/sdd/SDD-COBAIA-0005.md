---
id: SDD-COBAIA-0005
type: SDD
title: "Saldo total do estoque"
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

- [x] Todo requisito consolidado acima tem código correspondente.
- [x] Todo arquivo tocado aparece nesta SDD.
- [x] Nenhuma abstração, config, feature flag ou refactor extra.

## Evidência de verificação (preencher antes de status `implemented`)

Verificação independente em `validation-SDD-COBAIA-0005.md`. Veredito: **PASS**.

**Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_totais -v` | Ran 6 tests in 0.000s OK EXIT 0 | Mutação 1 (RF01): somar só nomes[:1] em estoque/totais.py:2 -> FAILED (failures=2). Mutação 2 (RF02): retornar 1 para lista vazia -> FAILED (failures=1, test_lista_vazia). Restaurado com git checkout; volta a OK. | Sim | tests/test_totais.py:15 | automatizado |
| 2 | `python3 -m unittest discover -s tests -v` | Ran 14 tests in 0.000s OK EXIT 0 | Com a mutação de RF02 (retornar 1 para lista vazia), a suíte completa resultou em FAILED (failures=1); restaurado com git checkout -- estoque/totais.py, a suíte volta a OK (14 testes). | Sim | tests/test_totais.py:27 | automatizado |

## Rastreabilidade

| Campo | Valor |
|---|---|
| source_docs | nenhum (sizing small) |
