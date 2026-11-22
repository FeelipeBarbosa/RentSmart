
class Orcamento:
    TAXA_CONTRATUAL = 2000.00
    MAX_PARCELAS = 5

    def __init__(self, imovel, parcelas_contrato):
        self.imovel = imovel
        self.parcelas_contrato = parcelas_contrato

        if not isinstance(parcelas_contrato, int):
            raise ValueError("Informe um número inteiro de parcelas.")

        if parcelas_contrato < 1 or parcelas_contrato > self.MAX_PARCELAS:
            raise ValueError("A taxa contratual pode ser dividida em até 5 parcelas.")

    def calcular_aluguel_mensal(self):
        return self.imovel.calcular_aluguel()

    def calcular_parcela_contrato(self):
        return round(
            self.TAXA_CONTRATUAL / self.parcelas_contrato, 2
        )

    def calcular_resumo(self):
        aluguel = self.calcular_aluguel_mensal()
        parcela = self.calcular_parcela_contrato()

        return {
            "imovel": self.imovel.apresentar_informacoes(),
            "aluguel_mensal": aluguel,
            "taxa_contratual": self.TAXA_CONTRATUAL,
            "quantidade_parcelas": self.parcelas_contrato,
            "valor_parcela": parcela,
            "primeiro_pagamento": round(aluguel + parcela, 2)
        }

    def apresentar_orcamento(self):
        resumo = self.calcular_resumo()

        print("\n========== RENTSMART ==========")
        print("       RESUMO DO ORÇAMENTO")
        print("===============================")

        print(f"Tipo de imóvel: {resumo['imovel']['tipo']}")
        print(f"Aluguel mensal: R$ {resumo['aluguel_mensal']:.2f}")

        print("\n--- TAXA CONTRATUAL ---")
        print(f"Valor total: R$ {resumo['taxa_contratual']:.2f}")
        print(f"Parcelas: {resumo['quantidade_parcelas']}")
        print(f"Valor por parcela: R$ {resumo['valor_parcela']:.2f}")

        print("\n--- PRIMEIRO PAGAMENTO ---")
        print(f"Aluguel + parcela: R$ {resumo['primeiro_pagamento']:.2f}")

        print("===============================")

        return resumo
