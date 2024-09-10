import customtkinter as ctk
from tkinter import ttk
from PIL import Image

class AplicacionPedidos(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Pedidos")
        self.geometry("600x400")

        # Diccionario de precios
        self.precios = {
            "Papas Fritas": 500,
            "Pepsi": 1100,
            "Completo": 1800,
            "Hamburguesa": 3500
        }

        tarjetas_frame = ctk.CTkFrame(self)
        tarjetas_frame.pack(side="top", fill="x", pady=10)

        # Botones
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

        # Treeview para mostrar el pedido
        frame_treeview2 = ctk.CTkFrame(self)
        frame_treeview2.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)

        self.tree_pedido = ttk.Treeview(frame_treeview2, columns=("Menu", "Cantidad", "Precio"), show="headings")
        self.tree_pedido.heading("Menu", text="Menu")
        self.tree_pedido.heading("Cantidad", text="Cantidad")
        self.tree_pedido.heading("Precio", text="Precio Unitario")
        self.tree_pedido.pack(expand=True, fill="both", padx=10, pady=10)

    def agregar_pedido(self, pedido):
        precio = self.precios[pedido]
        cantidad = 1  # Puedes ajustar esto para que el usuario seleccione la cantidad
        self.tree_pedido.insert("", "end", values=(pedido, cantidad, precio))

if __name__ == "__main__":
    app = AplicacionPedidos()
    app.mainloop()
