
import csv
import os


class GeradorCSV:

    def __init__(self, orcamento):
        self.orcamento = orcamento

    def gerar_projecao(self):
        resumo = self.orcamento.calcular_resumo()

        aluguel = resumo["aluguel_mensal"]
        quantidade_parcelas = resumo["quantidade_parcelas"]

        taxa_centavos = 200000
        parcela_base = taxa_centavos // quantidade_parcelas
        resto = taxa_centavos % quantidade_parcelas

        # Criar a pasta de relatórios, caso não exista
        os.makedirs("relatorios", exist_ok=True)

        caminho_arquivo = os.path.join(
            "relatorios",
            "projecao_locacao.csv"
        )

        with open(
            caminho_arquivo,
            mode="w",
            newline="",
            encoding="utf-8-sig"
        ) as arquivo:

            colunas = [
                "Mes",
                "Aluguel Mensal",
                "Parcela Contratual",
                "Total Previsto"
            ]

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=colunas,
                delimiter=";"
            )

            escritor.writeheader()

            for mes in range(1, 13):

                if mes <= quantidade_parcelas:
                    parcela_centavos = parcela_base

                    if mes <= resto:
                        parcela_centavos += 1
                else:
                    parcela_centavos = 0

                parcela = parcela_centavos / 100

                total = round(aluguel + parcela, 2)

                escritor.writerow({
                    "Mes": f"{mes}º mês",
                    "Aluguel Mensal": f"{aluguel:.2f}",
                    "Parcela Contratual": f"{parcela:.2f}",
                    "Total Previsto": f"{total:.2f}"
                })

        print("\nArquivo CSV gerado com sucesso!")
        print(f"Local: {caminho_arquivo}")

        return caminho_arquivo
