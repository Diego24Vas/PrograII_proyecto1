class Ingredientes:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre.lower()
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.cantidad} x {self.nombre}"