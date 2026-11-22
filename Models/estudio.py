from Models.Imovel import Imovel

class Estudio(Imovel):
    def __init__(self, vagas):
        super().__init__("Estúdio", 1200.00)

        if vagas < 2:
            raise ValueError("O estúdio deve possuir pelo menos 2 vagas.")

        self.vagas = vagas

    def calcular_aluguel(self):
        valor = self.valor_base

        # Pacote inicial de duas vagas
        valor += 250.00

        # Adicional para cada vaga acima das duas iniciais
        vagas_extras = self.vagas - 2
        valor += vagas_extras * 60.00

        return round(valor, 2)

    def apresentar_informacoes(self):
        informacoes = super().apresentar_informacoes()

        informacoes.update({
            "vagas": self.vagas,
            "valor_final": self.calcular_aluguel()
        })

        return informacoes
    