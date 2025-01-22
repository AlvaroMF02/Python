import sys
print(sys.argv) # argumentos enviados

filas = int(input("Escribe las filas"))
colum = int(input("Escribe las columnas"))

while filas<0 or filas>9:
    filas = int(input("Inserte un numero valido"))
    
while colum<0 or colum>9:
    colum = int(input("Inserte un numero valido"))
    
for i in range(filas):
    for j in range(colum):
        print(" * ", end='')
    print("")