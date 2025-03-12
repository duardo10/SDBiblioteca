import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox, Listbox, Scrollbar, END, Entry
import pyrebase

# Configuração do Firebase
firebaseConfig = {
    'apiKey': "AIzaSyCcKoowTWge7vtVIkSsT_Dj13fHXZM3_zs",
    'authDomain': "sistemasdistribuidos-e8eaf.firebaseapp.com",
    'databaseURL': "https://sistemasdistribuidos-e8eaf-default-rtdb.firebaseio.com",
    'projectId': "sistemasdistribuidos-e8eaf",
    'storageBucket': "sistemasdistribuidos-e8eaf.firebasestorage.app",
    'messagingSenderId': "34064682324",
    'appId': "1:34064682324:web:61ebb87c80e40748edccc1"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

# Criando a janela principal
root = ttk.Window(themename="solar")
root.title("Login e Cadastro")
root.geometry("1280x832")

# Função para alternar entre telas


def mostrar_tela(tela, previous_container=None):
    for widget in root.winfo_children():
        widget.destroy()

    if previous_container is None:
        container = ttk.Frame(root)
        # Centraliza o container
        container.place(relx=0.5, rely=0.5, anchor="center")
    else:
        container = previous_container

    tela(container)

# Tela de Login


def tela_login(container):
    # Criar um frame para centralizar os elementos
    frame = ttk.Frame(container)
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza na tela

    ttk.Label(frame, text="Login", font=("Arial", 18, "bold")).pack(pady=10)

    ttk.Label(frame, text="Email:").pack()
    email_entry = ttk.Entry(frame, bootstyle="primary")
    email_entry.pack(pady=5, padx=20, fill=X)

    ttk.Label(frame, text="Senha:").pack()
    senha_entry = ttk.Entry(frame, bootstyle="primary", show="*")
    senha_entry.pack(pady=5, padx=20, fill=X)

    def validar_login():
        email = email_entry.get()
        senha = senha_entry.get()
        try:
            user = auth.sign_in_with_email_and_password(email, senha)
            messagebox.showinfo("Sucesso", f"Bem-vindo, {email}!")
            mostrar_tela(tela_principal, container)  # Passando o container
        except:
            messagebox.showerror("Erro", "Email ou senha inválidos!")

    ttk.Button(frame, text="Entrar", command=validar_login,
               bootstyle=SUCCESS).pack(pady=10)
    ttk.Button(frame, text="Cadastrar-se",
               command=lambda: mostrar_tela(tela_cadastro, container), bootstyle=LINK).pack()

# Tela principal (após login)


def tela_principal(container):
    # Criar um frame centralizado para organizar os widgets
    frame = ttk.Frame(container)
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza na tela

    email_usuario = auth.current_user['email']
    ttk.Label(frame, text=f"Bem-vindo, {email_usuario}!",
              font=("Arial", 18, "bold")).pack(pady=10)

    button_width = 20  # Defina a largura fixa para os botões

    ttk.Button(frame, text="Cadastrar Livro", command=lambda: mostrar_tela(tela_cadastro_livro, container),
               bootstyle=SUCCESS, width=button_width).pack(pady=10, padx=20, fill=X)

    ttk.Button(frame, text="Editar Livro", command=lambda: mostrar_tela(tela_editar_livro, container),
               bootstyle=INFO, width=button_width).pack(pady=10, padx=20, fill=X)

    ttk.Button(frame, text="Pesquisar Livros", command=lambda: mostrar_tela(tela_pesquisar_livros, container),
               bootstyle=PRIMARY, width=button_width).pack(pady=10, padx=20, fill=X)

    ttk.Button(frame, text="Sair", command=lambda: mostrar_tela(tela_login, container),
               bootstyle=DANGER, width=button_width).pack(pady=10, padx=20, fill=X)


# Tela de Cadastro
def tela_cadastro(container):
    # Criar um frame para centralizar os elementos
    frame = ttk.Frame(container)
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza na tela

    ttk.Label(frame, text="Cadastro", font=("Arial", 18, "bold")).pack(pady=10)

    ttk.Label(frame, text="Email:").pack()
    email_entry = ttk.Entry(frame, bootstyle="primary")
    email_entry.pack(pady=5, padx=20, fill=X)

    ttk.Label(frame, text="Senha:").pack()
    senha_entry = ttk.Entry(frame, bootstyle="primary", show="*")
    senha_entry.pack(pady=5, padx=20, fill=X)

    def registrar():
        email = email_entry.get()
        senha = senha_entry.get()

        if len(senha) < 6:
            messagebox.showwarning(
                "Aviso", "A senha deve ter pelo menos 6 caracteres!")
            return

        try:
            auth.create_user_with_email_and_password(email, senha)
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            mostrar_tela(tela_login, container)
        except:
            messagebox.showerror(
                "Erro", "Erro ao cadastrar. Email pode já estar em uso!")

    ttk.Button(frame, text="Cadastrar", command=registrar,
               bootstyle=SUCCESS).pack(pady=10)
    ttk.Button(frame, text="Voltar", command=lambda: mostrar_tela(
        tela_login, container), bootstyle=LINK).pack()


# Tela de Pesquisa de Livros


def tela_pesquisar_livros(container):
    ttk.Label(container, text="Pesquisar Livros",
              font=("Arial", 18, "bold")).pack(pady=10)

    livros_listbox = Listbox(container, height=10, width=50)
    livros_listbox.pack(pady=10, padx=20)

    scrollbar = Scrollbar(container, orient="vertical",
                          command=livros_listbox.yview)
    livros_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    try:
        livros = db.child("livros").get()  # Recupera todos os livros
        for livro in livros.each():
            titulo = livro.val()["titulo"]
            autor = livro.val()["autor"]
            livros_listbox.insert(END, f"{titulo} - {autor}")
    except:
        messagebox.showerror("Erro", "Não foi possível recuperar os livros!")

    ttk.Button(container, text="Voltar", command=lambda: mostrar_tela(
        tela_principal, container), bootstyle=LINK).pack(pady=10)


def tela_editar_livro(container):
    email_usuario = auth.current_user['email']

    frame = ttk.Frame(container)
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza na tela

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

# Tela de Cadastro de Livro


def tela_cadastro_livro(container):
    # Criar um frame para centralizar os elementos
    frame = ttk.Frame(container)
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza na tela

    ttk.Label(frame, text="Cadastro de Livros",
              font=("Arial", 18, "bold")).pack(pady=10)

    ttk.Label(frame, text="Título:").pack()
    titulo_entry = ttk.Entry(frame, bootstyle="primary")
    titulo_entry.pack(pady=5, padx=20, fill=X)

    ttk.Label(frame, text="Autor:").pack()
    autor_entry = ttk.Entry(frame, bootstyle="primary")
    autor_entry.pack(pady=5, padx=20, fill=X)

    ttk.Label(frame, text="Quantidade de Páginas:").pack()
    paginas_entry = ttk.Entry(frame, bootstyle="primary")
    paginas_entry.pack(pady=5, padx=20, fill=X)

    ttk.Label(frame, text="Ano de Publicação:").pack()
    ano_entry = ttk.Entry(frame, bootstyle="primary")
    ano_entry.pack(pady=5, padx=20, fill=X)

    def salvar_livro():
        titulo = titulo_entry.get()
        autor = autor_entry.get()
        paginas = paginas_entry.get()
        ano = ano_entry.get()

        if not titulo or not autor or not paginas or not ano:
            messagebox.showwarning(
                "Aviso", "Todos os campos devem ser preenchidos!")
            return

        livro = {
            "titulo": titulo,
            "autor": autor,
            "paginas": paginas,
            "ano": ano,
            # Associa o livro ao usuário logado
            "email_usuario": auth.current_user['email']
        }

        try:
            db.child("livros").push(livro)
            messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
        except:
            messagebox.showerror("Erro", "Não foi possível cadastrar o livro!")

    ttk.Button(frame, text="Salvar Livro", command=salvar_livro,
               bootstyle=SUCCESS).pack(pady=10)
    ttk.Button(frame, text="Voltar", command=lambda: mostrar_tela(
        tela_principal, container), bootstyle=LINK).pack()


# Mostrar a tela de login inicialmente
tela_login(root)

root.mainloop()
