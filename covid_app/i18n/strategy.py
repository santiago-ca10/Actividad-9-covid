# Define la clase base abstracta para implementar el patrón Strategy de idiomas
class LanguageStrategy:
    
    # Método que deben implementar todas las clases hijas (como English o Spanish)
    def get(self, key):
        # Lanza una excepción si no se implementa el método en la subclase
        raise NotImplementedError("Implementa este método en tu idioma")

