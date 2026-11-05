import hmac


def token_valido(recebido, esperado):
    if not recebido or not esperado:
        return False
    return hmac.compare_digest(recebido, esperado)
