import unittest
from biblioteca.usuario import Usuario
from biblioteca.libro import Libro

class TestUsuario(unittest.TestCase):
    def test_agregar_prestamo(self):
        usuario = Usuario("Alice", 1)
        libro = Libro("1984", "George Orwell", "1234567890")
        usuario.agregar_prestamo(libro)
        self.assertIn(libro, usuario.prestamos)

    def test_devolver_libro(self):
        usuario = Usuario("Alice", 1)
        libro = Libro("1984", "George Orwell", "1234567890")
        usuario.agregar_prestamo(libro)
        usuario.devolver_libro(libro)
        self.assertNotIn(libro, usuario.prestamos)
