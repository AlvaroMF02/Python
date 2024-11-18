fichero = open("personas.txt",encoding="utf8")
personas = fichero.read()
personas = personas.split() # asi para que no me salgan con los \n
fichero.close()

dicc = {"id":"miau", "nombre":"miau", "apellido":"miau", "nacimiento":"miau"}

for i in personas:
    tupla = i.split(";")
    print(tupla)
    for j in tupla:
        # meter en el dicc
        print(j)
        dicc
        

print(personas)


#añadir a la lista personas

# mostrar personas