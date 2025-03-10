import tkinter as tk
from tkinter import ttk

class LoginScreen(ttk.Frame):
    def __init__(self, parent, on_login):
        super().__init__(parent)
        self.on_login = on_login
        self.create_widgets()

    def create_widgets(self):
        self.pack(pady=50)

        ttk.Label(self, text="Email:", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.email_entry = ttk.Entry(self, width=30)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Senha:", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = ttk.Entry(self, show="*", width=30)
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        login_button = ttk.Button(self, text="Login", command=self.on_login)
        login_button.grid(row=2, column=0, columnspan=2, pady=20) 