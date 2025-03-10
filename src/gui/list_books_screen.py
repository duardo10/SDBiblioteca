import tkinter as tk
from tkinter import ttk

class ListBooksScreen(ttk.Frame):
    def __init__(self, parent, on_back):
        super().__init__(parent)
        self.on_back = on_back
        self.create_widgets()

    def create_widgets(self):
        self.pack(pady=20)

        ttk.Label(self, text="Listagem de Livros", font=("Helvetica", 14, "bold")).pack(pady=10)

        # Aqui você pode adicionar um Treeview ou Listbox para mostrar os livros

        back_button = ttk.Button(self, text="Voltar", command=self.on_back)
        back_button.pack(pady=20) 