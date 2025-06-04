# Importa la clase base LanguageStrategy desde el módulo i18n.strategy
from i18n.strategy import LanguageStrategy

# Define la clase English, que implementa la estrategia de idioma en inglés
class English(LanguageStrategy):
    # Constructor de la clase English
    def __init__(self):
        # Diccionario que contiene todos los textos en inglés utilizados en la interfaz
        self.texts = {
            "title": "Employee COVID Control",           # Título principal de la aplicación
            "save": "Save",                              # Texto del botón para guardar
            "update": "Update",                          # Texto del botón para actualizar
            "view": "View Records",                      # Texto del botón para ver los registros
            "edit_selected": "Edit selected",            # Texto del botón para editar un registro seleccionado
            "success": "Data saved successfully.",       # Mensaje de éxito al guardar los datos
            # Diccionario anidado con las etiquetas de los campos del formulario
            "fields": {
                "name": "Name",                                  # Campo: nombre
                "address": "Address",                            # Campo: dirección
                "locality": "Locality",                          # Campo: localidad
                "contacts": "People you live with",              # Campo: convivientes
                "health_status": "Health Status",                # Campo: estado de salud
                "comorbidities": "Comorbidities",                # Campo: comorbilidades
                "covid_positive": "Had COVID?",                  # Campo: si tuvo COVID
                "severity": "Severity Level",                    # Campo: nivel de afectación
                "temperature": "Temperature",                    # Campo: temperatura
                "contact_with_infected": "Contact with infected?",  # Campo: contacto con infectados
                "mood": "Emotional State"                        # Campo: estado emocional
            }
        }

    # Método que devuelve el valor del texto asociado a una clave dada
    def get(self, key):
        return self.texts.get(key, key)  # Si la clave no existe, retorna la misma clave como valor por defecto
