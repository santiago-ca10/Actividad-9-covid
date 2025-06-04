import json  # Para leer y escribir archivos JSON
import os    # Para verificar y crear rutas de archivos

class DataStore:
    """
    Clase Singleton responsable de gestionar el almacenamiento y recuperación
    de los empleados desde un archivo JSON.
    """
    _instance = None  # Atributo de clase para mantener una única instancia
    _file_path = "data/employees.json"  # Ruta al archivo JSON donde se guardan los datos

    def __new__(cls):
        """
        Implementación del patrón Singleton: solo se permite una instancia.
        Si no existe, la crea y carga los datos.
        """
        if cls._instance is None:
            cls._instance = super(DataStore, cls).__new__(cls)
            cls._instance.load()
        return cls._instance

    def load(self):
        """
        Carga la lista de empleados desde el archivo JSON.
        Si el archivo no existe, inicializa la lista vacía.
        """
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as f:
                self.employees = json.load(f)  # Carga los datos del archivo
        else:
            self.employees = []  # Lista vacía si no hay datos previos

    def save(self):
        """
        Guarda la lista actual de empleados en el archivo JSON.
        Crea el directorio si no existe.
        """
        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)
        with open(self._file_path, 'w') as f:
            json.dump(self.employees, f, indent=4)  # Guarda con formato legible

    def add_employee(self, employee):
        """
        Añade un nuevo empleado a la lista y guarda los cambios.
        """
        self.employees.append(employee.to_dict())  # Convierte el objeto a diccionario
        self.save()

    def update_employee(self, index, updated_data):
        """
        Actualiza los datos de un empleado en la posición indicada.
        """
        self.employees[index] = updated_data
        self.save()

    def get_all(self):
        """
        Devuelve la lista completa de empleados.
        """
        return self.employees
