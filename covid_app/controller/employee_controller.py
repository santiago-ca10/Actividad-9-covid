from model.employee import Employee           # Importa la clase Employee para crear instancias
from model.data_store import DataStore       # Importa DataStore para manejar la persistencia de datos

class EmployeeController:
    """
    Controlador que maneja la lógica relacionada con los empleados.
    Se comunica con los modelos Employee y DataStore.
    """

    def __init__(self):
        """
        Inicializa el controlador creando una instancia del almacén de datos (Singleton).
        """
        self.store = DataStore()

    def add_employee(self, **kwargs):
        """
        Crea un nuevo empleado a partir de los datos recibidos y lo guarda en el almacén.

        Parámetros:
        **kwargs -- Diccionario de atributos necesarios para instanciar un Employee.
        """
        employee = Employee(**kwargs)
        self.store.add_employee(employee)

    def update_employee(self, index, updated_data):
        """
        Actualiza la información de un empleado existente.

        Parámetros:
        index -- Índice del empleado en la lista.
        updated_data -- Diccionario con los nuevos datos.
        """
        self.store.update_employee(index, updated_data)

    def list_employees(self):
        """
        Retorna la lista de todos los empleados registrados.

        Retorna:
        Lista de diccionarios con los datos de los empleados.
        """
        return self.store.get_all()
