---
id: SDD-COBAIA-0008
type: SDD
title: "Limite de retirada por item"
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

# Limite de retirada por item

## Resumo executivo

Impede retirada acima do limite configurado para o item.

## Decisão(ões) de arquitetura aplicável(is)

Sem ADR: mudança contida neste repositório fictício.

## Requisitos consolidados

| RF-ID | Requisito | Critério de aceite (EARS) | Arquivos |
|---|---|---|---|
| RF01 | Definir limite | Quando `definir_limite(nome, limite)` for chamado com limite positivo, o sistema deve guardar o limite do item. Se o limite não for positivo, então deve lançar `ValueError`. | `estoque/limites.py`, `tests/test_limites.py` |
| RF02 | Respeitar limite | Quando `pode_retirar(nome, quantidade)` for chamado, o sistema deve devolver True se o item não tiver limite ou se a quantidade for até o limite, e False caso contrário. | `estoque/limites.py`, `tests/test_limites.py` |

## Especificação técnica consolidada

`Limites` é classe de `estoque/limites.py`, com os métodos `definir_limite` e `pode_retirar`.

## Critérios de aceite / definição de pronto

| # | Critério (origem: RF-ID / contrato) | Comando de verificação | Resultado esperado | Perfil esperado |
|---|---|---|---|---|
| 1 | RF01 e RF02 | `python3 -m unittest tests.test_limites -v` | exit 0 | automatizado |
| 2 | Regressão | `python3 -m unittest discover -s tests -v` | exit 0 | automatizado |

## Instruções específicas para a IA implementadora

Toque só nos arquivos listados. Testes na classe `TestLimites`.

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
