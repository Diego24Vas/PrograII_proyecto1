import customtkinter as ctk
from tkinter import ttk
from Ingredientes import Ingredientes
from Inventario import Inventario
from menu import Menu

import re
from CTkMessagebox import CTkMessagebox
from PIL import Image


class AplicacionConPestanas(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Mcdonals")
        self.geometry("1200x700")

        # Inicializar la Biblioteca
        self.inventario = Inventario()


        # Lista para almacenar los datos del menú
        self.menu_datos = Menu()

        # Crear pestañas
        self.tabview = ctk.CTkTabview(self, width=600, height=500)
        self.tabview.pack(padx=20, pady=20)

        self.crear_pestanas()

    def crear_pestanas(self):
        # Crear y configurar las pestañas
        self.tab1 = self.tabview.add("Ingreso de ingedientes")
        self.tab2 = self.tabview.add("Pedido")

        # Configurar el contenido de la pestaña 1
        self.configurar_pestana1()
        self.configurar_pestana2()

    def configurar_pestana1(self):
        # Dividir la pestaña en dos frames
        frame_formulario = ctk.CTkFrame(self.tab1)
        frame_formulario.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        frame_treeview = ctk.CTkFrame(self.tab1)
        frame_treeview.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Formulario Nombre del ingrediente
        label_ingediente = ctk.CTkLabel(frame_formulario, text="")
        label_ingediente.pack(pady=2)
        self.entry_ingediente = ctk.CTkEntry(frame_formulario, placeholder_text="Ingrediente")
        self.entry_ingediente.pack(pady=2)

        # Formulario cantidad
        label_cantidad = ctk.CTkLabel(frame_formulario, text="")
        label_cantidad.pack(pady=2)
        self.entry_cantidad = ctk.CTkEntry(frame_formulario, placeholder_text="Cantidad")
        self.entry_cantidad.pack(pady=2)

        # Botón de ingreso
        self.boton_ingresar = ctk.CTkButton(frame_formulario, text="Ingresar Ingrediente")
        self.boton_ingresar.configure(command=self.ingresar_ingrediente)
        self.boton_ingresar.pack(pady=100)

        # Botón para eliminar ingrediente
        self.boton_eliminar = ctk.CTkButton(frame_treeview, text="Eliminar Ingrediente", fg_color="black", text_color="white")
        self.boton_eliminar.configure(command=self.eliminar_ingrediente)
        self.boton_eliminar.pack(pady=10)




        # Treeview en el segundo frame
        self.tree = ttk.Treeview(frame_treeview, columns=("Ingrediente", "Cantidad"), show="headings")
        self.tree.heading("Ingrediente", text="Ingrediente")

        # Treeview para ingredientes
        self.tree = ttk.Treeview(frame_treeview, columns=("Ingediente", "Cantidad"), show="headings")
        self.tree.heading("Ingediente", text="Ingrediente")

        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

    def configurar_pestana2(self):
        tarjetas_frame = ctk.CTkFrame(self.tab2)
        tarjetas_frame.pack(side="top", fill="both", padx=10, pady=10)


        # Cargar la imagen
        image_Bebida = ctk.CTkImage(Image.open("IMG/Comida1.png"), size=(100, 100))
        # Crear un botón con imagen

        # Cargar la imagen
        image_Hamburguesa = ctk.CTkImage(Image.open("IMG/Comida2.png"), size=(100, 100))
        # Crear un botón con imagen

        # Cargar la imagen
        image_Completo = ctk.CTkImage(Image.open("IMG/Comida3.png"), size=(100, 100))
        # Crear un botón con imagen

        # Cargar la imagen
        image_Papas = ctk.CTkImage(Image.open("IMG/Comida4.png"), size=(100, 100))
        # Crear un botón con imagen

        


        self.precios = {
            "Papas Fritas": 500,
            "Pepsi": 1100,
            "Completo": 1800,
            "Hamburguesa": 3500
        }

        # Botones con imágenes y asignación de pedidos
        image_Bebida = ctk.CTkImage(Image.open("IMG/Comida1.png"), size=(100, 100))
        self.boton_Bebida = ctk.CTkButton(tarjetas_frame, image=image_Bebida, text="Pepsi", width=100, height=50,
                                          command=lambda: self.agregar_pedido("Pepsi"))
        self.boton_Bebida.pack(side="left", padx=10, pady=10)

        image_Hamburguesa = ctk.CTkImage(Image.open("IMG/Comida2.png"), size=(100, 100))
        self.boton_Hamburguesa = ctk.CTkButton(tarjetas_frame, image=image_Hamburguesa, text="Hamburguesa", width=100, height=50,
                                               command=lambda: self.agregar_pedido("Hamburguesa"))
        self.boton_Hamburguesa.pack(side="left", padx=10, pady=10)

        image_Completo = ctk.CTkImage(Image.open("IMG/Comida3.png"), size=(100, 100))
        self.boton_Completo = ctk.CTkButton(tarjetas_frame, image=image_Completo, text="Completo", width=100, height=50,
                                          command=lambda: self.agregar_pedido("Completo"))
        self.boton_Completo.pack(side="left", padx=10, pady=10)

        image_Papas = ctk.CTkImage(Image.open("IMG/Comida4.png"), size=(100, 100))
        self.boton_Papas = ctk.CTkButton(tarjetas_frame, image=image_Papas, text="Papas", width=100, height=50,
                                         command=lambda: self.agregar_pedido("Papas Fritas"))
        self.boton_Papas.pack(side="left", padx=10, pady=10)

        # Treeview para pedidos

        frame_treeview2 = ctk.CTkFrame(self.tab2)
        frame_treeview2.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)

        self.tree_pedido = ttk.Treeview(frame_treeview2, columns=("Menu", "Cantidad", "Precio"), show="headings")
        self.tree_pedido.heading("Menu", text="Menu")
        self.tree_pedido.heading("Cantidad", text="Cantidad")
        self.tree_pedido.heading("Precio", text="Precio Unitario")
        self.tree_pedido.pack(expand=True, fill="both", padx=10, pady=10)


        # Botón para eliminar menu arriba del Treeview
        self.boton_Elimenu = ctk.CTkButton(frame_treeview2, text="Eliminar Menu", fg_color="red", text_color="white")
        self.boton_Elimenu.configure(command=self.eliminar_ingrediente) 
        self.boton_Elimenu.pack(pady=10)

        self.boton_pdf = ctk.CTkButton(frame_treeview2, text="Generar Boleta", fg_color="green", text_color="white")
        self.boton_pdf.pack(pady=10)




    def agregar_pedido(self, pedido):
        precio = self.precios[pedido]
        cantidad = 1  # Puedes ajustar esto para que el usuario seleccione la cantidad
        self.tree_pedido.insert("", "end", values=(pedido, cantidad, precio))

    def validar_nombre(self, nombre):
        if re.match(r"^[a-zA-Z\s]+$", nombre):
            return True
        else:
            CTkMessagebox(title="Error de Validación", message="El nombre debe contener solo letras y espacios.", icon="warning")
            return False

    def validar_numero(self, cantidad):
        if re.match(r"^\d+$", cantidad):
            return True
        else:
            CTkMessagebox(title="Error de Validación", message="La cantidad debe contener solo números.", icon="warning")
            return False

    def ingresar_ingrediente(self):
        nombre = self.entry_ingediente.get()
        cantidad = self.entry_cantidad.get()

        self.entry_cantidad.delete(0, ctk.END)
        self.entry_ingediente.delete(0, ctk.END)

        # Validar entradas
        if not self.validar_nombre(nombre):
            return

        if not self.validar_numero(cantidad):
            return

        # Crear una instancia de ingrediente
        ingrediente = Ingredientes(nombre, int(cantidad))

        if self.inventario.agregar_ingrediente(ingrediente):
            self.actualizar_treeview()
            self.actualizar_estado_menus()  # función para actualizar los menús según los ingredientes
        


    def actualizar_estado_menus(self):
        # Diccionario con los ingredientes necesarios para cada menú
        ingredientes_menus = {
            "Pepsi":       {"bebida": 1},
            "Hamburguesa": {"pan de hamburguesa": 1, "lámina de queso": 1, "churrasco de carne": 1},
            "Completo":    {"vienesa": 1, "pan de completo": 1, "tomate": 1, "palta": 1},
            "Papas Fritas":{"papas": 5}
        }


        # Verificar disponibilidad y habilitar/deshabilitar los botones según los ingredientes
        if self.inventario.verificar_disponibilidad(ingredientes_menus["Pepsi"]):
            self.boton_Bebida.configure(state="normal")
        else:
            self.boton_Bebida.configure(state="disabled")

        if self.inventario.verificar_disponibilidad(ingredientes_menus["Hamburguesa"]):
            self.boton_Hamburguesa.configure(state="normal")
        else:
            self.boton_Hamburguesa.configure(state="disabled")

        if self.inventario.verificar_disponibilidad(ingredientes_menus["Completo"]):
            self.boton_Completo.configure(state="normal")
        else:
            self.boton_Completo.configure(state="disabled")

        if self.inventario.verificar_disponibilidad(ingredientes_menus["Papas Fritas"]):
            self.boton_Papas.configure(state="normal")
        else:
            self.boton_Papas.configure(state="disabled")



    def eliminar_ingrediente(self):
        seleccion = self.tree.selection()
        if not seleccion:
            CTkMessagebox(title="Error", message="Por favor selecciona un ingrediente para eliminar.", icon="warning")
            return

        item = self.tree.item(seleccion)
        nombre = item['values'][0]

        # Eliminar el ingrediente de inventario
        if self.inventario.eliminar_ingrediente(nombre):
            self.actualizar_treeview()
        else:
            CTkMessagebox(title="Error", message="El Ingrediente no se pudo eliminar.", icon="warning")

    def actualizar_treeview(self):
        # Limpiar el Treeview actual
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Agregar todos los ingredientes de la biblioteca al Treeview
        for ingrediente in self.inventario.obtener_ingredientes():
            self.tree.insert("", "end", values=(ingrediente.nombre, ingrediente.cantidad))




    """for item in tree.get_children():
        print(tree.item(item)["values"])"""

    def generar_menu(self):
        # Limpiar los datos anteriores
        self.menu_datos.clear()


    def actualizar_treeview_pedido(self):
        # Limpiar el Treeview de la segunda pestaña
        for item in self.tree_pedido.get_children():
            self.tree_pedido.delete(item)

        # Agregar los datos almacenados en self.menu_datos al Treeview de la segunda pestaña
        for dato in self.menu_datos:
            self.tree_pedido.insert("", "end", values=(dato[0], dato[1], "Precio a definir"))

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = AplicacionConPestanas()
    app.mainloop()
