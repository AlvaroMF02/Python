"""


** Una vez lo tengas listo realiza las siguientes prueba en tu código: **
* Crea los tres personajes de la tabla anterior y añádelos al Gestor.
* Muestra los personajes del Gestor.
* Borra al Arquero.
* Muestra de nuevo el Gestor.
  
*Sugerencias: El ejemplo con pickle que realizamos puede servirte como base.*
"""

# TODO SE DEBE IR GUARDANDO

class Personaje():
    
    def __init__(self,clase="",vida=0,ataque=0,defensa=0,alcance = 0):
        self.clase = clase
        self.vida = abs(vida)
        self.ataque = abs(ataque)
        self.defensa = abs(defensa)
        self.alcance = abs(alcance)
        
        # hay q comprobar que la clase no existe
    
    # Getters
    def getClase(self):
        return self.clase
    def getaVida(self):
        return self.vida
    def getAtaque(self):
        return self.ataque
    def getDefensa(self):
        return self.defensa
    def getAlcance(self):
        return self.alcance
    

"""
* Por otro lado la clase **Gestor** deberá incorporar todos los métodos necesarios para **añadir personajes, mostrarlos y borrarlos (a partir de su nombre
por ejemplo)** (tendrás que pensar una forma de hacerlo), además de los métodos esenciales para guardar los cambios en el fichero personajes.pckl que se deberían 
ejecutar automáticamente. 
* En caso de que el personaje ya exista en el Gestor entonces no se creará.

"""
class Gestor():
    
    def __init__(self,lista):
        self.lista = lista
        
    
    
    
    def insertarPersonaje(self,pers):
        self.lista.append(pers)
    
    def verPersonajes(self):
        print(self.lista)
        
    def elimPersonaje(self,pers):
        self.lista.remove(pers)