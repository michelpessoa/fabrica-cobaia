def itens_com_saldo(estoque, nomes):
    return [nome for nome in nomes if estoque.saldo(nome) > 0]
