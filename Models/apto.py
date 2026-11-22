
from Models.Imovel import Imovel


class Apartamento(Imovel):
    def __init__(self, quartos, possui_garagem, possui_criancas):
        super().__init__("Apartamento", 700.00)

        self.quartos = quartos
        self.possui_garagem = possui_garagem
        self.possui_criancas = possui_criancas

    def calcular_aluguel(self):
        valor = self.valor_base

        # Adicional para apartamento com dois quartos
        if self.quartos == 2:
            valor += 200.00

        # Adicional para vaga de garagem
        if self.possui_garagem:
            valor += 300.00

        # Desconto de 5% para clientes sem crianças
        if not self.possui_criancas:
            valor -= valor * 0.05

        return round(valor, 2)

    def apresentar_informacoes(self):
        informacoes = super().apresentar_informacoes()

        informacoes.update({
            "quartos": self.quartos,
            "possui_garagem": self.possui_garagem,
            "possui_criancas": self.possui_criancas,
            "valor_final": self.calcular_aluguel()
        })

        return informacoes
