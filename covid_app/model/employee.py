import datetime

class Employee:
    def __init__(self, name, address, locality, contacts, health_status,
                 comorbidities, temperature, contact_with_infected,
                 covid_positive, severity, mood):
        self.name = name
        self.address = address
        self.locality = locality
        self.contacts = contacts
        self.health_status = health_status
        self.comorbidities = comorbidities
        self.covid_positive = covid_positive
        self.severity = severity
        self.history = []

        self.add_daily_record(temperature, contact_with_infected, mood)

    def add_daily_record(self, temperature, contact, mood):
        try:
            temp = float(temperature)
        except ValueError:
            temp = 0.0

        record = {
            "fecha": datetime.date.today().isoformat(),
            "temperatura": temp,
            "estado_animo": mood,
            "contacto_con_infectado": contact,
            "puede_asistir": temp <= 37.5 and contact.lower() != "sí"
        }
        self.history.append(record)

    def to_dict(self):
        return self.__dict__
