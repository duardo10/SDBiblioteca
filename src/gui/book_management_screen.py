import tkinter as tk
from tkinter import ttk

class BookManagementScreen(ttk.Frame):
    def __init__(self, parent, on_list_books):
        super().__init__(parent)
        self.on_list_books = on_list_books
        self.create_widgets()

    def create_widgets(self):
        self.pack(pady=20)

        ttk.Label(self, text="Título do Livro:", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.title_entry = ttk.Entry(self, width=30)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Autor Principal:", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.author_entry = ttk.Entry(self, width=30)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Quantidade de Páginas:", font=("Helvetica", 12)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.pages_entry = ttk.Entry(self, width=30)
        self.pages_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self, text="Ano de Publicação:", font=("Helvetica", 12)).grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.year_entry = ttk.Entry(self, width=30)
        self.year_entry.grid(row=3, column=1, padx=5, pady=5)

        add_button = ttk.Button(self, text="Adicionar Livro")
        add_button.grid(row=4, column=0, columnspan=2, pady=20)

        list_books_button = ttk.Button(self, text="Listar Livros", command=self.on_list_books)
        list_books_button.grid(row=5, column=0, columnspan=2, pady=10) 