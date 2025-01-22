import tkinter as tk
from tkinter import ttk, messagebox
import json
from tkinter import *
from datetime import datetime

def cargarDatos(tree):  # cambia rnombre para que lo lea en clase
    with open("c:/Users/alvar/Documents/Python/Tema13/tareas.json",encoding="utf8") as jsonfile:
        datos = json.load(jsonfile)
        for i in datos["tareas"]:
            tree.insert("", 'end',text = "id_1", values=(i["tarea"],i["prioridad"],i["fecha_limite"],i["estado"]))
            

def agregar():
    top = tk.Toplevel(root)
    top.title("Agregar Tarea")
    tk.Label(top, text="Tarea:").grid(row=0, column=0, padx=10, pady=5)
    entry_tarea = tk.Entry(top, width=30)
    entry_tarea.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(top, text="Prioridad:").grid(row=1, column=0, padx=10, pady=5)
    prioridad_var = tk.StringVar(value="Media")
    tk.Radiobutton(top, text="Alta", variable=prioridad_var, value="Alta").grid(row=1, column=1, sticky="w")
    tk.Radiobutton(top, text="Media", variable=prioridad_var, value="Media").grid(row=2, column=1, sticky="w")
    tk.Radiobutton(top, text="Baja", variable=prioridad_var, value="Baja").grid(row=3, column=1, sticky="w")
    
    tk.Label(top, text="Fecha límite:").grid(row=4, column=0, padx=10, pady=5)
    # date_entry = DateEntry(top, width=27, date_pattern="dd/mm/yyyy")
    date_entry.grid(row=4, column=1, padx=10, pady=5)
    
    tk.Button(top, text="Guardar", command=guardar_tarea).grid(row=5, column=0, columnspan=2, pady=10)



# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")

# Treeview para mostrar las tareas
tree = ttk.Treeview(root, columns=("Tarea", "Prioridad", "Fecha límite", "Estado"), show="headings")
tree.heading("Tarea", text="Tarea")
tree.heading("Prioridad", text="Prioridad")
tree.heading("Fecha límite", text="Fecha límite")
tree.heading("Estado", text="Estado")
tree.pack(fill="both", expand=True, padx=10, pady=10)

# editar agregar eliminar
Button(root, text="Agregar",command=agregar).pack(side=LEFT)
Button(root, text="Editar").pack(side=LEFT)
Button(root, text="Eliminar").pack(side=LEFT)
Button(root, text="Marcar como completada").pack(side=LEFT)





# Ejecutar la aplicación
cargarDatos(tree)
root.mainloop()