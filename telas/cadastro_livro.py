import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from firebase_service import adicionar_livro, auth
from telas.gerenciador_telas import get_tela_principal


def tela_cadastro_livro(container, root):
    frame = ttk.Frame(container)
    frame.pack(expand=True, fill="both") 
    frame.place(relx=0.5, rely=0.5, anchor="center")

    ttk.Label(frame, text="Cadastro de Livros", font=("Arial", 18, "bold")).pack(pady=10)

    ttk.Label(frame, text="Título:").pack()
    titulo_entry = ttk.Entry(frame, bootstyle="primary", width=30)
    titulo_entry.pack(pady=5, padx=20)

    ttk.Label(frame, text="Autor:").pack()
    autor_entry = ttk.Entry(frame, bootstyle="primary", width=30)
    autor_entry.pack(pady=5, padx=20)

    ttk.Label(frame, text="Quantidade de Páginas:").pack()
    paginas_entry = ttk.Entry(frame, bootstyle="primary", width=30)
    paginas_entry.pack(pady=5, padx=20)

    ttk.Label(frame, text="Ano de Publicação:").pack()
    ano_entry = ttk.Entry(frame, bootstyle="primary", width=30)
    ano_entry.pack(pady=5, padx=20)

    def salvar_livro():
        titulo = titulo_entry.get()
        autor = autor_entry.get()
        ano = ano_entry.get()
        paginas = paginas_entry.get()
        email_usuario = auth.current_user['email']

        if not titulo or not autor:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
            return

        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "paginas": paginas,
            "email_usuario": email_usuario
        }

        adicionar_livro(livro)
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
        root.mostrar_tela(get_tela_principal)

    ttk.Button(frame, text="Salvar Livro", command=salvar_livro, bootstyle=SUCCESS).pack(pady=10)
    ttk.Button(frame, text="Voltar", command=lambda: root.mostrar_tela(get_tela_principal), bootstyle=LINK).pack()
