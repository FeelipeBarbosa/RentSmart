
import tkinter as tk
from tkinter import ttk


# IDENTIDADE VISUAL DO RENTSMART # :)

CORES = {
    "azul_escuro": "#173B63",
    "azul": "#2878B5",
    "azul_claro": "#EAF3FA",
    "branco": "#FFFFFF",
    "fundo": "#F4F7FB",
    "texto": "#263445",
    "cinza": "#718096",
    "verde": "#198754",
    "vermelho": "#DC3545"
}

FONTES = {
    "titulo": ("Segoe UI", 22, "bold"),
    "subtitulo": ("Segoe UI", 13, "bold"),
    "normal": ("Segoe UI", 10),
    "botao": ("Segoe UI", 10, "bold")
}


def criar_titulo(pai, texto):
    titulo = tk.Label(
        pai,
        text=texto,
        font=FONTES["titulo"],
        bg=CORES["fundo"],
        fg=CORES["azul_escuro"]
    )

    return titulo


def criar_subtitulo(pai, texto):
    subtitulo = tk.Label(
        pai,
        text=texto,
        font=FONTES["subtitulo"],
        bg=CORES["fundo"],
        fg=CORES["texto"]
    )

    return subtitulo


def criar_texto(pai, texto):
    label = tk.Label(
        pai,
        text=texto,
        font=FONTES["normal"],
        bg=CORES["fundo"],
        fg=CORES["cinza"]
    )

    return label


def criar_botao(pai, texto, comando, cor=None):
    if cor is None:
        cor = CORES["azul"]

    botao = tk.Button(
        pai,
        text=texto,
        command=comando,
        font=FONTES["botao"],
        bg=cor,
        fg=CORES["branco"],
        activebackground=CORES["azul_escuro"],
        activeforeground=CORES["branco"],
        relief="flat",
        cursor="hand2",
        padx=18,
        pady=10,
        borderwidth=0
    )

    return botao


def criar_campo(pai, largura=30):
    campo = ttk.Entry(
        pai,
        width=largura,
        font=FONTES["normal"]
    )

    return campo


def configurar_estilo():
    estilo = ttk.Style()

    estilo.configure(
        "RentSmart.TCombobox",
        padding=8,
        font=FONTES["normal"]
    )

    estilo.configure(
        "RentSmart.TEntry",
        padding=8,
        font=FONTES["normal"]
    )

    return estilo
