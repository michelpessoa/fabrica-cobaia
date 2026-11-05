def saldo_total(estoque, nomes):
    return sum(estoque.saldo(nome) for nome in nomes)
