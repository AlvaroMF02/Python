import tkinter as tk
from tkinter import ttk, messagebox
import json
from tkinter import *
from datetime import datetime

def cargarDatos(tree):
    with open("c:/Users/alvaro/Documents/python/Tema13/tareas.json",encoding="utf8") as jsonfile:
        datos = json.load(jsonfile)
        for i in datos["tareas"]:
            tree.insert("", 'end',text = "id_1", values=(i["tarea"],i["prioridad"],i["fecha_limite"],i["estado"]))
            

def agregar():
    pass



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