class Menu:
    def __init__(self, nombre, precio, ingredientes, inventario):
        self.nombre = nombre
        self.precio = precio
        self.ingredientes = ingredientes
        self.inventario = inventario

    def generar_menu(self):
        # Verificar si los ingredientes están disponibles en el inventario
        if self.inventario.verificar_disponibilidad(self.ingredientes):
            self.inventario.consumir_ingredientes(self.ingredientes)
        else:
            print(f"No hay suficientes ingredientes para crear el menú '{self.nombre}'.")
