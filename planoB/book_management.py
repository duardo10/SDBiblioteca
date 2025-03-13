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

# Inicializa o Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def show_book_management(root, main_frame):
    """ Exibe a tela de gerenciamento de livros """
    
    management_frame = ttk.Frame(root)
    management_frame.place(relx=0.5, rely=0.5, anchor="center")
    
    title_label = ttk.Label(management_frame, text="Gerenciar Livros", font=("Arial", 20))
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Função para listar livros
    def list_books():
        # Limpa a lista de livros
        for widget in management_frame.winfo_children():
            widget.grid_forget()

        books = db.child("books").get()
        if books.each():
            row = 1
            for book in books.each():
                book_data = book.val()
                book_id = book.key()
                book_info = f"{book_data['title']} - {book_data['author']}"
                ttk.Label(management_frame, text=book_info).grid(row=row, column=0, pady=5, padx=10)

                edit_button = ttk.Button(management_frame, text="Editar", command=lambda book_id=book_id: edit_book(book_id, management_frame))
                edit_button.grid(row=row, column=1, padx=5)

                delete_button = ttk.Button(management_frame, text="Excluir", command=lambda book_id=book_id: delete_book(book_id, management_frame))
                delete_button.grid(row=row, column=2, padx=5)

                row += 1
        else:
            messagebox.showinfo("Info", "Nenhum livro encontrado!")

    # Função para editar livro
    def edit_book(book_id, management_frame):
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
            list_books()  # Recarrega a lista de livros

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

    # Função para excluir livro
    def delete_book(book_id, management_frame):
        confirm = messagebox.askyesno("Confirmar Exclusão", "Você tem certeza que deseja excluir este livro?")
        if confirm:
            db.child("books").child(book_id).remove()
            messagebox.showinfo("Sucesso", "Livro excluído com sucesso!")
            list_books()  # Recarrega a lista de livros

    # Carregar a lista de livros
    list_books()

    # Botão para voltar para a tela principal
    back_button = ttk.Button(management_frame, text="Voltar", command=lambda: go_back_to_main(root, management_frame))
    back_button.grid(row=row + 1, column=0, columnspan=2, pady=20)

# Função para voltar para a tela principal
def go_back_to_main(root, management_frame):
    management_frame.place_forget()
    from main_screen import show_main_screen
    show_main_screen(root)
