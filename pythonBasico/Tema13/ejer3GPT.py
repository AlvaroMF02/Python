import tkinter as tk
from tkinter import ttk, messagebox
# from calendar import DateEntry
import json
from datetime import datetime

# Variables globales
tasks = []
file_name = "tareas.json"

# Funciones
def agregar_tarea():
    def guardar_tarea():
        tarea = entry_tarea.get()
        prioridad = prioridad_var.get()
        fecha_limite = date_entry.get()
        
        if not tarea.strip():
            messagebox.showerror("Error", "La tarea no puede estar vacía")
            return
        
        tasks.append({"Tarea": tarea, "Prioridad": prioridad, "Fecha límite": fecha_limite, "Estado": "Pendiente"})
        actualizar_treeview()
        top.destroy()

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

def editar_tarea():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Seleccione una tarea para editar")
        return

    item_index = int(selected_item[0])
    tarea_seleccionada = tasks[item_index]

    def guardar_edicion():
        tarea = entry_tarea.get()
        prioridad = prioridad_var.get()
        fecha_limite = date_entry.get()

        if not tarea.strip():
            messagebox.showerror("Error", "La tarea no puede estar vacía")
            return

        tasks[item_index] = {"Tarea": tarea, "Prioridad": prioridad, "Fecha límite": fecha_limite, "Estado": tarea_seleccionada["Estado"]}
        actualizar_treeview()
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Editar Tarea")

    tk.Label(top, text="Tarea:").grid(row=0, column=0, padx=10, pady=5)
    entry_tarea = tk.Entry(top, width=30)
    entry_tarea.insert(0, tarea_seleccionada["Tarea"])
    entry_tarea.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(top, text="Prioridad:").grid(row=1, column=0, padx=10, pady=5)
    prioridad_var = tk.StringVar(value=tarea_seleccionada["Prioridad"])
    tk.Radiobutton(top, text="Alta", variable=prioridad_var, value="Alta").grid(row=1, column=1, sticky="w")
    tk.Radiobutton(top, text="Media", variable=prioridad_var, value="Media").grid(row=2, column=1, sticky="w")
    tk.Radiobutton(top, text="Baja", variable=prioridad_var, value="Baja").grid(row=3, column=1, sticky="w")

    tk.Label(top, text="Fecha límite:").grid(row=4, column=0, padx=10, pady=5)
    # date_entry = DateEntry(top, width=27, date_pattern="dd/mm/yyyy")
    date_entry.set_date(datetime.strptime(tarea_seleccionada["Fecha límite"], "%d/%m/%Y"))
    date_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Button(top, text="Guardar", command=guardar_edicion).grid(row=5, column=0, columnspan=2, pady=10)

def eliminar_tarea():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Seleccione una tarea para eliminar")
        return

    item_index = int(selected_item[0])
    del tasks[item_index]
    actualizar_treeview()

def marcar_completada():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Seleccione una tarea para marcar como completada")
        return

    item_index = int(selected_item[0])
    tasks[item_index]["Estado"] = "Completada"
    actualizar_treeview()

def actualizar_treeview():
    tree.delete(*tree.get_children())
    for i, task in enumerate(tasks):
        tree.insert("", "end", iid=i, values=(task["Tarea"], task["Prioridad"], task["Fecha límite"], task["Estado"]))

def guardar_tareas():
    with open(file_name, "w") as f:
        json.dump(tasks, f)
    messagebox.showinfo("Información", "Tareas guardadas correctamente")

def cargar_tareas():
    global tasks
    try:
        with open(file_name, "r") as f:
            tasks = json.load(f)
        actualizar_treeview()
    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error al cargar las tareas")

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

# Frame para los controles
frame_controles = tk.Frame(root)
frame_controles.pack(fill="x", padx=10, pady=5)

tk.Button(frame_controles, text="Agregar", command=agregar_tarea).pack(side="left", padx=5)
tk.Button(frame_controles, text="Editar", command=editar_tarea).pack(side="left", padx=5)
tk.Button(frame_controles, text="Eliminar", command=eliminar_tarea).pack(side="left", padx=5)
tk.Button(frame_controles, text="Marcar como Completada", command=marcar_completada).pack(side="left", padx=5)
tk.Button(frame_controles, text="Guardar", command=guardar_tareas).pack(side="left", padx=5)
tk.Button(frame_controles, text="Cargar", command=cargar_tareas).pack(side="left", padx=5)

# Cargar tareas al iniciar
cargar_tareas()

# Ejecutar la aplicación
root.mainloop()
