import csv

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

resp = 0

while resp != "5":
    print("\n\n*********************************")
    print("1) Crear un producto")
    print("2) Ver todos los producto")
    print("3) Eliminar un producto")
    print("4) Actualizar un producto")
    print("5) Salir")
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
        id = input("ID: ")
        borrar(id)
    elif resp == "4":
        print("Lo actualiza")
    else:
        print("Chao")