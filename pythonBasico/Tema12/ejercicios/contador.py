import sys

# si no existe lo crea
fichero = open('contador.txt','r+')
num = fichero.readlines()
num = int(num[0])

# coger lo q le paso por la terminal
arg = sys.argv[1]

if arg == "inc":
# sumar uno al número de contador
    num+=1
    fichero.seek(0)
    fichero.writelines(str(num))
elif arg == "dec":
    # restar uno al número de contador
    num-=1
    fichero.seek(0)
    fichero.writelines(str(num))
else:
    # mostrar el numeros que hay  
    print(num)

fichero.close()

