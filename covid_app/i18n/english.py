from i18n.strategy import LanguageStrategy

class English(LanguageStrategy):
    def __init__(self):
        self.texts = {
            "title": "Employee COVID Control",
            "save": "Save",
            "update": "Update",
            "view": "View Records",
            "edit_selected": "Edit selected",
            "success": "Data saved successfully.",
            "fields": {
                "name": "Name",
                "address": "Address",
                "locality": "Locality",
                "contacts": "People you live with",
                "health_status": "Health Status",
                "comorbidities": "Comorbidities",
                "covid_positive": "Had COVID?",
                "severity": "Severity Level",
                "temperature": "Temperature",
                "contact_with_infected": "Contact with infected?",
                "mood": "Emotional State"
            }
        }

    def get(self, key):
        return self.texts.get(key, key)
