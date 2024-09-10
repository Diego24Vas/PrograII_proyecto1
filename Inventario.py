class Inventario:
    def __init__(self):
        self.lista_ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        for ingr in self.lista_ingredientes:
            if ingr.nombre == ingrediente.nombre:
                ingr.cantidad += ingrediente.cantidad
                return True
        self.lista_ingredientes.append(ingrediente)
        return True  # ingrediente agregado como nuevo

    def eliminar_ingrediente(self, nombre_ingrediente):
        for ingr in self.lista_ingredientes:
            if ingr.nombre == nombre_ingrediente:
                self.lista_ingredientes.remove(ingr)
                return True
        return False  # ingrediente no encontrado


    def obtener_ingredientes(self):
        return [ingrediente for ingrediente in self.lista_ingredientes]
