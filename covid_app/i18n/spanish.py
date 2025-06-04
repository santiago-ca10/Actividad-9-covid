# Importa la clase base LanguageStrategy desde el módulo i18n.strategy.
from i18n.strategy import LanguageStrategy

# Define la clase Spanish que hereda de LanguageStrategy.
class Spanish(LanguageStrategy):
    # Constructor de la clase Spanish
    def __init__(self):
        # Diccionario que contiene todos los textos en español utilizados en la interfaz
        self.texts = {
            "title": "Control de Empleados - COVID",  # Título de la ventana
            "save": "Guardar",                        # Texto para el botón de guardar
            "update": "Actualizar",                   # Texto para el botón de actualizar
            "view": "Ver registros",                  # Texto para ver registros
            "edit_selected": "Editar seleccionado",   # Texto del botón para editar un registro seleccionado
            "success": "Datos guardados correctamente.",  # Mensaje al guardar con éxito
            # Diccionario anidado con etiquetas de campos en español
            "fields": {
                "name": "Nombre",                              # Campo de nombre
                "address": "Dirección",                        # Campo de dirección
                "locality": "Localidad",                       # Campo de localidad
                "contacts": "Convivientes",                    # Campo de convivientes
                "health_status": "Estado de salud",            # Campo de estado de salud
                "comorbidities": "Comorbilidades",             # Campo de comorbilidades
                "covid_positive": "¿Tuvo COVID?",              # Campo para indicar si tuvo COVID
                "severity": "Nivel de afectación",             # Campo para nivel de afectación
                "temperature": "Temperatura",                  # Campo de temperatura
                "contact_with_infected": "¿Contacto con infectados?",  # Campo de contacto con infectados
                "mood": "Estado emocional"                     # Campo de estado emocional
            }
        }

    # Método que devuelve el valor asociado a una clave del diccionario de textos.
    def get(self, key):
        return self.texts.get(key, key)  # Si no encuentra la clave, devuelve la misma clave
