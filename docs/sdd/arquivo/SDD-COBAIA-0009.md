---
id: SDD-COBAIA-0009
type: SDD
title: "Validar token de reposição"
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

# Validar token de reposição

## Resumo executivo

Confere o token que autoriza um pedido de reposição fictício.

## Decisão(ões) de arquitetura aplicável(is)

Sem ADR: mudança contida neste repositório fictício.

## Requisitos consolidados

| RF-ID | Requisito | Critério de aceite (EARS) | Arquivos |
|---|---|---|---|
| RF01 | Validar token | Quando `token_valido(recebido, esperado)` for chamado, o sistema deve devolver True só se os dois forem iguais, comparando em tempo constante. Se algum for vazio, então deve devolver False. | `estoque/reposicao.py`, `tests/test_reposicao.py` |

## Especificação técnica consolidada

`token_valido(recebido, esperado)` é função de `estoque/reposicao.py` e usa `hmac.compare_digest`.

## Critérios de aceite / definição de pronto

| # | Critério (origem: RF-ID / contrato) | Comando de verificação | Resultado esperado | Perfil esperado |
|---|---|---|---|---|
| 1 | RF01 | `python3 -m unittest tests.test_reposicao -v` | exit 0 | automatizado |
| 2 | Regressão | `python3 -m unittest discover -s tests -v` | exit 0 | automatizado |

## Instruções específicas para a IA implementadora

Toque só nos arquivos listados. Testes na classe `TestToken`.

## Verificação de escopo (nada a mais, nada a menos)

- [x] Todo requisito consolidado acima tem código correspondente.
- [x] Todo arquivo tocado aparece nesta SDD.
- [x] Nenhuma abstração, config, feature flag ou refactor extra.

## Evidência de verificação (preencher antes de status `implemented`)

Verificação independente em `validation-SDD-COBAIA-0009.md`. Veredito: **PASS**.

**Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_reposicao -v` | Ran 12 tests in 0.001s OK (exit 0) | Mutações em estoque/reposicao.py: 'or'->'and' na checagem de vazio => FAILED (failures=1); remover checagem de vazio (if False) => FAILED (failures=2); trocar compare_digest por '==' => FAILED (failures=2); negar compare_digest => FAILED (failures=7). Restaurado com git checkout, volta a OK. | Sim | tests/test_reposicao.py:9 | automatizado |
| 2 | `python3 -m unittest discover -s tests -v` | Ran 57 tests in 0.003s OK (exit 0) | Regressão: a suíte inclui tests/test_reposicao.py, que falhou sob as mesmas mutações do critério 1; restaurado e verde. | Sim | tests/test_reposicao.py:9 | automatizado |

## Rastreabilidade

| Campo | Valor |
|---|---|
| source_docs | nenhum |
