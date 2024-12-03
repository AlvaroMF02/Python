import re

def validar_password(passw):
    """
    Valida una contraseña dependiendo de lo siguiente:
    - Mínimo 8 caracteres
    - Al menos una letra mayúscula
    - Al menos un número
    - Al menos un carácter especial (@#$%&)
    
    Validas:
        asD4$erft
        $asdkU632
        
    Invalidas:
        12345678
        unodostrescuatro
        
    >>> validar_password(1234)
    False

    >>> validar_password(1d2a34d)
    False

    >>> validar_password(unodostrescuatro)
    False

    >>> validar_password(asD4$erft)
    True

    >>> validar_password($asdkU632)
    True
    
    """
    patron = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&])[A-Za-z\d@#$%&]{8,}$'
    if re.match(patron, passw):
        return True
    else:
        return False
    