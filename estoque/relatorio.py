def relatorio_csv(estoque, itens):
    return "\n".join(f"{item},{estoque.saldo(item)}" for item in itens)
