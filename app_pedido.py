import customtkinter as ctk
from tkinter import ttk
from Ingredientes import Ingredientes
from Inventario import Inventario
import re
from CTkMessagebox import CTkMessagebox
from menu import Menu

class AplicacionConPestanas(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Mcdonals")
        self.geometry("1200x700")

        # Inicializar la Biblioteca
        self.inventario = Inventario()

        # Lista para almacenar los datos del menú
        self.menu_datos = Menu[]

        # Crear pestañas
        self.tabview = ctk.CTkTabview(self, width=600, height=500)
        self.tabview.pack(padx=20, pady=20)

        self.crear_pestanas()

    def crear_pestanas(self):
        # Crear y configurar las pestañas
        self.tab1 = self.tabview.add("Ingreso de ingredientes")
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

        label_ingrediente = ctk.CTkLabel(frame_formulario, text="")
        label_ingrediente.pack(pady=2)
        self.entry_ingrediente = ctk.CTkEntry(frame_formulario, placeholder_text="Ingrediente")
        self.entry_ingrediente.pack(pady=2)

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

        # Botón para generar el menú
        self.boton_menu = ctk.CTkButton(frame_treeview, text="Generar Menú")
        self.boton_menu.configure(command=self.generar_menu)
        self.boton_menu.pack(pady=10, side="bottom")

        # Treeview en el segundo frame
        self.tree = ttk.Treeview(frame_treeview, columns=("Ingrediente", "Cantidad"), show="headings")
        self.tree.heading("Ingrediente", text="Ingrediente")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

    def configurar_pestana2(self):
        tarjetas_frame = ctk.CTkFrame(self.tab2)
        tarjetas_frame.pack(side="top", fill="both", padx=10, pady=10)

        frame_treeview2 = ctk.CTkFrame(self.tab2)
        frame_treeview2.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)

        self.tree_pedido = ttk.Treeview(frame_treeview2, columns=("Menu", "Cantidad", "Precio"), show="headings")
        self.tree_pedido.heading("Menu", text="Menu")
        self.tree_pedido.heading("Cantidad", text="Cantidad")
        self.tree_pedido.heading("Precio", text="Precio Unitario")
        self.tree_pedido.pack(expand=True, fill="both", padx=10, pady=10)

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
        nombre = self.entry_ingrediente.get()
        cantidad = self.entry_cantidad.get()
        self.entry_cantidad.delete(0, ctk.END)
        self.entry_ingrediente.delete(0, ctk.END)
    
        # Validar entradas
        if not self.validar_nombre(nombre):
            return

        if not self.validar_numero(cantidad):
            return

        # Crear una instancia de ingrediente
        ingrediente = Ingredientes(nombre, cantidad)

        # Agregar el ingrediente al inventario
        if self.inventario.agregar_ingrediente(ingrediente):
            self.actualizar_treeview()
        else:
            CTkMessagebox(title="Error", message="El Ingrediente ya existe en el inventario.", icon="warning")

    def eliminar_ingrediente(self):
        seleccion = self.tree.selection()
        if not seleccion:
            CTkMessagebox(title="Error", message="Por favor selecciona un ingrediente para eliminar.", icon="warning")
            return

        item = self.tree.item(seleccion)
        nombre = item['values'][0]

        # Eliminar el ingrediente del inventario
        if self.inventario.eliminar_ingrediente(nombre):
            self.actualizar_treeview()
        else:
            CTkMessagebox(title="Error", message="El ingrediente no se pudo eliminar.", icon="warning")


    def actualizar_treeview(self):
        # Limpiar el Treeview actual
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Agregar todos los ingredientes del inventario al Treeview
        for ingrediente in self.inventario.obtener_ingredientes():
            self.tree.insert("", "end", values=(ingrediente.nombre, ingrediente.cantidad))



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
