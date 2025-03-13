import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from firebase_service import adicionar_livro
from firebase_service import auth
from telas.principal import get_tela_principal




def tela_cadastro_livro(container, root):
    frame = ttk.Frame(container)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    ttk.Label(frame, text="Cadastro de Livros", font=("Arial", 18, "bold")).pack(pady=10)

    ttk.Label(frame, text="Título:").pack()
    titulo_entry = ttk.Entry(frame, bootstyle="primary")
    titulo_entry.pack(pady=5, padx=20, fill=X)

    ttk.Label(frame, text="Autor:").pack()
    autor_entry = ttk.Entry(frame, bootstyle="primary")
    autor_entry.pack(pady=5, padx=20, fill=X)

    def salvar_livro():
        titulo = titulo_entry.get()
        autor = autor_entry.get()
        email_usuario = auth.current_user['email']

        if not titulo or not autor:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
            return

        livro = {
            "titulo": titulo,
            "autor": autor,
            "email_usuario": email_usuario
        }

        adicionar_livro(livro)

    ttk.Button(frame, text="Salvar Livro", command=salvar_livro, bootstyle=SUCCESS).pack(pady=10)
    ttk.Button(frame, text="Voltar", command=lambda: root.mostrar_tela(tela_principal), bootstyle=LINK).pack()
