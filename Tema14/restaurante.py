import sqlite3

def crear_bd():
    # creacion de la bd
    cursor.execute("CREATE TABLE IF NOT EXISTS categoria( id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS plato( id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL, categoria_id INTEGER NOT NULL, FOREIGN KEY(categoria_id) REFERENCES categoria(id))")
    conexion.commit()
    

def agregar_categoria(nomCateg):
    # insertar categoria
    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '"+nomCateg+"')")
        conexion.commit()
        print(" # Insertado con exito # ")
    except:
        print(" # Ese nombre ya se encuentra en uso # ")
        
        
def agregar_plato(seleCateg,nomPlato):
    # insertar plato 
    try:
        cursor.execute("INSERT INTO plato VALUES (null, '"+nomPlato+"',"+str(seleCateg)+")",)
        conexion.commit()
        print(" # Insertado con exito # ")
    except:
        print(" # El plato ya existe # ")

def mostrar_menu():
    # mostrar de forma ordenada el menu
    cursor.execute("SELECT * FROM plato LEFT JOIN categoria ON plato.id = categoria.id")
    menu = cursor.fetchall()
    for i in menu:
        print(i)
    for _,plat,_,_,categ in menu:
        print("\t- {} : {}".format(categ,plat))
            









conexion = sqlite3.connect('restaurante.db')
cursor = conexion.cursor()

# Crea la bd
crear_bd()

# Menu
while True:
    print("\n\n###############################")
    print("1) Insertar una categoria")
    print("2) Insertar un plato")
    print("3) Ver menú")
    print("0) Salir")
    print("###############################\n\n")
    selec = input("Escoja una opción: ")

    if selec == "1":
        # crear una categoria nueva
        nomCateg = input("Nombre: ")
        agregar_categoria(nomCateg)
        
    elif selec == "2":
        # mostrar las categorias que hay
        cursor.execute("SELECT * FROM categoria")
        categ = cursor.fetchall()
        for ind,val in categ:
            print("{}) {}".format(ind,val))
        # escoger la categoria comprobando errores
        try:
            seleCateg = int(input("Escoja la categoria a la que pertenecerá el plato: "))
            if seleCateg < 0 or seleCateg > len(categ):
                print(" # Esa opción no existe # ")
        except ValueError:
            print(" # Escriba números # ")
        
        nomPlato = input("¿Qué nombre desea ponerle al plato?: ")
        # pasar datos para insertar
        agregar_plato(seleCateg,nomPlato)
        
    elif selec == "3":
        mostrar_menu()
    
    elif selec == "0":
        break


conexion.close()
