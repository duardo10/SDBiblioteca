import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from firebase_service import cadastrar_usuario
from telas.gerenciador_telas import get_tela_login



def tela_cadastro(container, root):
    frame = ttk.Frame(container)
    frame.pack(expand=True, fill="both") 
    frame.place(relx=0.5, rely=0.5, anchor="center")
    
    ttk.Label(frame, text="Cadastro", font=("Arial", 18, "bold")).pack(pady=10)

    ttk.Label(frame, text="Email:").pack()
    email_entry = ttk.Entry(frame, bootstyle="primary", width=30)
    email_entry.pack(pady=5, padx=20)

    ttk.Label(frame, text="Senha:").pack()
    senha_entry = ttk.Entry(frame, bootstyle="primary", show="*", width=30)
    senha_entry.pack(pady=5, padx=20)

    def registrar():
        email = email_entry.get()
        senha = senha_entry.get()
        if cadastrar_usuario(email, senha):
            root.mostrar_tela(tela_login)

    ttk.Button(frame, text="Cadastrar", command=registrar, bootstyle=SUCCESS).pack(pady=10)
    ttk.Button(frame, text="Voltar", command=lambda: root.mostrar_tela(get_tela_login), bootstyle=LINK).pack()
    
