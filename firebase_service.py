from config import auth, db
from tkinter import messagebox


def login_usuario(email, senha):
    try:
        user = auth.sign_in_with_email_and_password(email, senha)
        return user
    except:
        messagebox.showerror("Erro", "Email ou senha inválidos!")
        return None


def cadastrar_usuario(email, senha):
    if len(senha) < 6:
        messagebox.showwarning("Aviso", "A senha deve ter pelo menos 6 caracteres!")
        return False

    try:
        auth.create_user_with_email_and_password(email, senha)
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        return True
    except:
        messagebox.showerror("Erro", "Erro ao cadastrar. Email pode já estar em uso!")
        return False


def adicionar_livro(livro):
    try:
        db.child("livros").push(livro)
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
    except:
        messagebox.showerror("Erro", "Não foi possível cadastrar o livro!")


def obter_livros():
    try:
        return db.child("livros").get()
    except:
        messagebox.showerror("Erro", "Não foi possível recuperar os livros!")
        return []
