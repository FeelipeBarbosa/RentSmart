
import tkinter as tk

from ui.componentes import (
    CORES,
    FONTES,
    criar_titulo,
    criar_subtitulo,
    criar_texto,
    criar_botao
)


class JanelaPrincipal:

    def __init__(self, janela, comando_novo_orcamento):
        self.janela = janela
        self.comando_novo_orcamento = comando_novo_orcamento

        self.configurar_janela()
        self.criar_interface()

    def configurar_janela(self):
        self.janela.title("RentSmart | Sistema de Locação")
        self.janela.geometry("1100x700")
        self.janela.minsize(900, 600)
        self.janela.configure(bg=CORES["fundo"])

    def criar_interface(self):

        # MENU LATERAL
        self.menu = tk.Frame(
            self.janela,
            bg=CORES["azul_escuro"],
            width=230
        )

        self.menu.pack(side="left", fill="y")
        self.menu.pack_propagate(False)

        # LOGOTIPO
        tk.Label(
            self.menu,
            text="RentSmart",
            font=("Segoe UI", 23, "bold"),
            bg=CORES["azul_escuro"],
            fg=CORES["branco"]
        ).pack(pady=(35, 5))

        tk.Label(
            self.menu,
            text="GESTÃO DE LOCAÇÕES",
            font=("Segoe UI", 8, "bold"),
            bg=CORES["azul_escuro"],
            fg="#B8D4ED"
        ).pack(pady=(0, 40))

        # OPÇÕES DO MENU
        tk.Label(
            self.menu,
            text="MENU PRINCIPAL",
            font=("Segoe UI", 9, "bold"),
            bg=CORES["azul_escuro"],
            fg="#B8D4ED"
        ).pack(anchor="w", padx=20, pady=(0, 15))

        self.criar_item_menu("⌂   Início", self.voltar_inicio)
        self.criar_item_menu(
            "＋   Novo orçamento",
            self.comando_novo_orcamento
        )

        # IDENTIFICAÇÃO NO RODAPÉ
        tk.Label(
            self.menu,
            text="R.M IMÓVEIS\nSistema de orçamento",
            font=("Segoe UI", 9),
            bg=CORES["azul_escuro"],
            fg="#B8D4ED",
            justify="left"
        ).pack(side="bottom", anchor="w", padx=20, pady=25)

        # ÁREA PRINCIPAL
        self.conteudo = tk.Frame(
            self.janela,
            bg=CORES["fundo"]
        )

        self.conteudo.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.criar_painel_inicial()

    def criar_item_menu(self, texto, comando):

        botao = tk.Button(
            self.menu,
            text=texto,
            command=comando,
            font=("Segoe UI", 10),
            bg=CORES["azul_escuro"],
            fg=CORES["branco"],
            activebackground=CORES["azul"],
            activeforeground=CORES["branco"],
            relief="flat",
            anchor="w",
            padx=20,
            pady=14,
            cursor="hand2"
        )

        botao.pack(fill="x", padx=10, pady=3)

    def criar_painel_inicial(self):

        # CABEÇALHO
        cabecalho = tk.Frame(
            self.conteudo,
            bg=CORES["branco"],
            height=75
        )

        cabecalho.pack(fill="x")
        cabecalho.pack_propagate(False)

        tk.Label(
            cabecalho,
            text="Painel inicial",
            font=FONTES["subtitulo"],
            bg=CORES["branco"],
            fg=CORES["texto"]
        ).pack(side="left", padx=30, pady=22)

        # CONTEÚDO CENTRAL
        corpo = tk.Frame(
            self.conteudo,
            bg=CORES["fundo"]
        )

        corpo.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=45
        )

        # BOAS-VINDAS
        criar_titulo(
            corpo,
            "Bem-vindo ao RentSmart!"
        ).pack(anchor="w", pady=(10, 8))

        criar_texto(
            corpo,
            "Simplifique a gestão de orçamentos de locação."
        ).pack(anchor="w", pady=(0, 35))

        # CARTÃO PRINCIPAL
        cartao = tk.Frame(
            corpo,
            bg=CORES["branco"],
            padx=30,
            pady=30,
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )

        cartao.pack(fill="x", pady=10)

        criar_subtitulo(
            cartao,
            "Novo orçamento de locação"
        ).pack(anchor="w", pady=(0, 12))

        tk.Label(
            cartao,
            text=(
                "Calcule automaticamente o valor do aluguel, "
                "os adicionais,\nos descontos e a taxa contratual."
            ),
            font=FONTES["normal"],
            bg=CORES["branco"],
            fg=CORES["cinza"],
            justify="left"
        ).pack(anchor="w", pady=(0, 22))

        criar_botao(
            cartao,
            "＋  Criar novo orçamento",
            self.comando_novo_orcamento
        ).pack(anchor="w")

        # INFORMAÇÕES DO SISTEMA
        criar_subtitulo(
            corpo,
            "Sobre o sistema"
        ).pack(anchor="w", pady=(35, 15))

        informacoes = tk.Frame(
            corpo,
            bg=CORES["fundo"]
        )

        informacoes.pack(fill="x")

        self.criar_cartao_informacao(
            informacoes,
            "01",
            "Apartamentos",
            "Cálculo com adicionais e desconto."
        ).pack(side="left", fill="both", expand=True, padx=(0, 10))

        self.criar_cartao_informacao(
            informacoes,
            "02",
            "Casas",
            "Cálculo de quartos e garagem."
        ).pack(side="left", fill="both", expand=True, padx=10)

        self.criar_cartao_informacao(
            informacoes,
            "03",
            "Estúdios",
            "Cálculo de vagas de estacionamento."
        ).pack(side="left", fill="both", expand=True, padx=(10, 0))

    def criar_cartao_informacao(self, pai, numero, titulo, descricao):

        cartao = tk.Frame(
            pai,
            bg=CORES["branco"],
            padx=15,
            pady=20,
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )

        tk.Label(
            cartao,
            text=numero,
            font=("Segoe UI", 18, "bold"),
            bg=CORES["branco"],
            fg=CORES["azul"]
        ).pack(anchor="w")

        tk.Label(
            cartao,
            text=titulo,
            font=FONTES["subtitulo"],
            bg=CORES["branco"],
            fg=CORES["texto"]
        ).pack(anchor="w", pady=8)

        tk.Label(
            cartao,
            text=descricao,
            font=("Segoe UI", 9),
            bg=CORES["branco"],
            fg=CORES["cinza"],
            wraplength=180,
            justify="left"
        ).pack(anchor="w")

        return cartao

    def voltar_inicio(self):
        # O painel inicial já está aberto.
        pass
