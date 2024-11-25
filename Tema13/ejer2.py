# """
# Desarrollar una calculadora de conversión de unidades que incluya:
# - Un ComboBox para seleccionar el tipo de conversión (Temperatura, Longitud, Peso)
# - Dos ComboBox para seleccionar las unidades de origen y destino
# - Entry para introducir el valor a convertir
# - Label para mostrar el resultado
# - Botón para realizar la conversión
# - Manejo de errores con MessageBox para entradas inválidas

# Tipos de conversión mínimos:
# - Temperatura: Celsius, Fahrenheit, Kelvin
# - Longitud: Metros, Kilómetros, Millas, Pies
# - Peso: Kilogramos, Libras, Onzas

# """

# from tkinter import *
# from tkinter import ttk


# root = Tk()
# root.title("Conversor de Unidades")

# # Combobox 
# comboConv = ttk.Combobox(state="readonly",
#     values=["Temperatura", "Longitud", "Peso"])
# comboConv.place(x=50, y=50)

# comboUniOrig = ttk.Combobox(state="readonly",
#     values=["Temperatura", "Longitud", "Peso"])
# comboUniOrig.place(x=50, y=50)

# comboUniDest = ttk.Combobox(state="readonly",
#     values=["Temperatura", "Longitud", "Peso"])
# comboUniDest.place(x=50, y=50)


# tipoConv = comboConv.get()






# comboConv.pack()
# root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

# Funciones de conversión
def convertir():
    try:
        valor = float(entry_valor.get())
        tipo_conversion = combo_tipo_conversion.get()
        unidad_origen = combo_origen.get()
        unidad_destino = combo_destino.get()

        if tipo_conversion == "Temperatura":
            resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
        elif tipo_conversion == "Longitud":
            resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
        elif tipo_conversion == "Peso":
            resultado = convertir_peso(valor, unidad_origen, unidad_destino)
        else:
            raise ValueError("Tipo de conversión no válido")

        label_resultado.config(text=f"Resultado: {resultado:.2f} {unidad_destino}")
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")

# Función para conversión de temperatura
def convertir_temperatura(valor, origen, destino):
    if origen == destino:
        return valor

    # Convertir a Celsius
    if origen == "Celsius":
        celsius = valor
    elif origen == "Fahrenheit":
        celsius = (valor - 32) * 5/9
    elif origen == "Kelvin":
        celsius = valor - 273.15

    # Convertir de Celsius a destino
    if destino == "Celsius":
        return celsius
    elif destino == "Fahrenheit":
        return celsius * 9/5 + 32
    elif destino == "Kelvin":
        return celsius + 273.15

# Función para conversión de longitud
def convertir_longitud(valor, origen, destino):
    factores = {
        "Metros": 1,
        "Kilómetros": 1000,
        "Millas": 1609.34,
        "Pies": 0.3048
    }

    return valor * factores[origen] / factores[destino]

# Función para conversión de peso
def convertir_peso(valor, origen, destino):
    factores = {
        "Kilogramos": 1,
        "Libras": 0.453592,
        "Onzas": 0.0283495
    }

    return valor * factores[origen] / factores[destino]

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Conversor de Unidades")

# Widgets de la interfaz
tk.Label(root, text="Tipo de conversión:").grid(row=0, column=0, padx=10, pady=5)
combo_tipo_conversion = ttk.Combobox(root, values=["Temperatura", "Longitud", "Peso"])
combo_tipo_conversion.grid(row=0, column=1, padx=10, pady=5)
combo_tipo_conversion.set("Temperatura")

combo_tipo_conversion.bind("<<ComboboxSelected>>", lambda _: actualizar_unidades())

# ComboBox para unidades de origen y destino
tk.Label(root, text="Unidad origen:").grid(row=1, column=0, padx=10, pady=5)
combo_origen = ttk.Combobox(root)
combo_origen.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Unidad destino:").grid(row=2, column=0, padx=10, pady=5)
combo_destino = ttk.Combobox(root)
combo_destino.grid(row=2, column=1, padx=10, pady=5)

# Entry para el valor a convertir
tk.Label(root, text="Valor a convertir:").grid(row=3, column=0, padx=10, pady=5)
entry_valor = tk.Entry(root)
entry_valor.grid(row=3, column=1, padx=10, pady=5)

# Botón para realizar la conversión
btn_convertir = tk.Button(root, text="Convertir", command=convertir)
btn_convertir.grid(row=4, column=0, columnspan=2, pady=10)

# Label para mostrar el resultado
label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.grid(row=5, column=0, columnspan=2, pady=10)

def actualizar_unidades():
    tipo = combo_tipo_conversion.get()
    if tipo == "Temperatura":
        unidades = ["Celsius", "Fahrenheit", "Kelvin"]
    elif tipo == "Longitud":
        unidades = ["Metros", "Kilómetros", "Millas", "Pies"]
    elif tipo == "Peso":
        unidades = ["Kilogramos", "Libras", "Onzas"]
    else:
        unidades = []

    combo_origen['values'] = unidades
    combo_destino['values'] = unidades
    combo_origen.set(unidades[0])
    combo_destino.set(unidades[1])

# Inicializar con las unidades de Temperatura
actualizar_unidades()

# Ejecutar la aplicación
root.mainloop()
