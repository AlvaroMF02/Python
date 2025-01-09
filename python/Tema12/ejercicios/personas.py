fichero = open("personas.txt",encoding="utf8")
personas = fichero.read()
personas = personas.split() # asi para que no me salgan con los \n
fichero.close()

listaDicc = []

for i in personas:
    tupla = i.split(";")
    # Crear un diccionario para cada persona
    diccionario_persona = {
        'id': tupla[0],
        'nombre': tupla[1],
        'apellido': tupla[2],
        'nacimiento': tupla[3]
    }
    
    # añadir a la lista personas
    listaDicc.append(diccionario_persona)

print(listaDicc)