# Importa la clase MainWindow desde el módulo view.main_window
from view.main_window import MainWindow

# Verifica si el archivo se está ejecutando como programa principal
if __name__ == "__main__":
    # Crea una instancia de la ventana principal de la aplicación
    app = MainWindow()
    # Ejecuta la aplicación
    app.run()
