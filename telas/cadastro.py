import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from firebase_service import cadastrar_usuario
from telas.gerenciador_telas import get_tela_login



def tela_cadastro(container, root):
    frame = ttk.Frame(container)
    frame.pack(expand=True, fill="both") 

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
        if cadastrar_usuario(email, senha):
            root.mostrar_tela(tela_login)

    ttk.Button(frame, text="Cadastrar", command=registrar, bootstyle=SUCCESS).pack(pady=10)
