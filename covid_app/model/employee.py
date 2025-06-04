import datetime  # Módulo para trabajar con fechas

class Employee:
    """
    Representa a un empleado con información personal, clínica y su historial diario.
    """

    def __init__(self, name, address, locality, contacts, health_status,
                 comorbidities, temperature, contact_with_infected,
                 covid_positive, severity, mood):
        """
        Inicializa un nuevo empleado con sus datos básicos y un primer registro diario.
        """
        self.name = name  # Nombre del empleado
        self.address = address  # Dirección del empleado
        self.locality = locality  # Localidad de residencia
        self.contacts = contacts  # Personas con las que convive o se relaciona
        self.health_status = health_status  # Estado de salud general (ej: sano, enfermo)
        self.comorbidities = comorbidities  # Enfermedades preexistentes
        self.covid_positive = covid_positive  # Si el empleado ha dado positivo en COVID-19
        self.severity = severity  # Nivel de afectación en caso de estar contagiado
        self.history = []  # Historial de registros diarios

        # Se agrega el primer registro diario automáticamente al crearlo
        self.add_daily_record(temperature, contact_with_infected, mood)

    def add_daily_record(self, temperature, contact, mood):
        """
        Agrega un registro diario al historial del empleado.
        Incluye temperatura, contacto con infectados, estado de ánimo, y asistencia.
        """
        try:
            temp = float(temperature)  # Convierte la temperatura a número
        except ValueError:
            temp = 0.0  # Si no es válida, se asigna 0.0 por defecto

        # Registro diario estructurado
        record = {
            "fecha": datetime.date.today().isoformat(),  # Fecha actual en formato ISO
            "temperatura": temp,
            "estado_animo": mood,
            "contacto_con_infectado": contact,
            "puede_asistir": temp <= 37.5 and contact.lower() != "sí"  # Regla para determinar si puede asistir al trabajo
        }

        self.history.append(record)  # Se agrega al historial

    def to_dict(self):
        """
        Convierte el objeto empleado en un diccionario para su serialización.
        """
        return self.__dict__  # Devuelve todos los atributos como diccionario

