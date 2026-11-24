def _validar(item, quantidade):
    if not item.strip():
        raise ValueError("item vazio")
    if not isinstance(quantidade, int) or isinstance(quantidade, bool) or quantidade <= 0:
        raise ValueError("quantidade deve ser int > 0")


def registrar_entrada(historico, item, quantidade, data):
    _validar(item, quantidade)
    historico.append({"tipo": "entrada", "item": item, "quantidade": quantidade, "data": data})


def registrar_saida(historico, item, quantidade, data):
    _validar(item, quantidade)
    if quantidade > saldo_por_item(historico).get(item, 0):
        raise ValueError("saldo insuficiente")
    historico.append({"tipo": "saida", "item": item, "quantidade": quantidade, "data": data})


def saldo_por_item(historico, ate=None):
    saldos = {}
    for m in historico:
        if ate is not None and not m["data"] <= ate:
            continue
        sinal = 1 if m["tipo"] == "entrada" else -1
        saldos[m["item"]] = saldos.get(m["item"], 0) + sinal * m["quantidade"]
    return saldos
