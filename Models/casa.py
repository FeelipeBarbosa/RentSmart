
from Models.Imovel import Imovel

class Casa(Imovel):
    def __init__(self, quartos, possui_garagem):
        super().__init__("Casa", 900.00)

        self.quartos = quartos
        self.possui_garagem = possui_garagem

    def calcular_aluguel(self):
        valor = self.valor_base

        # Adicional para casa com dois quartos
        if self.quartos == 2:
            valor += 250.00

        # Adicional para vaga de garagem
        if self.possui_garagem:
            valor += 300.00

        return round(valor, 2)

    def apresentar_informacoes(self):
        informacoes = super().apresentar_informacoes()

        informacoes.update({
            "quartos": self.quartos,
            "possui_garagem": self.possui_garagem,
            "valor_final": self.calcular_aluguel()
        })

        return informacoes
