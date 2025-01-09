
def suma(n1,n2):
    res = 0 # por si hay un error q devuelva 0
    try:
        res = n1 + n2
    except TypeError:
        print("Los valores no son números")
        
    return res

def resta(n1,n2):
    res = 0 
    try:
        res = n1 - n2
    except TypeError:
        print("Los valores no son números")
    
    return res

def producto(n1,n2):
    res = 0 
    try:
        res = n1 * n2
    except TypeError:
        print("Los valores no son números")
    
    return res

def division(n1,n2):
    res = 0
    try:
        res = n1 / n2
    except TypeError:
        print("Los valores no son números")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    return res