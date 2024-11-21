import csv
import json

def verProductos():
    with open("productos.csv", newline="\n",encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for id, nombre, categoria, precio, stock,imagen in reader:
            print("id: {}, Nombre: {}, Categoria: {}, Precio: {}, Stock: {}, Imagen: {}".format(id, nombre, categoria, precio, stock, imagen))
            
def insertar(id,nombre,categoria,precio,stock,imagen):
        with open("productos.csv", "a", newline="\n") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow([id, nombre, categoria, precio, stock, imagen])
            
def borrar(idBorr):
    prod = []
    # creo una lista con los productos en tuplas
    with open("productos.csv", newline="\n",encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for id, nombre, categoria, precio, stock,imagen in reader:
            p = (id, nombre, categoria, precio, stock, imagen)
            prod.append(p)
    
    # actualizo la lista sacando el del id      PASAR A DICCIONARIO
    listaActualizada = []
    for i in prod:
        if idBorr not in i:
            listaActualizada.append(i)
        else:
            print("Borrado exitosamente")
    
    with open("productos.csv", "w", newline="\n") as csvfile:
        campos = ["id", "nombre", "categoria", "precio", "stock", "imagen"]
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
        for id, nombre, categoria, precio, stock, imagen in listaActualizada:
            writer.writerow({
                id, nombre, categoria, precio, stock, imagen
            })

def filtrar(categ):
    prod = []
    # creo una lista con los productos en tuplas
    with open("productos.csv", newline="\n",encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for id, nombre, categoria, precio, stock,imagen in reader:
            p = (id, nombre, categoria, precio, stock, imagen)
            prod.append(p)
    
    for i in prod:
        if categ == i[2].lower():
            print(i)
            
def buscar(nom):
    prod = []
    # creo una lista con los productos en tuplas
    with open("productos.csv", newline="\n",encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for id, nombre, categoria, precio, stock,imagen in reader:
            p = (id, nombre, categoria, precio, stock, imagen)
            prod.append(p)
    
    for i in prod:
        if nom == i[1].lower():
            print(i)
            
def exportarJson():
    prod = []
    with open("productos.csv", newline="\n",encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for id, nombre, categoria, precio, stock, imagen in reader:
            p = (id, nombre, categoria, precio, stock, imagen)
            prod.append(p)

    datos = []
    for id, nombre, categoria, precio, stock, imagen in prod:
        datos.append({"id":id, "nombre":nombre, "categoria":categoria, "precio":precio, "stock":stock, "imagen":imagen})

    with open("productos.json", "a+") as jsonfile:
        json.dump(datos, jsonfile)
    
    
            
def exportarXml():
    prod = []
    with open("productos.csv", newline="\n",encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for id, nombre, categoria, precio, stock,imagen in reader:
            p = (id, nombre, categoria, precio, stock, imagen)
            prod.append(p)
    
    



resp = 0

while resp != "5":
    print("\n\n*********************************")
    print("1) Crear un producto")
    print("2) Ver todos los producto")
    print("3) Eliminar un producto")
    print("4) Actualizar un producto")
    print("5) Filtrar por categoría")
    print("6) Buscar producto")
    print("7) Exportar productos")
    print("8) Salir")
    print("*********************************")
    
    resp = input("¿Qué desea hacer? ")
    
    if resp == "1":
        id = input("Id: ")
        nombre = input("Nombre: ")
        categoria = input("Categoria: ")
        precio = int(input("Precio: "))
        stock = int(input("Stock: "))
        imagen = int(input("Ruta Imagen: "))
        
        insertar(id,nombre,categoria,precio,stock,imagen)
        
    elif resp == "2":
        verProductos()
        
    elif resp == "3":
        print("Sin hacer")
        # id = input("ID: ")
        # borrar(id)
    elif resp == "4":
        print("Lo actualiza")
    elif resp == "5":
        print("----------------------")
        print("- Electrónica")
        print("- Deportes")
        print("- Hogar")
        print("- Juguetes")
        print("- Ropa")
        print("----------------------")
        categ = input("¿Por qué desea filtrar? (debe escribir el nombre)")
        filtrar(categ.lower())
    elif resp == "6":
        categ = input("¿Qué está buscando?")
        buscar(categ.lower())
    elif resp == "7":
        print("----------------------")
        print("1) JSON")
        print("2) XML")
        print("3) Cancelar")
        print("----------------------")
        expor = input("¿En qué desea exportar?")
        if expor == "1":
            exportarJson()
        elif expor == "2":
            pass
        else:
            print("Cancelado")
    else:
        print("Chao")