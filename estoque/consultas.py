from estoque.movimentacoes import saldo_por_item


def itens_zerados(historico, nomes):
    saldos = saldo_por_item(historico)
    return [nome for nome in nomes if saldos.get(nome, 0) == 0]
