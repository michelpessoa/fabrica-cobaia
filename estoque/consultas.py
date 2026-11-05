def itens_zerados(estoque, nomes):
    return [nome for nome in nomes if estoque.saldo(nome) == 0]
