
import tkinter as tk
from tkinter import ttk, messagebox

from Models.apto import Apartamento
from Models.casa import Casa
from Models.estudio import Estudio

from service.orcamento import Orcamento
from service.gerador_csv import GeradorCSV

from ui.componentes import CORES, FONTES, criar_botao


class TelaOrcamento:

    def __init__(self, janela):
        self.janela = janela

        self.tela = tk.Toplevel(janela)
        self.tela.title("RentSmart | Novo Orçamento")
        self.tela.geometry("850x700")
        self.tela.minsize(750, 600)
        self.tela.configure(bg=CORES["fundo"])

        self.orcamento_atual = None

        self.criar_interface()

    def criar_interface(self):

        # CABEÇALHO
        cabecalho = tk.Frame(
            self.tela,
            bg=CORES["azul_escuro"],
            height=85
        )

        cabecalho.pack(fill="x")
        cabecalho.pack_propagate(False)

        tk.Label(
            cabecalho,
            text="Novo orçamento",
            font=("Segoe UI", 20, "bold"),
            bg=CORES["azul_escuro"],
            fg=CORES["branco"]
        ).pack(anchor="w", padx=30, pady=(15, 0))

        tk.Label(
            cabecalho,
            text="Preencha os dados da locação para calcular o orçamento.",
            font=FONTES["normal"],
            bg=CORES["azul_escuro"],
            fg="#DCE9F6"
        ).pack(anchor="w", padx=30)

        # ÁREA DO FORMULÁRIO
        container = tk.Frame(
            self.tela,
            bg=CORES["fundo"]
        )

        container.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=25
        )

        # TIPO DE IMÓVEL
        self.criar_rotulo(container, "Tipo de imóvel")

        self.tipo_var = tk.StringVar(value="Apartamento")

        self.tipo_combo = ttk.Combobox(
            container,
            textvariable=self.tipo_var,
            values=["Apartamento", "Casa", "Estúdio"],
            state="readonly",
            font=FONTES["normal"],
            width=35
        )

        self.tipo_combo.pack(anchor="w", pady=(5, 18))
        self.tipo_combo.bind(
            "<<ComboboxSelected>>",
            self.atualizar_campos
        )

        # ÁREA DINÂMICA
        self.campos_dinamicos = tk.Frame(
            container,
            bg=CORES["fundo"]
        )

        self.campos_dinamicos.pack(
            fill="x",
            anchor="w"
        )

        self.atualizar_campos()

        # PARCELAMENTO
        self.criar_rotulo(
            container,
            "Parcelamento da taxa contratual"
        )

        self.parcelas_var = tk.StringVar(value="1")

        self.parcelas_combo = ttk.Combobox(
            container,
            textvariable=self.parcelas_var,
            values=["1", "2", "3", "4", "5"],
            state="readonly",
            font=FONTES["normal"],
            width=35
        )

        self.parcelas_combo.pack(
            anchor="w",
            pady=(5, 20)
        )

        tk.Label(
            container,
            text="Taxa contratual: R$ 2.000,00",
            font=("Segoe UI", 10, "bold"),
            bg=CORES["fundo"],
            fg=CORES["azul_escuro"]
        ).pack(anchor="w", pady=(0, 20))

        # BOTÕES
        botoes = tk.Frame(
            container,
            bg=CORES["fundo"]
        )

        botoes.pack(anchor="w")

        criar_botao(
            botoes,
            "Calcular orçamento",
            self.calcular_orcamento
        ).pack(side="left", padx=(0, 10))

        criar_botao(
            botoes,
            "Fechar",
            self.tela.destroy,
            cor=CORES["cinza"]
        ).pack(side="left")

    def criar_rotulo(self, pai, texto):

        tk.Label(
            pai,
            text=texto,
            font=FONTES["subtitulo"],
            bg=CORES["fundo"],
            fg=CORES["texto"]
        ).pack(anchor="w", pady=(5, 0))

    def atualizar_campos(self, evento=None):

        for widget in self.campos_dinamicos.winfo_children():
            widget.destroy()

        tipo = self.tipo_var.get()

        if tipo == "Apartamento" or tipo == "Casa":

            self.criar_rotulo(
                self.campos_dinamicos,
                "Quantidade de quartos"
            )

            self.quartos_var = tk.StringVar(value="1")

            ttk.Combobox(
                self.campos_dinamicos,
                textvariable=self.quartos_var,
                values=["1", "2"],
                state="readonly",
                font=FONTES["normal"],
                width=35
            ).pack(anchor="w", pady=(5, 15))

            self.criar_rotulo(
                self.campos_dinamicos,
                "Possui vaga de garagem?"
            )

            self.garagem_var = tk.StringVar(value="Não")

            ttk.Combobox(
                self.campos_dinamicos,
                textvariable=self.garagem_var,
                values=["Sim", "Não"],
                state="readonly",
                font=FONTES["normal"],
                width=35
            ).pack(anchor="w", pady=(5, 15))

            if tipo == "Apartamento":

                self.criar_rotulo(
                    self.campos_dinamicos,
                    "Possui crianças?"
                )

                self.criancas_var = tk.StringVar(value="Não")

                ttk.Combobox(
                    self.campos_dinamicos,
                    textvariable=self.criancas_var,
                    values=["Sim", "Não"],
                    state="readonly",
                    font=FONTES["normal"],
                    width=35
                ).pack(anchor="w", pady=(5, 15))

        elif tipo == "Estúdio":

            self.criar_rotulo(
                self.campos_dinamicos,
                "Quantidade de vagas de estacionamento"
            )

            self.vagas_var = tk.StringVar(value="2")

            ttk.Spinbox(
                self.campos_dinamicos,
                from_=2,
                to=20,
                textvariable=self.vagas_var,
                state="readonly",
                font=FONTES["normal"],
                width=35
            ).pack(anchor="w", pady=(5, 15))

            tk.Label(
                self.campos_dinamicos,
                text="O pacote inicial inclui duas vagas por R$ 250,00.",
                font=FONTES["normal"],
                bg=CORES["fundo"],
                fg=CORES["cinza"]
            ).pack(anchor="w", pady=(0, 10))

    def calcular_orcamento(self):

        try:
            tipo = self.tipo_var.get()

            if tipo == "Apartamento":

                imovel = Apartamento(
                    quartos=int(self.quartos_var.get()),
                    possui_garagem=self.garagem_var.get() == "Sim",
                    possui_criancas=self.criancas_var.get() == "Sim"
                )

            elif tipo == "Casa":

                imovel = Casa(
                    quartos=int(self.quartos_var.get()),
                    possui_garagem=self.garagem_var.get() == "Sim"
                )

            else:

                imovel = Estudio(
                    vagas=int(self.vagas_var.get())
                )

            parcelas = int(self.parcelas_var.get())

            self.orcamento_atual = Orcamento(
                imovel,
                parcelas
            )

            self.mostrar_resultado()

        except (ValueError, TypeError) as erro:

            messagebox.showerror(
                "Dados inválidos",
                str(erro),
                parent=self.tela
            )

    def mostrar_resultado(self):

        resumo = self.orcamento_atual.calcular_resumo()

        janela_resultado = tk.Toplevel(self.tela)
        janela_resultado.title("RentSmart | Resultado")
        janela_resultado.geometry("520x570")
        janela_resultado.configure(bg=CORES["fundo"])
        janela_resultado.resizable(False, False)

        container = tk.Frame(
            janela_resultado,
            bg=CORES["branco"],
            padx=30,
            pady=25
        )

        container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        tk.Label(
            container,
            text="Orçamento calculado!",
            font=("Segoe UI", 20, "bold"),
            bg=CORES["branco"],
            fg=CORES["azul_escuro"]
        ).pack(anchor="w", pady=(0, 10))

        tk.Label(
            container,
            text=f"Imóvel: {resumo['imovel']['tipo']}",
            font=FONTES["normal"],
            bg=CORES["branco"],
            fg=CORES["texto"]
        ).pack(anchor="w", pady=5)

        tk.Label(
            container,
            text="RESUMO FINANCEIRO",
            font=FONTES["subtitulo"],
            bg=CORES["branco"],
            fg=CORES["azul"]
        ).pack(anchor="w", pady=(20, 10))

        self.criar_linha(
            container,
            "Aluguel mensal",
            resumo["aluguel_mensal"]
        )

        self.criar_linha(
            container,
            "Taxa contratual",
            resumo["taxa_contratual"]
        )

        self.criar_linha(
            container,
            "Quantidade de parcelas",
            resumo["quantidade_parcelas"],
            moeda=False
        )

        self.criar_linha(
            container,
            "Valor de cada parcela",
            resumo["valor_parcela"]
        )

        tk.Frame(
            container,
            bg="#E2E8F0",
            height=1
        ).pack(fill="x", pady=15)

        tk.Label(
            container,
            text="PRIMEIRO PAGAMENTO",
            font=FONTES["subtitulo"],
            bg=CORES["branco"],
            fg=CORES["cinza"]
        ).pack(anchor="w")

        tk.Label(
            container,
            text=f"R$ {resumo['primeiro_pagamento']:,.2f}".replace(
                ",", "X"
            ).replace(".", ",").replace("X", "."),
            font=("Segoe UI", 25, "bold"),
            bg=CORES["branco"],
            fg=CORES["verde"]
        ).pack(anchor="w", pady=10)

        criar_botao(
            container,
            "Gerar projeção CSV",
            lambda: self.exportar_csv(janela_resultado)
        ).pack(fill="x", pady=(15, 8))

        criar_botao(
            container,
            "Fechar resultado",
            janela_resultado.destroy,
            cor=CORES["cinza"]
        ).pack(fill="x")

    def criar_linha(self, pai, descricao, valor, moeda=True):

        linha = tk.Frame(
            pai,
            bg=CORES["branco"]
        )

        linha.pack(fill="x", pady=6)

        tk.Label(
            linha,
            text=descricao,
            font=FONTES["normal"],
            bg=CORES["branco"],
            fg=CORES["texto"]
        ).pack(side="left")

        if moeda:
            valor_formatado = (
                f"R$ {valor:,.2f}"
                .replace(",", "X")
                .replace(".", ",")
                .replace("X", ".")
            )
        else:
            valor_formatado = str(valor)

        tk.Label(
            linha,
            text=valor_formatado,
            font=("Segoe UI", 10, "bold"),
            bg=CORES["branco"],
            fg=CORES["texto"]
        ).pack(side="right")

    def exportar_csv(self, janela_resultado):

        try:

            gerador = GeradorCSV(self.orcamento_atual)

            caminho = gerador.gerar_projecao()

            messagebox.showinfo(
                "RentSmart",
                f"Projeção gerada com sucesso!\n\nArquivo: {caminho}",
                parent=janela_resultado
            )

        except (OSError, ValueError) as erro:

            messagebox.showerror(
                "Erro ao gerar CSV",
                str(erro),
                parent=janela_resultado
            )
