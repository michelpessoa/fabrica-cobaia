---
id: SDD-COBAIA-0004
type: SDD
title: "Consulta de itens zerados"
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

- [x] Todo requisito consolidado acima tem código correspondente.
- [x] Todo arquivo tocado aparece nesta SDD.
- [x] Nenhuma abstração, config, feature flag ou refactor extra.

## Evidência de verificação (preencher antes de status `implemented`)

Verificação independente em `validation-SDD-COBAIA-0004.md`. Veredito: **PASS**.

**Verificador independente:** sim

| # | Comando rodado | Saída (resumo) | Sensor | Passou? | Assertion (file:line) | Perfil usado |
|---|---|---|---|---|---|---|
| 1 | `python3 -m unittest tests.test_consultas -v` | Ran 6 tests in 0.000s OK (exit 0): test_devolve_lista, test_devolve_so_zerados_na_ordem_recebida, test_item_desconhecido_tem_saldo_zero, test_lista_vazia, test_nenhum_zerado, test_saldo_um_nao_e_zerado | Mutação 1: '== 0' trocado por '!= 0' em estoque/consultas.py:2 -> FAILED (failures=4). Mutação 2: iteração em reversed(list(nomes)) -> FAILED (failures=1). Mutação 3: filtro removido -> FAILED (failures=3). Depois do git checkout, volta a OK. | Sim | tests/test_consultas.py:12 | automatizado |
| 2 | `python3 -m unittest discover -s tests -v` | Ran 8 tests in 0.000s OK (exit 0): os 6 de TestItensZerados mais test_itens.TestAdicionar (test_recusa_quantidade_nao_positiva, test_soma_ao_saldo) | Mutação em estoque/itens.py:6 ('<= 0' trocado por '< 0') -> FAILED (failures=1). Mutação de consultas.py com '!= 0' também faz a suíte falhar. Depois do git checkout, volta a OK. | Sim | tests/test_itens.py:14 | automatizado |

## Rastreabilidade

| Campo | Valor |
|---|---|
| source_docs | nenhum (sizing small) |
