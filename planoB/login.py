import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyrebase
import main_screen  # Importa o arquivo da tela principal

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

# Função de login
def login():
    email = entry_email.get()
    password = entry_password.get()

    # Verificar se os campos não estão vazios
    if not email or not password:
        messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos.")
        return

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        messagebox.showinfo("Login", "Login bem-sucedido!")
        show_main_screen()  # Exibe a tela principal após o login
    except Exception as e:
        messagebox.showerror("Erro", f"Credenciais inválidas ou erro: {str(e)}")

# Função de registro
def register():
    email = entry_register_email.get()
    password = entry_register_password.get()

    # Verificar se os campos não estão vazios
    if not email or not password:
        messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos.")
        return

    # Verificar se o e-mail é válido
    if '@' not in email or '.' not in email:
        messagebox.showwarning("E-mail inválido", "Por favor, insira um e-mail válido.")
        return

    # Verificar se a senha tem comprimento mínimo
    if len(password) < 6:
        messagebox.showwarning("Senha fraca", "A senha deve ter pelo menos 6 caracteres.")
        return

    try:
        # Tenta criar um novo usuário no Firebase
        auth.create_user_with_email_and_password(email, password)
        messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso! Agora, faça o login.")
        show_login_screen()  # Exibe a tela de login após o cadastro
    except pyrebase.pyrebase.AuthException as e:
        # Se o e-mail já estiver registrado ou outro erro de autenticação ocorrer
        messagebox.showerror("Erro", f"Erro ao cadastrar: {str(e)}")
    except Exception as e:
        # Captura de outros erros genéricos
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Função para exibir a tela principal
def show_main_screen():
    login_frame.place_forget()  # Esconde a tela de login
    register_frame.place_forget()  # Esconde a tela de registro
    main_screen.show_main_screen(root)  # Chama a tela principal

# Função para alternar entre as telas de login e registro
def show_register_screen():
    login_frame.place_forget()  # Esconde a tela de login
    register_frame.place(relx=0.5, rely=0.5, anchor="center")  # Exibe a tela de registro

def show_login_screen():
    register_frame.place_forget()  # Esconde a tela de registro
    login_frame.place(relx=0.5, rely=0.5, anchor="center")  # Exibe a tela de login

# Função para alternar a visibilidade da senha no login
def toggle_password():
    if entry_password.cget("show") == "*":
        entry_password.config(show="")
        show_password_button.config(text="Ocultar senha")
    else:
        entry_password.config(show="*")
        show_password_button.config(text="Mostrar senha")

# Configuração da Janela Principal
root = tk.Tk()
root.title("Login e Cadastro")
root.geometry("1280x832")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Frame para a tela de login
login_frame = ttk.Frame(root)
login_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o frame

# Título da tela de login
title = ttk.Label(login_frame, text="Login", font=("Arial", 20))
title.grid(row=0, column=0, columnspan=2, pady=20)

# Email
label_email = ttk.Label(login_frame, text="Email:")
label_email.grid(row=1, column=0, pady=5, padx=10, sticky="e")

entry_email = ttk.Entry(login_frame)
entry_email.grid(row=1, column=1, pady=5, padx=10)
entry_email.focus()  # Foca no campo de e-mail ao iniciar

# Senha
label_password = ttk.Label(login_frame, text="Senha:")
label_password.grid(row=2, column=0, pady=5, padx=10, sticky="e")

entry_password = ttk.Entry(login_frame, show="*")
entry_password.grid(row=2, column=1, pady=5, padx=10)

# Botão para mostrar/ocultar senha
show_password_button = ttk.Button(login_frame, text="Mostrar senha", command=toggle_password)
show_password_button.grid(row=3, column=1, pady=5, sticky="w")

# Botão de login
login_button = ttk.Button(login_frame, text="Login", command=login)
login_button.grid(row=4, column=0, columnspan=2, pady=20)

# Link para abrir a tela de registro
register_link = ttk.Button(login_frame, text="Cadastrar-se", command=show_register_screen)
register_link.grid(row=5, column=0, columnspan=2, pady=10)

# Frame para a tela de registro
register_frame = ttk.Frame(root)

# Título da tela de registro
register_title = ttk.Label(register_frame, text="Cadastro", font=("Arial", 20))
register_title.grid(row=0, column=0, columnspan=2, pady=20)

# Email
label_register_email = ttk.Label(register_frame, text="Email:")
label_register_email.grid(row=1, column=0, pady=5, padx=10, sticky="e")

entry_register_email = ttk.Entry(register_frame)
entry_register_email.grid(row=1, column=1, pady=5, padx=10)
entry_register_email.focus()  # Foca no campo de e-mail ao iniciar

# Senha
label_register_password = ttk.Label(register_frame, text="Senha:")
label_register_password.grid(row=2, column=0, pady=5, padx=10, sticky="e")

entry_register_password = ttk.Entry(register_frame, show="*")
entry_register_password.grid(row=2, column=1, pady=5, padx=10)

# Botão de cadastro
register_button = ttk.Button(register_frame, text="Cadastrar", command=register)
register_button.grid(row=3, column=0, columnspan=2, pady=20)

# Link para voltar à tela de login
back_to_login_button = ttk.Button(register_frame, text="Já tem uma conta? Faça login", command=show_login_screen)
back_to_login_button.grid(row=4, column=0, columnspan=2, pady=10)

# Executar o loop da interface
root.mainloop()
