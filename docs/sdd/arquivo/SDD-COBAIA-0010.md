---
id: SDD-COBAIA-0010
type: SDD
title: "Nome normalizado de item"
status: implemented
project: "COBAIA"
owner: "Michel Pessoa"
created: "2026-11-05"
updated: "2026-11-05"
relates_to: []
source_docs: []
consumption_instructions: "Leia a SDD inteira antes de implementar. Não implemente se o status não for approved."
supersedes: null
superseded_by: null
tags: [cobaia]
---

# Nome normalizado de item

## Resumo executivo

Normaliza nomes de itens antes da consulta.

## Decisão(ões) de arquitetura aplicável(is)

Sem ADR: mudança contida neste repositório fictício.

## Requisitos consolidados

| RF-ID | Requisito | Critério de aceite (EARS) | Arquivos |
|---|---|---|---|
| RF01 | Normalizar | Quando `normalizar(nome)` for chamado, o sistema deve devolver o nome sem espaços nas pontas e em minúsculas. | `estoque/nomes.py`, `tests/test_nomes.py` |

## Especificação técnica consolidada

`normalizar(nome)` é função de `estoque/nomes.py` e devolve uma string.

## Critérios de aceite / definição de pronto

| # | Critério (origem: RF-ID / contrato) | Comando de verificação | Resultado esperado | Perfil esperado |
|---|---|---|---|---|
| 1 | RF01 | `python3 -m unittest tests.test_nomes -v` | exit 0 | automatizado |
| 2 | Regressão | `python3 -m unittest discover -s tests -v` | exit 0 | automatizado |

## Instruções específicas para a IA implementadora

Toque só nos arquivos listados. Testes na classe `TestNormalizar`.

## Verificação de escopo (nada a mais, nada a menos)

- [x] Todo requisito consolidado acima tem código correspondente.
- [x] Todo arquivo tocado aparece nesta SDD.
- [x] Nenhuma abstração, config, feature flag ou refactor extra.

## Evidência de verificação (preencher antes de status `implemented`)

Verificação independente em `validation-SDD-COBAIA-0010.md`. Veredito: **PASS**.

**Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_nomes -v` | Ran 11 tests in 0.000s OK EXIT=0 | Removido .strip() em estoque/nomes.py:2 -> FAILED (failures=6); removido .lower() -> FAILED (failures=6); restaurado com git checkout, voltou a OK | Sim | tests/test_nomes.py:8 | automatizado |
| 2 | `python3 -m unittest discover -s tests -v` | Ran 45 tests in 0.002s OK EXIT=0 | Mutação em estoque/nomes.py:2 (trunca último caractere do resultado) -> suíte completa FAILED (failures=8); restaurado com git checkout, 45 testes OK | Sim | tests/test_nomes.py:11 | automatizado |

## Rastreabilidade

| Campo | Valor |
|---|---|
| source_docs | nenhum |
