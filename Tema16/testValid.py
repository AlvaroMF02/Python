import unittest
from validadorPassw import validar_password

class TestValidarPassword(unittest.TestCase):
    
    def valido(self):
        # Caso válido: cumple todos los criterios
        self.assertTrue(validar_password("Abc@1234"))
    
    def corto(self):
        # Caso inválido: menos de 8 caracteres
        self.assertFalse(validar_password("Ab1@"))
    
    def sinMayus(self):
        # Caso inválido: no tiene letra mayúscula
        self.assertFalse(validar_password("abc@1234"))
    
    def sinNum(self):
        # Caso inválido: no tiene número
        self.assertFalse(validar_password("Abcdefg@"))
    
    def sinCaracEspec(self):
        # Caso inválido: no tiene carácter especial
        self.assertFalse(validar_password("Abc12345"))

if __name__ == "__main__":
    unittest.main()
