import sys

if len(sys.argv) != 2: # Para comprobar que se pasa lo q se pide creo
    print("Uso: python descomposicion.py <número entero positivo>")
else:
    try:
        numero = int(sys.argv[1])
        if numero < 0:
            # Crear un error
            raise ValueError("El número debe ser positivo.")
        
        numero_str = str(numero)
        longitud = len(numero_str)

        for i, digito in enumerate(numero_str):         # separa cada una de las letras
            valor = int(digito) * (10 ** (longitud - i - 1))
            print(f"{valor:0{longitud}d}")
            
    except ValueError as e:
        print(f"Error: {e}")