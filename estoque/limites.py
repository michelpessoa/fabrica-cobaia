class Limites:
    def __init__(self):
        self._limites = {}

    def definir_limite(self, nome, limite):
        if limite <= 0:
            raise ValueError("limite deve ser positivo")
        self._limites[nome] = limite

    def pode_retirar(self, nome, quantidade):
        if nome not in self._limites:
            return True
        return quantidade <= self._limites[nome]
