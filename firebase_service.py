from config import auth, db
from tkinter import messagebox
import time


def login_usuario(email, senha):
    start_time = time.time()
    try:
        user = auth.sign_in_with_email_and_password(email, senha)
        duration = time.time() - start_time
        print(f"Login request duration: {duration:.4f} seconds")
        return user
    except:
        duration = time.time() - start_time
        print(f"Login request failed after {duration:.4f} seconds")
        messagebox.showerror("Erro", "Email ou senha inválidos!")
        return None


def cadastrar_usuario(email, senha):
    start_time = time.time()
    if len(senha) < 6:
        messagebox.showwarning("Aviso", "A senha deve ter pelo menos 6 caracteres!")
        return False

    try:
        auth.create_user_with_email_and_password(email, senha)
        duration = time.time() - start_time
        print(f"User registration request duration: {duration:.4f} seconds")
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        return True
    except:
        duration = time.time() - start_time
        print(f"User registration request failed after {duration:.4f} seconds")
        messagebox.showerror("Erro", "Erro ao cadastrar. Email pode já estar em uso!")
        return False


def adicionar_livro(livro):
    start_time = time.time()
    try:
        db.child("livros").push(livro)
        duration = time.time() - start_time
        print(f"Add book request duration: {duration:.4f} seconds")
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
    except:
        duration = time.time() - start_time
        print(f"Add book request failed after {duration:.4f} seconds")
        messagebox.showerror("Erro", "Não foi possível cadastrar o livro!")


def obter_livros():
    start_time = time.time()
    try:
        livros = db.child("livros").get()
        duration = time.time() - start_time
        print(f"Get books request duration: {duration:.4f} seconds")
        return livros
    except:
        duration = time.time() - start_time
        print(f"Get books request failed after {duration:.4f} seconds")
        messagebox.showerror("Erro", "Não foi possível recuperar os livros!")
        return []
