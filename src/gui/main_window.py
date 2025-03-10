# Este arquivo será responsável pela implementação da interface gráfica principal usando Tkinter.
# Aqui, você deve criar a janela principal e os componentes da interface do usuário. 

import tkinter as tk
from tkinter import ttk
from src.gui.login_screen import LoginScreen
from src.gui.book_management_screen import BookManagementScreen
from src.gui.list_books_screen import ListBooksScreen

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Cadastro de Livros")
        self.geometry("600x400")
        
        # Aplicar tema
        style = ttk.Style(self)
        style.theme_use('clam')  # Você pode escolher entre 'clam', 'alt', 'default', 'classic'

        self.login_screen = LoginScreen(self, self.show_book_management_screen)
        self.book_management_screen = BookManagementScreen(self, self.show_list_books_screen)
        self.list_books_screen = ListBooksScreen(self, self.show_book_management_screen)

        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()
        self.login_screen.pack()

    def show_book_management_screen(self):
        self.clear_screen()
        self.book_management_screen.pack()

    def show_list_books_screen(self):
        self.clear_screen()
        self.list_books_screen.pack()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.pack_forget()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop() 