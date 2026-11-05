class EstoqueInsuficiente(Exception):
    pass


class Estoque:
    def __init__(self):
        self._saldos = {}

    def adicionar(self, nome, quantidade):
        if quantidade <= 0:
            raise ValueError("quantidade deve ser positiva")
        self._saldos[nome] = self.saldo(nome) + quantidade

    def saldo(self, nome):
        return self._saldos.get(nome, 0)

    def retirar(self, nome, quantidade):
        self._saldos[nome] = self.saldo(nome) - quantidade
