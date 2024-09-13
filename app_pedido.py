import customtkinter as ctk
from tkinter import ttk
from Ingredientes import Ingredientes
from Inventario import Inventario
from PDF import GeneradorPDF
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
        
        # Definir el diccionario de precios aquí
        self.precios = {
            "Papas Fritas": 500,
            "Pepsi": 1100,
            "Completo": 1800,
            "Hamburguesa": 3500
        }

        # Crear pestañas
        self.tabview = ctk.CTkTabview(self, width=600, height=500)
        self.tabview.pack(padx=20, pady=20)

        self.crear_pestanas()

        # Asegúrate de actualizar el estado de los menús al inicio
        self.actualizar_estado_menus()

    def crear_pestanas(self):
        # Crear y configurar las pestañas
        self.tab1 = self.tabview.add("Ingreso de ingredientes")
        self.tab2 = self.tabview.add("Pedido")

        # Configurar el contenido de las pestañas
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
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

    def configurar_pestana2(self):
        tarjetas_frame = ctk.CTkFrame(self.tab2)
        tarjetas_frame.pack(side="top", fill="both", padx=10, pady=10)


        # Cargar imágenes y crear botones con imágenes, deshabilitados por defecto
        image_Bebida = ctk.CTkImage(Image.open("IMG/Comida1.png"), size=(100, 100))
        self.boton_Bebida = ctk.CTkButton(tarjetas_frame, image=image_Bebida, text="Pepsi", width=100, height=50,
                                      state="disabled",  # Deshabilitado por defecto
                                      command=lambda: self.agregar_pedido("Pepsi"))
        self.boton_Bebida.pack(side="left", padx=10, pady=10)

        image_Hamburguesa = ctk.CTkImage(Image.open("IMG/Comida2.png"), size=(100, 100))
        self.boton_Hamburguesa = ctk.CTkButton(tarjetas_frame, image=image_Hamburguesa, text="Hamburguesa", width=100, height=50,
                                            command=lambda: self.agregar_pedido("Hamburguesa"))
        self.boton_Hamburguesa.pack(side="left", padx=10, pady=10)

        image_Completo = ctk.CTkImage(Image.open("IMG/Comida3.png"), size=(100, 100))
        self.boton_Completo = ctk.CTkButton(tarjetas_frame, image=image_Completo, text="Completo", width=100, height=50,
                                        state="disabled",  # Deshabilitado por defecto
                                        command=lambda: self.agregar_pedido("Completo"))
        self.boton_Completo.pack(side="left", padx=10, pady=10)

        image_Papas = ctk.CTkImage(Image.open("IMG/Comida4.png"), size=(100, 100))
        self.boton_Papas = ctk.CTkButton(tarjetas_frame, image=image_Papas, text="Papas Fritas", width=100, height=50,
                                     state="disabled",  # Deshabilitado por defecto
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

        # Botón para eliminar menú
        self.boton_Elimenu = ctk.CTkButton(frame_treeview2, text="Eliminar Menu", fg_color="red", text_color="white")
        self.boton_Elimenu.configure(command=self.eliminar_pedido)
        self.boton_Elimenu.pack(pady=10)

        self.boton_pdf = ctk.CTkButton(frame_treeview2, text="Generar Boleta", fg_color="green", text_color="white", command=self.generar_pdf)
        self.boton_pdf.pack(pady=10)
        
        
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

    def eliminar_pedido(self):
        seleccion = self.tree_pedido.selection()
        if not seleccion:
            CTkMessagebox(title="Error", message="Por favor selecciona un pedido para eliminar.", icon="warning")
            return

        item = self.tree_pedido.item(seleccion)
        pedido = item['values'][0]
        cantidad = item['values'][1]

        # Diccionario con los ingredientes necesarios para cada menú
        ingredientes_menus = {
            "Pepsi": {"bebida": 1},
            "Hamburguesa": {"pan de hamburguesa": 1, "lámina de queso": 1, "churrasco de carne": 1},
            "Completo": {"vienesa": 1, "pan de completo": 1, "tomate": 1, "palta": 1},
            "Papas Fritas": {"papas": 5}
        }

        if pedido in ingredientes_menus:
            ingredientes_necesarios = ingredientes_menus[pedido]
            for ingrediente, cantidad_necesaria in ingredientes_necesarios.items():
                cantidad_total = cantidad_necesaria * cantidad
                self.inventario.agregar_ingrediente(Ingredientes(ingrediente, cantidad_total))

        # Eliminar el pedido del Treeview
        self.tree_pedido.delete(seleccion)

        # Actualizar el Treeview de ingredientes
        self.actualizar_treeview()
        # Actualizar el estado de los botones de los platillos
        self.actualizar_estado_menus()


    def generar_pdf(self):
        pedidos = []
        for item in self.tree_pedido.get_children():
            pedido = self.tree_pedido.item(item)["values"]
            pedidos.append(pedido)
        
        generador = GeneradorPDF(pedidos)
        generador.generar_pdf()
        
        CTkMessagebox(title="PDF Generado", message="La boleta ha sido generada exitosamente.", icon="check")

    def agregar_pedido(self, pedido):
        # Verificar que el pedido exista en el diccionario de precios
        if pedido not in self.precios:
            CTkMessagebox(title="Error", message="Pedido no válido.", icon="warning")
            return
        
        # Definir los ingredientes necesarios para cada platillo
        ingredientes_menus = {
            "Pepsi": {"bebida": 1},
            "Hamburguesa": {"pan de hamburguesa": 1, "lamina de queso": 1, "churrasco de carne": 1},
            "Completo": {"vienesa": 1, "pan de completo": 1, "tomate": 1, "palta": 1},
            "Papas Fritas": {"papas": 5}
        }
        
        # Obtener la cantidad necesaria para cada platillo
        ingredientes_necesarios = ingredientes_menus.get(pedido, {})
        
        # Verificar disponibilidad antes de agregar el pedido
        if not self.inventario.verificar_disponibilidad(ingredientes_necesarios):
            CTkMessagebox(title="Error", message="Ingredientes insuficientes para el pedido.", icon="warning")
            return
        
        # Descontar los ingredientes del inventario
        for nombre, cantidad in ingredientes_necesarios.items():
            for ingr in self.inventario.lista_ingredientes:
                if ingr.nombre == nombre:
                    ingr.cantidad -= cantidad
                    if ingr.cantidad <= 0:
                        self.inventario.eliminar_ingrediente(nombre)
                    break
        
        # Agregar o actualizar el pedido en el Treeview
        precio_unitario = self.precios[pedido]
        cantidad = 1  # Puedes ajustar esto para que el usuario seleccione la cantidad
        
        # Buscar si el platillo ya existe en el Treeview
        for item in self.tree_pedido.get_children():
            valores = self.tree_pedido.item(item, "values")
            if valores[0] == pedido:
                # Convertir valores a enteros para la actualización
                cantidad_actual = int(valores[1])
                precio_actual = float(valores[2])
                
                # Actualizar cantidad y precio total
                nueva_cantidad = cantidad_actual + cantidad
                nuevo_precio = nueva_cantidad * precio_unitario
                
                # Actualizar el Treeview
                self.tree_pedido.item(item, values=(pedido, nueva_cantidad, nuevo_precio))
                break
        else:
            # Agregar nuevo pedido
            self.tree_pedido.insert("", "end", values=(pedido, cantidad, precio_unitario))
        
        # Actualizar ambos Treeviews
        self.actualizar_treeview()  # Actualizar el Treeview de ingredientes
        self.actualizar_estado_menus()  # Actualizar la disponibilidad de los platillos

       


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

        if not self.validar_nombre(nombre):
            return

        if not self.validar_numero(cantidad):
            return

        ingrediente = Ingredientes(nombre, int(cantidad))

        if self.inventario.agregar_ingrediente(ingrediente):
            self.actualizar_treeview()
            self.actualizar_estado_menus()  # Asegúrate de que esta función se llama aquí


    def actualizar_estado_menus(self):
        ingredientes_menus = {
            "Pepsi":       {"bebida": 1},
            "Hamburguesa": {"pan de hamburguesa": 1, "lamina de queso": 1, "churrasco de carne": 1},
            "Completo":    {"vienesa": 1, "pan de completo": 1, "tomate": 1, "palta": 1},
            "Papas Fritas":{"papas": 5}
        }

        for menu, ingredientes in ingredientes_menus.items():
            if self.inventario.verificar_disponibilidad(ingredientes):
                boton = getattr(self, f"boton_{menu.replace(' ', '_')}", None)
                if boton:
                    boton.configure(state="normal")
            else:
                boton = getattr(self, f"boton_{menu.replace(' ', '_')}", None)
                if boton:
                    boton.configure(state="disabled")

                
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


    def actualizar_treeview(self):
        # Limpiar el Treeview actual
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Agregar todos los ingredientes de la biblioteca al Treeview
        for ingrediente in self.inventario.obtener_ingredientes():
            self.tree.insert("", "end", values=(ingrediente.nombre, ingrediente.cantidad))

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