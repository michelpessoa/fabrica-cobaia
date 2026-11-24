from estoque.movimentacoes import saldo_por_item


def saldo_total(historico, nomes):
    saldos = saldo_por_item(historico)
    return sum(saldos.get(nome, 0) for nome in nomes)
