import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Listbox, Scrollbar, END, messagebox
from firebase_service import obter_livros
from telas.gerenciador_telas import get_tela_principal


def tela_pesquisar_livros(container, root):
    frame = ttk.Frame(container)
    frame.pack(expand=True, fill="both") 

    ttk.Label(frame, text="Pesquisar Livros", font=("Arial", 18, "bold")).pack(pady=10)

    livros_listbox = Listbox(frame, height=10, width=50)
    livros_listbox.pack(pady=10, padx=20)

    scrollbar = Scrollbar(frame, orient="vertical", command=livros_listbox.yview)
    livros_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    livros = obter_livros()
    for livro in livros.each():
        titulo = livro.val()["titulo"]
        autor = livro.val()["autor"]
        livros_listbox.insert(END, f"{titulo} - {autor}")

    ttk.Button(frame, text="Voltar", command=lambda: root.mostrar_tela(tela_principal), bootstyle=LINK).pack(pady=10)
