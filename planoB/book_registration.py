import tkinter as tk
from tkinter import ttk, messagebox
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
db = firebase.database()

def show_book_registration(root, main_frame):
    """ Exibe a tela de cadastro de livro """

    for widget in main_frame.winfo_children():
        widget.destroy()

    # Centraliza o conteúdo
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Criando widgets
    title_label = ttk.Label(main_frame, text="Cadastrar Livro", font=("Arial", 20))
    entry_title = ttk.Entry(main_frame)
    entry_author = ttk.Entry(main_frame)
    entry_year = ttk.Entry(main_frame)
    entry_pages = ttk.Entry(main_frame)

    save_button = ttk.Button(main_frame, text="Salvar", command=lambda: save_book(entry_title, entry_author, entry_year, entry_pages, root, main_frame))
    back_button = ttk.Button(main_frame, text="Voltar", command=lambda: go_back_to_main(root, main_frame))

    # Layout centralizado usando grid()
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Label(main_frame, text="Título:").grid(row=1, column=0, sticky="e")
    entry_title.grid(row=1, column=1)

    ttk.Label(main_frame, text="Autor:").grid(row=2, column=0, sticky="e")
    entry_author.grid(row=2, column=1)

    ttk.Label(main_frame, text="Ano:").grid(row=3, column=0, sticky="e")
    entry_year.grid(row=3, column=1)

    ttk.Label(main_frame, text="Páginas:").grid(row=4, column=0, sticky="e")
    entry_pages.grid(row=4, column=1)

    save_button.grid(row=5, column=0, columnspan=2, pady=10)
    back_button.grid(row=6, column=0, columnspan=2)

def save_book(entry_title, entry_author, entry_year, entry_pages, root, main_frame):
    """ Salva o livro no Firebase """
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    pages = entry_pages.get()

    if not title or not author or not year or not pages:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    try:
        year = int(year)
        pages = int(pages)
    except ValueError:
        messagebox.showerror("Erro", "Ano e Páginas devem ser números!")
        return

    db.child("books").push({"title": title, "author": author, "year": year, "pages": pages})
    messagebox.showinfo("Sucesso", "Livro cadastrado!")
    go_back_to_main(root, main_frame)

def go_back_to_main(root, main_frame):
    """ Retorna à tela principal """
    from main_screen import show_main_screen
    show_main_screen(root, main_frame)
