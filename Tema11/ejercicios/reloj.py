from datetime import datetime
import time

def reloj():
    while True:
        # Coger la hora y formatearla
        hora = datetime.now().strftime("%H:%M:%S")
        print("Son las " + str(hora))
        # Para q se ejecute cada segundo (como un tiempo de espera)
        time.sleep(1)
        

if __name__ == "__main__":
    reloj()


