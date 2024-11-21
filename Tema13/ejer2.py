"""
Desarrollar una calculadora de conversión de unidades que incluya:
- Un ComboBox para seleccionar el tipo de conversión (Temperatura, Longitud, Peso)
- Dos ComboBox para seleccionar las unidades de origen y destino
- Entry para introducir el valor a convertir
- Label para mostrar el resultado
- Botón para realizar la conversión
- Manejo de errores con MessageBox para entradas inválidas

Tipos de conversión mínimos:
- Temperatura: Celsius, Fahrenheit, Kelvin
- Longitud: Metros, Kilómetros, Millas, Pies
- Peso: Kilogramos, Libras, Onzas

"""

from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Conversor de Unidades")

# Combobox 
comboConv = ttk.Combobox(state="readonly",
    values=["Temperatura", "Longitud", "Peso"])
comboConv.place(x=50, y=50)

comboUniOrig = ttk.Combobox(state="readonly",
    values=["Temperatura", "Longitud", "Peso"])
comboUniOrig.place(x=50, y=50)

comboUniDest = ttk.Combobox(state="readonly",
    values=["Temperatura", "Longitud", "Peso"])
comboUniDest.place(x=50, y=50)


tipoConv = comboConv.get()






comboConv.pack()
root.mainloop()