import customtkinter as ctk
from tkinter import ttk


from Ingredientes import Ingredientes



from Inventario import Inventario
import re
from CTkMessagebox import CTkMessagebox
print("Hola mundo")

class AplicacionConPestanas(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Biblioteca")
        self.geometry("1200x700")

        # Inicializar la Biblioteca
        self.inventario = Inventario()

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

        # Formulario Nombre del libro
        label_ingediente = ctk.CTkLabel(frame_formulario, text="")
        label_ingediente.pack(pady=2)
        self.entry_ingediente = ctk.CTkEntry(frame_formulario, placeholder_text="Ingrediente")
        self.entry_ingediente.pack(pady=2)

        # Formulario cantidad
        label_cantidad = ctk.CTkLabel(frame_formulario, text="")
        label_cantidad.pack(pady=2)
        self.entry_cantidad = ctk.CTkEntry(frame_formulario, placeholder_text="Cantidad")
        self.entry_cantidad.pack(pady=2)


        #Boton de ingreso
        self.boton_ingresar = ctk.CTkButton(frame_formulario, text="Ingresar Ingrediente")
        self.boton_ingresar.configure(command=self.ingresar_ingrediente)
        self.boton_ingresar.pack(pady=100)

        # Botón para eliminar libro arriba del Treeview
        self.boton_eliminar = ctk.CTkButton(frame_treeview, text="Eliminar Ingrediente", fg_color="black", text_color="white")
        self.boton_eliminar.configure(command=self.eliminar_libro)
        self.boton_eliminar.pack(pady=10)

        # Botón para generar el menu
        self.boton_menu = ctk.CTkButton(frame_treeview, text="Generar Menu")
        self.boton_menu.pack(pady=10, side="bottom")

        # Treeview en el segundo frame
        self.tree = ttk.Treeview(frame_treeview, columns=("Ingediente", "Cantidad"), show="headings")
        self.tree.heading("Ingediente", text="Ingrediente")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

    def configurar_pestana2(self):
        tarjetas_frame = ctk.CTkFrame(self.tab2)
        tarjetas_frame.pack(side ="top", fill="both", padx=10, pady=10)




        frame_treeview2 = ctk.CTkFrame(self.tab2)
        frame_treeview2.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)

        self.tree_pedido = ttk.Treeview(frame_treeview2, columns=("Menu","Cantidad", "Precio"), show="headings")
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
            CTkMessagebox(title="Error de Validación", message="La categoria debe contener solo numeros.", icon="warning")
            return False
        


    def ingresar_ingrediente(self):

        nombre = self.entry_ingediente.get()
        cantidad = self.entry_cantidad.get()

        
        # Validar entradas
        if not self.validar_nombre(nombre):
            return

        if not self.validar_numero (cantidad):
            return

        
        # Crear una instancia de Libro
        ingrediente = Ingredientes(nombre,cantidad)
        

        # Agregar el libro a la biblioteca
        if self.ingrediente.agregar_ingrediente(ingrediente):
            self.actualizar_treeview()

        else:
            CTkMessagebox(title="Error", message="El libro ya existe en la biblioteca.", icon="warning")
        

    def eliminar_libro(self):
        seleccion = self.tree.selection()
        if not seleccion:
            CTkMessagebox(title="Error", message="Por favor selecciona un libro para eliminar.", icon="warning")
            return

        item = self.tree.item(seleccion)
        nombre = item['values'][0]

        # Eliminar el libro de la biblioteca
        if self.ingrediente.eliminar_libro(nombre):
            self.actualizar_treeview()
        else:
            CTkMessagebox(title="Error", message="El libro no se pudo eliminar.", icon="warning")

    def actualizar_treeview(self):
        # Limpiar el Treeview actual
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Agregar todos los libros de la biblioteca al Treeview
        for libro in self.ingrediente.obtener_libros():
            self.tree.insert("", "end", values=(libro.nombre, libro.autor, libro.categoria, libro.cantidad))


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = AplicacionConPestanas()
    app.mainloop()
