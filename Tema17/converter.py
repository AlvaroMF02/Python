import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        value = float(entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        if from_unit == to_unit:
            result_label.config(text=f"{value:.2f} {to_unit}")
            return
        
        # Conversión a Celsius
        if from_unit == "Celsius":
            celsius = value
        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
        elif from_unit == "Kelvin":
            celsius = value - 273.15

        # Conversión desde Celsius a la unidad destino
        if to_unit == "Celsius":
            result = celsius
        elif to_unit == "Fahrenheit":
            result = celsius * 9/5 + 32
        elif to_unit == "Kelvin":
            result = celsius + 273.15

        result_label.config(text=f"{result:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Entrada Inválida", "Por favor, ingrese un número válido.")

# Configuración de la ventana principal
app = tk.Tk()
app.title("Conversor de Temperatura")
app.geometry("300x200")
app.resizable(False, False)

# Variables
from_unit_var = tk.StringVar(value="Celsius")
to_unit_var = tk.StringVar(value="Fahrenheit")

# Widgets
tk.Label(app, text="Ingrese el valor:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(app)
entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="De:").grid(row=1, column=0, padx=10, pady=10)
from_unit_menu = ttk.Combobox(app, textvariable=from_unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
from_unit_menu.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="A:").grid(row=2, column=0, padx=10, pady=10)
to_unit_menu = ttk.Combobox(app, textvariable=to_unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
to_unit_menu.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(app, text="Convertir", command=convert_temperature)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(app, text="Resultado: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar la aplicación
app.mainloop()
