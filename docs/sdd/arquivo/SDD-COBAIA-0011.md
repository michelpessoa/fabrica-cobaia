---
id: SDD-COBAIA-0011
type: SDD
title: "Soma de limites"
status: implemented
project: "COBAIA"
owner: "Michel Pessoa"
created: "2026-11-05"
updated: "2026-11-05"
relates_to: []
source_docs: []
consumption_instructions: "Leia a SDD inteira antes de implementar. Não implemente se o status não for approved."
sizing: medium
supersedes: null
superseded_by: null
tags: [cobaia]
---

# Soma de limites

## Resumo executivo

Soma os limites informados para relatório.

## Decisão(ões) de arquitetura aplicável(is)

Sem ADR: mudança contida neste repositório fictício.

## Requisitos consolidados

| RF-ID | Requisito | Critério de aceite (EARS) | Arquivos |
|---|---|---|---|
| RF01 | Soma | Quando `somar_limites(valores)` for chamado, o sistema deve devolver a soma dos valores. Se a lista for vazia, então deve devolver 0. | `estoque/soma_limites.py`, `tests/test_soma_limites.py` |

## Especificação técnica consolidada

`somar_limites(valores)` é função de `estoque/soma_limites.py` e devolve um inteiro.

## Critérios de aceite / definição de pronto

| # | Critério (origem: RF-ID / contrato) | Comando de verificação | Resultado esperado | Perfil esperado |
|---|---|---|---|---|
| 1 | RF01 | `python3 -m unittest tests.test_soma_limites -v` | exit 0 | automatizado |
| 2 | Regressão | `python3 -m unittest discover -s tests -v` | exit 0 | automatizado |

## Instruções específicas para a IA implementadora

Toque só nos arquivos listados. Testes na classe `TestSomaLimites`.

## Verificação de escopo (nada a mais, nada a menos)

- [x] Todo requisito consolidado acima tem código correspondente.
- [x] Todo arquivo tocado aparece nesta SDD.
- [x] Nenhuma abstração, config, feature flag ou refactor extra.

## Evidência de verificação (preencher antes de status `implemented`)

Verificação independente em `validation-SDD-COBAIA-0011.md`. Veredito: **PASS**.

**Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_soma_limites -v` | Ran 10 tests in 0.000s OK EXIT 0 | Mutação 1: estoque/soma_limites.py:3 trocado por int(sum(valores[1:])) -> FAILED (failures=7). Mutação 2: devolver None para lista vazia -> FAIL test_lista_vazia (failures=1). Restaurado com git checkout, volta para OK. | Sim | tests/test_soma_limites.py:9 | automatizado |
| 2 | `python3 -m unittest discover -s tests -v` | Ran 67 tests in 0.003s OK EXIT 0 | Mutação int(sum(valores[1:])) em estoque/soma_limites.py:3 -> discover FAILED (failures=7); restaurado, volta para OK. | Sim | tests/test_soma_limites.py:20 | automatizado |

## Rastreabilidade

| Campo | Valor |
|---|---|
| source_docs | nenhum |
