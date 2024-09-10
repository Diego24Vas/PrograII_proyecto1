class Menu:
    def __init__(self):
        self.lista_ingredientes: []
        
    def generar_menu(self):
        # Limpiar los datos anteriores
        self.menu_datos.clear()

        # Obtener todos los ingredientes del Treeview
        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            self.menu_datos.append(values)

        # Aquí podrías hacer algo más con los datos, como mostrarlos en la segunda pestaña
        self.actualizar_treeview_pedido()
