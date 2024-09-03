class Inventario:
    def __init__(self):
        self.lista_ingredientes = []

    def agregar_ingediente(self, ingrediente):
        self.lista_ingredientes.append(ingrediente)
        return True  # ingrediente agregado como nuevo

    def eliminar_ingrediente(self, nombre_ingrediente, cantidad=1):
        for ingr in self.lista_ingredientes:
            if ingr.nombre == nombre_ingrediente:
                self.lista_ingredientes.remove(ingr)
                return True
            else: 
                return False



    def obtener_ingredientes(self):
        return [ingredientes for ingredientes in self.lista_ingredientes]
