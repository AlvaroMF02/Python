from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox



def abrir():
    fichero = FileDialog.askopenfilename(title="Abrir un fichero")
    print(fichero)
    
def guardar():
    ruta = FileDialog.asksaveasfile(title="Guardar un fichero")
    print(ruta)
    
def cerrar():
    contenido = texto.get("1.0", "end-1c")
    if len(contenido)>0:
        resultado = MessageBox.askquestion("Salir", 
        "¿Está seguro que desea salir sin guardar?")

        if resultado == "yes":
            root.destroy()
    else:
        root.quit()
    
def cortar(root):
    root.text_area.event_generate("<<Cut>>")
    
def copiar(root):
    root.text_area.event_generate("<<Copiar>>")
    
def pegar(root):
    root.text_area.event_generate("<<Pegar>>")


root = Tk()

root.title("Editor de Texto")
texto = Text(root)
texto.config(font=("Consolas",12), padx=5, pady=5)

# conf del menu
menuC = Menu(root)
root.config(menu=menuC)
# Submenus
archivo = Menu(menuC,tearoff=0)
edicion = Menu(menuC,tearoff=0)
menuC.add_cascade(label="Archivo",menu=archivo)
menuC.add_cascade(label="Edición",menu=edicion)
archivo.add_command(label="Nuevo")
archivo.add_command(label="Abrir",command=abrir)
archivo.add_command(label="Guardar",command=guardar)
archivo.add_separator()
archivo.add_command(label="Salir",command=cerrar)

edicion.add_command(label="Cortar",command=cortar)
edicion.add_command(label="Copiar",command=copiar)
edicion.add_command(label="Pegar",command=pegar)

texto.pack()
root.mainloop()