import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from firebase_service import auth
from telas.gerenciador_telas import get_tela_cadastro_livro, get_tela_editar_livro, get_tela_pesquisar_livros, get_tela_login


def tela_principal(container, root):
    # Criar um frame centralizado para organizar os widgets
    frame = ttk.Frame(container)
    frame.pack(expand=True, fill="both") 
    frame.place(relx=0.5, rely=0.5, anchor="center")

    email_usuario = auth.current_user['email']
    ttk.Label(frame, text=f"Bem-vindo, {email_usuario}!",
              font=("Arial", 18, "bold")).pack(pady=10)

    button_width = 10  # Defina a largura fixa para os botões

    ttk.Button(frame, text="Cadastrar Livro", command=lambda: root.mostrar_tela(get_tela_cadastro_livro),
               bootstyle=SUCCESS, width=button_width).pack(pady=10, padx=20, fill=X)

    ttk.Button(frame, text="Editar Livro", command=lambda: root.mostrar_tela(get_tela_editar_livro),
               bootstyle=INFO, width=button_width).pack(pady=10, padx=20, fill=X)

    ttk.Button(frame, text="Pesquisar Livros", command=lambda: root.mostrar_tela(get_tela_pesquisar_livros),
               bootstyle=PRIMARY, width=button_width).pack(pady=10, padx=20, fill=X)

    ttk.Button(frame, text="Sair", command=lambda: root.mostrar_tela(get_tela_login),
               bootstyle=DANGER, width=button_width).pack(pady=10, padx=20, fill=X)
