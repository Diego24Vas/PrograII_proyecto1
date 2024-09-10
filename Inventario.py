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

    def verificar_disponibilidad(self, ingredientes_necesarios):
        # Verifica si hay suficientes ingredientes disponibles
        for nombre_ingrediente, cantidad_necesaria in ingredientes_necesarios.items():
            for ingrediente in self.lista_ingredientes:
                if ingrediente.nombre == nombre_ingrediente:
                    if ingrediente.cantidad < cantidad_necesaria:
                        return False  # No hay suficiente de este ingrediente
                    break
            else:
                return False  # Ingrediente no encontrado
        return True