import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
from datetime import datetime
hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def crear_pdf(filename):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Boleta restaurante", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Razón social del negocio", ln=True)
    pdf.cell(200, 10, txt="Rut: 12.345.678-9", ln=True)
    pdf.cell(500, 10, txt="Dirección: Calle Falsa 123", ln=True)
    pdf.cell(200, 10, txt="Teléfono: +56 9 1234 5678", ln=True)
    pdf.set_xy(140, 50)
    pdf.cell(100, 10, txt=f"Fecha y hora: {hora_actual}")
    pdf.output(filename)

def save_pdf():
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if filename:
        try:
            crear_pdf(filename)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el PDF: {e}")

# Configuración de la interfaz Tkinter
root = tk.Tk()
root.title("Boleta")

label = tk.Label(root, text="Genera la boleta, aunque aun no tiene los datos... ahi que agregarlo aun.")
label.pack(pady=10)

btn_create_pdf = tk.Button(root, text="Crear Boleta", command=save_pdf)
btn_create_pdf.pack(pady=20)

root.mainloop()
