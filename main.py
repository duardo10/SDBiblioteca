import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from telas.gerenciador_telas import get_tela_login

class Aplicacao(ttk.Window):
    def __init__(self):
        super().__init__(themename="solar")
        self.title("Login e Cadastro")
        self.geometry("1280x832")

        # Mostrar a tela de login ao iniciar
        self.after(0, self.mostrar_tela, get_tela_login)  # Chamar depois que Tkinter estiver pronto

    def mostrar_tela(self, tela_func):
        for widget in self.winfo_children():
            widget.destroy()

        container = ttk.Frame(self)
        container.pack(expand=True, fill="both")
        tela_func()(container, self)  # Executando a função aqui, garantindo que funcione

if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()
