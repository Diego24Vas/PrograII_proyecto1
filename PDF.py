from fpdf import FPDF
from datetime import datetime

class GeneradorPDF:
    def __init__(self, pedidos):
        self.pedidos = pedidos

    def generar_pdf(self, archivo_salida="boleta_pedido.pdf"):
        pdf = FPDF()
        pdf.add_page()

        # Título del PDF
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, txt="Boleta restaurante", ln=True)
        pdf.cell(200, 10, txt="Razón social del negocio", ln=True)
        pdf.cell(200, 10, txt="Rut: 12.345.678-9", ln=True)
        pdf.cell(500, 10, txt="Dirección: Calle Falsa 123", ln=True)
        pdf.cell(200, 10, txt="Teléfono: +56 9 1234 5678", ln=True)
        #Fecha Boleta
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Fecha y hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", ln=True)

        # Espacio
        pdf.ln(10)

        # Añadir tabla de pedido
        pdf.set_font("Arial", size=12)
        pdf.cell(60, 10, txt="Menu", border=1)
        pdf.cell(40, 10, txt="Cantidad", border=1)
        pdf.cell(40, 10, txt="Precio Unitario", border=1)
        pdf.ln()

        # Añadir los elementos del pedido al PDF
        total = 0
        for pedido in self.pedidos:
            pdf.cell(60, 10, txt=str(pedido[0]), border=1)
            pdf.cell(40, 10, txt=str(pedido[1]), border=1)
            pdf.cell(40, 10, txt=str(pedido[2]), border=1)
            total += int(pedido[1]) * int(pedido[2])
            pdf.ln()

        # Añadir el total
        pdf.cell(100, 10, txt=f"Total: {total}", ln=True)

        # Guardar el PDF en un archivo
        pdf.output(archivo_salida)
