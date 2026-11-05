---
id: SDD-COBAIA-0011
type: SDD
title: "Soma de limites"
status: approved
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
| source_docs | nenhum |
