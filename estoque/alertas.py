def itens_em_alerta(estoque, itens):
    return [item for item in itens if estoque.saldo(item) < 10]
