
import tkinter as tk

from ui.janela_principal import JanelaPrincipal
from ui.tela_orcamento import TelaOrcamento


def abrir_orcamento(janela):
    TelaOrcamento(janela)


def iniciar_sistema():

    # Criar a janela principal
    janela = tk.Tk()

    # Configurar o sistema
    JanelaPrincipal(
        janela,
        comando_novo_orcamento=lambda: abrir_orcamento(janela)
    )

    # Iniciar a aplicação
    janela.mainloop()


if __name__ == "__main__":
    iniciar_sistema()
