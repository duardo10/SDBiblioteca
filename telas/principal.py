import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from firebase_service import auth
from telas.gerenciador_telas import get_tela_cadastro_livro
from telas.gerenciador_telas import get_tela_editar_livro
from telas.gerenciador_telas import get_tela_pesquisar_livros
from telas.gerenciador_telas import get_tela_login


def tela_principal(container):
    # Criar um frame centralizado para organizar os widgets
    frame = ttk.Frame(container)
    frame.pack(expand=True, fill="both") 

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
