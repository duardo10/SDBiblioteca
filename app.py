# Este arquivo será o ponto de entrada principal para iniciar a aplicação.
# Configure a inicialização da interface gráfica e a conexão com o Firebase.

from src.gui.main_window import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()