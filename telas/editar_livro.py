import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Listbox, Scrollbar, END, messagebox
from firebase_service import db, auth
from telas.gerenciador_telas import get_tela_principal


def tela_editar_livro(container, root):
    email_usuario = auth.current_user['email']

    frame = ttk.Frame(container)
    frame.pack(expand=True, fill="both") 

    ttk.Label(frame, text="Editar Livro", font=("Arial", 18, "bold")).pack(pady=10)

    # Listbox para exibir os livros
    livros_listbox = Listbox(frame, height=10, width=60)
    livros_listbox.pack(pady=10, padx=20)

    scrollbar = Scrollbar(frame, orient="vertical", command=livros_listbox.yview)
    livros_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Buscar livros do usuário logado
    livros_dict = {}
    try:
        livros = db.child("livros").order_by_child("email_usuario").equal_to(email_usuario).get()

        if not livros.each():
            messagebox.showwarning("Aviso", "Não há livros cadastrados!")

        for livro in livros.each():
            livro_id = livro.key()
            titulo = livro.val()["titulo"]
            autor = livro.val()["autor"]
            livros_dict[livro_id] = livro.val()
            livros_listbox.insert("end", f"{titulo} - {autor}")

    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível recuperar os livros! Erro: {str(e)}")

    # Função para editar o livro selecionado
    def editar_livro(livro_id, livro_data):
        for widget in frame.winfo_children():
            widget.destroy()

        ttk.Label(frame, text="Editar Livro", font=("Arial", 18, "bold")).pack(pady=10)

        ttk.Label(frame, text="Título:").pack()
        novo_titulo = ttk.Entry(frame, bootstyle="primary")
        novo_titulo.insert(0, livro_data["titulo"])
        novo_titulo.pack(pady=5, padx=20, fill="x")

        ttk.Label(frame, text="Autor:").pack()
        novo_autor = ttk.Entry(frame, bootstyle="primary")
        novo_autor.insert(0, livro_data["autor"])
        novo_autor.pack(pady=5, padx=20, fill="x")

        def salvar_edicao():
            db.child("livros").child(livro_id).update({
                "titulo": novo_titulo.get(),
                "autor": novo_autor.get()
            })
            messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")
            root.mostrar_tela(get_tela_editar_livro)

        def deletar_livro():
            db.child("livros").child(livro_id).remove()
            messagebox.showinfo("Sucesso", "Livro deletado com sucesso!")
            root.mostrar_tela(get_tela_editar_livro)

        ttk.Button(frame, text="Salvar Edição", command=salvar_edicao, bootstyle="SUCCESS").pack(pady=10)
        ttk.Button(frame, text="Deletar Livro", command=deletar_livro, bootstyle="DANGER").pack(pady=10)
        ttk.Button(frame, text="Voltar", command=lambda: root.mostrar_tela(get_tela_editar_livro), bootstyle="LINK").pack(pady=10)

    def selecionar_livro():
        try:
            selecionado = livros_listbox.curselection()[0]
            livro_id = list(livros_dict.keys())[selecionado]
            livro_data = livros_dict[livro_id]
            editar_livro(livro_id, livro_data)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um livro para editar!")

    livros_listbox.bind("<Double-1>", lambda event: selecionar_livro())

    ttk.Button(frame, text="Voltar", command=lambda: root.mostrar_tela(get_tela_principal), bootstyle="LINK").pack(pady=10)
