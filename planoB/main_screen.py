import tkinter as tk
from tkinter import ttk, messagebox
import pyrebase
import book_registration  

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

def show_main_screen(root, current_frame=None):
    """ Exibe a tela principal centralizada """

    if current_frame:
        for widget in current_frame.winfo_children():
            widget.destroy()

    # Configuração para centralizar conteúdo
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    main_frame = ttk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Criando os widgets
    welcome_label = ttk.Label(main_frame, text="Bem-vindo ao sistema!", font=("Arial", 20))
    register_button = ttk.Button(main_frame, text="Cadastrar Livro", command=lambda: open_book_registration(root, main_frame))
    list_books_button = ttk.Button(main_frame, text="Listar Livros", command=lambda: list_books(root, main_frame))
    close_button = ttk.Button(main_frame, text="Sair", command=root.quit)

    # Layout centralizado usando grid()
    welcome_label.grid(row=0, column=0, columnspan=2, pady=20)
    register_button.grid(row=1, column=0, columnspan=2, pady=10)
    list_books_button.grid(row=2, column=0, columnspan=2, pady=10)
    close_button.grid(row=3, column=0, columnspan=2, pady=10)

def open_book_registration(root, main_frame):
    """ Abre a tela de cadastro de livro """
    book_registration.show_book_registration(root, main_frame)

def list_books(root, main_frame):
    """ Exibe a lista de livros cadastrados """

    for widget in main_frame.winfo_children():
        widget.destroy()

    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    title_label = ttk.Label(main_frame, text="Livros Cadastrados", font=("Arial", 20))
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    books = db.child("books").get()

    if books.each():
        row = 1
        for book in books.each():
            book_data = book.val()
            book_id = book.key()
            book_label = ttk.Label(main_frame, text=f"{book_data['title']} - {book_data['author']}", font=("Arial", 14))
            book_label.grid(row=row, column=0, columnspan=2, pady=5)

            # Botões de edição e exclusão
            edit_button = ttk.Button(main_frame, text="Editar", command=lambda book_id=book_id: edit_book(book_id, root, main_frame))
            edit_button.grid(row=row, column=2, padx=5)

            delete_button = ttk.Button(main_frame, text="Excluir", command=lambda book_id=book_id: delete_book(book_id, root, main_frame))
            delete_button.grid(row=row, column=3, padx=5)

            row += 1
    else:
        messagebox.showinfo("Aviso", "Nenhum livro cadastrado.")

    # Botão para voltar para a tela principal
    back_button = ttk.Button(main_frame, text="Voltar", command=lambda: show_main_screen(root, main_frame))
    back_button.grid(row=row, column=0, columnspan=4, pady=20)

def edit_book(book_id, root, main_frame):
    """ Abre a tela de edição de livro """

    book_data = db.child("books").child(book_id).get().val()

    def save_edit():
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
            messagebox.showerror("Erro", "Ano e quantidade de páginas devem ser números!")
            return

        updated_data = {"title": title, "author": author, "year": year, "pages": pages}
        db.child("books").child(book_id).update(updated_data)
        messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")
        list_books(root, main_frame)  # Recarrega a lista de livros

    # Formulário de edição
    edit_window = tk.Toplevel(root)
    edit_window.title("Editar Livro")

    ttk.Label(edit_window, text="Título:").grid(row=0, column=0)
    entry_title = ttk.Entry(edit_window)
    entry_title.grid(row=0, column=1)
    entry_title.insert(0, book_data['title'])

    ttk.Label(edit_window, text="Autor:").grid(row=1, column=0)
    entry_author = ttk.Entry(edit_window)
    entry_author.grid(row=1, column=1)
    entry_author.insert(0, book_data['author'])

    ttk.Label(edit_window, text="Ano:").grid(row=2, column=0)
    entry_year = ttk.Entry(edit_window)
    entry_year.grid(row=2, column=1)
    entry_year.insert(0, book_data['year'])

    ttk.Label(edit_window, text="Páginas:").grid(row=3, column=0)
    entry_pages = ttk.Entry(edit_window)
    entry_pages.grid(row=3, column=1)
    entry_pages.insert(0, book_data['pages'])

    save_button = ttk.Button(edit_window, text="Salvar", command=save_edit)
    save_button.grid(row=4, column=0, columnspan=2, pady=20)

def delete_book(book_id, root, main_frame):
    """ Exclui o livro do banco de dados """

    confirm = messagebox.askyesno("Confirmar Exclusão", "Você tem certeza que deseja excluir este livro?")
    if confirm:
        db.child("books").child(book_id).remove()
        messagebox.showinfo("Sucesso", "Livro excluído com sucesso!")
        list_books(root, main_frame)  # Recarrega a lista de livros
