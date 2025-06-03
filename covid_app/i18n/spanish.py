from i18n.strategy import LanguageStrategy

class Spanish(LanguageStrategy):
    def __init__(self):
        self.texts = {
            "title": "Control de Empleados - COVID",
            "save": "Guardar",
            "update": "Actualizar",
            "view": "Ver registros",
            "edit_selected": "Editar seleccionado",
            "success": "Datos guardados correctamente.",
            "fields": {
                "name": "Nombre",
                "address": "Dirección",
                "locality": "Localidad",
                "contacts": "Convivientes",
                "health_status": "Estado de salud",
                "comorbidities": "Comorbilidades",
                "covid_positive": "¿Tuvo COVID?",
                "severity": "Nivel de afectación",
                "temperature": "Temperatura",
                "contact_with_infected": "¿Contacto con infectados?",
                "mood": "Estado emocional"
            }
        }

    def get(self, key):
        return self.texts.get(key, key)
