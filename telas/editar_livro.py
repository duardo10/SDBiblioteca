import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Listbox, Scrollbar, END, messagebox
from firebase_service import db, auth
from telas.gerenciador_telas import get_tela_principal



def tela_editar_livro(container):
    email_usuario = auth.current_user['email']

    frame = ttk.Frame(container)
    frame.pack(expand=True, fill="both") 

    ttk.Label(frame, text="Editar Livro", font=(
        "Arial", 18, "bold")).pack(pady=10)

    # Listbox para exibir os livros
    livros_listbox = Listbox(frame, height=10, width=60)
    livros_listbox.pack(pady=10, padx=20)

    scrollbar = Scrollbar(frame, orient="vertical",
                          command=livros_listbox.yview)
    livros_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Buscar livros do usuário logado
    livros_dict = {}
    try:
        livros = db.child("livros").order_by_child(
            "email_usuario").equal_to(email_usuario).get()

        if livros.each() == []:
            # Se não houver livros cadastrados
            messagebox.showwarning("Aviso", "Não há livros cadastrados!")

        for livro in livros.each():
            livro_id = livro.key()  # ID do livro para edição
            titulo = livro.val()["titulo"]
            autor = livro.val()["autor"]
            livros_dict[livro_id] = livro.val()

            # Adiciona os livros na listbox com "editar" (lápis) e "excluir" (lixeira)
            livros_listbox.insert("end", f"{titulo} - {autor}")
            # Cor do texto para facilitar leitura
            livros_listbox.itemconfig("end", {'fg': 'blue'})

    except Exception as e:
        messagebox.showerror(
            "Erro", f"Não foi possível recuperar os livros! Erro: {str(e)}")

    # Função para editar o livro selecionado
    def editar_livro(livro_id, livro_data):
        # Criar campos de edição
        for widget in frame.winfo_children():
            widget.destroy()  # Limpa a tela antes de mostrar os campos de edição

        ttk.Label(frame, text="Editar Livro", font=(
            "Arial", 18, "bold")).pack(pady=10)

        ttk.Label(frame, text="Título:").pack()
        novo_titulo = ttk.Entry(frame, bootstyle="primary")
        novo_titulo.insert(0, livro_data["titulo"])
        novo_titulo.pack(pady=5, padx=20, fill="x")

        ttk.Label(frame, text="Autor:").pack()
        novo_autor = ttk.Entry(frame, bootstyle="primary")
        novo_autor.insert(0, livro_data["autor"])
        novo_autor.pack(pady=5, padx=20, fill="x")

        ttk.Label(frame, text="Quantidade de Páginas:").pack()
        novo_paginas = ttk.Entry(frame, bootstyle="primary")
        novo_paginas.insert(0, livro_data["paginas"])
        novo_paginas.pack(pady=5, padx=20, fill="x")

        ttk.Label(frame, text="Ano de Publicação:").pack()
        novo_ano = ttk.Entry(frame, bootstyle="primary")
        novo_ano.insert(0, livro_data["ano"])
        novo_ano.pack(pady=5, padx=20, fill="x")

        # Função para salvar a edição
        def salvar_edicao():
            db.child("livros").child(livro_id).update({
                "titulo": novo_titulo.get(),
                "autor": novo_autor.get(),
                "paginas": novo_paginas.get(),
                "ano": novo_ano.get()
            })
            messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")
            # Recarregar tela de edição
            mostrar_tela(tela_editar_livro, container)

        # Função para deletar o livro
        def deletar_livro():
            db.child("livros").child(livro_id).remove()
            messagebox.showinfo("Sucesso", "Livro deletado com sucesso!")
            # Recarregar tela de edição
            mostrar_tela(tela_editar_livro, container)

        # Botões para salvar a edição ou excluir o livro
        ttk.Button(frame, text="Salvar Edição", command=salvar_edicao,
                   bootstyle="SUCCESS").pack(pady=10)
        ttk.Button(frame, text="Deletar Livro", command=deletar_livro,
                   bootstyle="DANGER").pack(pady=10)
        ttk.Button(frame, text="Voltar", command=lambda: mostrar_tela(
            tela_editar_livro, container), bootstyle="LINK").pack(pady=10)

    # Função para lidar com a seleção de um livro
    def selecionar_livro():
        try:
            selecionado = livros_listbox.curselection()[0]
            livro_id = list(livros_dict.keys())[selecionado]
            livro_data = livros_dict[livro_id]
            editar_livro(livro_id, livro_data)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um livro para editar!")

    # Adicionar ação de seleção ao clicar na listbox
    livros_listbox.bind("<Double-1>", lambda event: selecionar_livro())

    # Botão para voltar
    ttk.Button(frame, text="Voltar", command=lambda: mostrar_tela(
        tela_principal, container), bootstyle="LINK").pack(pady=10)
     
