import customtkinter as ctk
from tkinter import ttk
from Ingredientes import Ingredientes
from Inventario import Inventario
import re
from CTkMessagebox import CTkMessagebox
from PIL import Image
from fpdf import FPDF
from tkinter import filedialog, messagebox
from datetime import datetime

class AplicacionConPestanas(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Mcdonals")
        self.geometry("1200x700")

        # Inicializar la Biblioteca
        self.inventario = Inventario()

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

        # Treeview para ingredientes
        self.tree = ttk.Treeview(frame_treeview, columns=("Ingrediente", "Cantidad"), show="headings")
        self.tree.heading("Ingrediente", text="Ingrediente")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

    def configurar_pestana2(self):
        tarjetas_frame = ctk.CTkFrame(self.tab2)
        tarjetas_frame.pack(side="top", fill="both", padx=10, pady=10)

        self.precios = {
            "Papas Fritas": 500,
            "Pepsi": 1100,
            "Completo": 1800,
            "Hamburguesa": 3500
        }

        # Botones con imágenes y asignación de pedidos
        image_Bebida = ctk.CTkImage(Image.open("IMG/Comida1.png"), size=(100, 100))
        self.boton_Bebida = ctk.CTkButton(tarjetas_frame, image=image_Bebida, text="", width=100, height=50,
                                          command=lambda: self.agregar_pedido("Pepsi"))
        self.boton_Bebida.pack(side="left", padx=10, pady=10)

        image_Hamburguesa = ctk.CTkImage(Image.open("IMG/Comida2.png"), size=(100, 100))
        self.boton_Hamburguesa = ctk.CTkButton(tarjetas_frame, image=image_Hamburguesa, text="", width=100, height=50,
                                               command=lambda: self.agregar_pedido("Hamburguesa"))
        self.boton_Hamburguesa.pack(side="left", padx=10, pady=10)

        image_Hotdog = ctk.CTkImage(Image.open("IMG/Comida3.png"), size=(100, 100))
        self.boton_Hotdog = ctk.CTkButton(tarjetas_frame, image=image_Hotdog, text="", width=100, height=50,
                                          command=lambda: self.agregar_pedido("Completo"))
        self.boton_Hotdog.pack(side="left", padx=10, pady=10)

        image_Papas = ctk.CTkImage(Image.open("IMG/Comida4.png"), size=(100, 100))
        self.boton_Papas = ctk.CTkButton(tarjetas_frame, image=image_Papas, text="", width=100, height=50,
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

        # Botón para generar el PDF
        self.boton_generar_pdf = ctk.CTkButton(self.tab2, text="Generar PDF", command=self.generar_pdf)
        self.boton_generar_pdf.pack(pady=20)

    def agregar_pedido(self, pedido):
        precio = self.precios[pedido]
        cantidad = 1  # Puedes ajustar esto para que el usuario seleccione la cantidad
        self.tree_pedido.insert("", "end", values=(pedido, cantidad, precio))

    def generar_pdf(self):
        filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if filename:
            try:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", 'B', 12)
                pdf.cell(200, 10, txt="Boleta restaurante", ln=True)
                pdf.cell(200, 10, txt="Razón social del negocio", ln=True)
                pdf.cell(200, 10, txt="Rut: 12.345.678-9", ln=True)
                pdf.cell(500, 10, txt="Dirección: Calle Falsa 123", ln=True)
                pdf.cell(200, 10, txt="Teléfono: +56 9 1234 5678", ln=True)
                

                pdf.set_font("Arial", size=12)
                pdf.cell(200, 10, txt=f"Fecha y hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", ln=True)

                # Definir el ancho de las columnas
                col_width = pdf.get_string_width("Menu") + 10
                col_width2 = pdf.get_string_width("Cantidad") + 10
                col_width3 = pdf.get_string_width("Precio Unitario") + 10
                row_height = 10

                # Encabezado de la tabla
                pdf.set_font("Arial", 'B', 12)
                pdf.cell(col_width, row_height, "Menu", border=1)
                pdf.cell(col_width2, row_height, "Cantidad", border=1)
                pdf.cell(col_width3, row_height, "Precio Unitario", border=1)
                pdf.ln(row_height)

                # Datos de la tabla
                pdf.set_font("Arial", size=12)
                for item in self.tree_pedido.get_children():
                    values = self.tree_pedido.item(item, 'values')
                    menu, cantidad, precio = values
                    pdf.cell(col_width, row_height, menu, border=1)
                    pdf.cell(col_width2, row_height, str(cantidad), border=1)
                    pdf.cell(col_width3, row_height, str(precio), border=1)
                    pdf.ln(row_height)

                pdf.output(filename)
                messagebox.showinfo("Éxito", "PDF generado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo crear el PDF: {e}")


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

        # Validar entradas
        if not self.validar_nombre(nombre):
            return

        if not self.validar_numero(cantidad):
            return

        # Crear una instancia de ingrediente
        ingrediente = Ingredientes(nombre, int(cantidad))

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


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = AplicacionConPestanas()
    app.mainloop()
