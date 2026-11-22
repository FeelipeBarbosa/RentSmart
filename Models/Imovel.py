class Imovel:
    def __init__(self, tipo, valor_base):
        self.tipo = tipo
        self.valor_base = valor_base

    def calcular_aluguel(self):
        return self.valor_base

    def apresentar_informacoes(self):
        return {
            "tipo": self.tipo,
            "valor_base": self.valor_base
        }
