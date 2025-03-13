import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from firebase_service import login_usuario
from telas.gerenciador_telas import get_tela_principal, get_tela_cadastro


def tela_login(container, root):
    frame = ttk.Frame(container)
    frame.pack(expand=True, fill="both")  # Garantindo que o frame ocupe espaço

    ttk.Label(frame, text="Login", font=("Arial", 18, "bold")).pack(pady=10)

    ttk.Label(frame, text="Email:").pack()
    email_entry = ttk.Entry(frame, bootstyle="primary")
    email_entry.pack(pady=5, padx=20, fill="x")

    ttk.Label(frame, text="Senha:").pack()
    senha_entry = ttk.Entry(frame, bootstyle="primary", show="*")
    senha_entry.pack(pady=5, padx=20, fill="x")

    def validar_login():
        email = email_entry.get()
        senha = senha_entry.get()
        user = login_usuario(email, senha)
        if user:
            messagebox.showinfo("Sucesso", f"Bem-vindo, {email}!")
            root.mostrar_tela(get_tela_principal)

    ttk.Button(frame, text="Entrar", command=validar_login, bootstyle=SUCCESS).pack(pady=10)
    ttk.Button(frame, text="Cadastrar-se", 
               command=lambda: root.mostrar_tela(get_tela_cadastro), 
               bootstyle=LINK).pack()

