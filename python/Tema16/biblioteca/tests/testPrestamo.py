import unittest
from datetime import datetime, timedelta
from biblioteca.usuario import Usuario
from biblioteca.libro import Libro
from biblioteca.prestamo import Prestamo

class TestPrestamo(unittest.TestCase):
    def test_es_vencido(self):
        usuario = Usuario("Alice", 1)
        libro = Libro("1984", "George Orwell", "1234567890")
        prestamo = Prestamo(usuario, libro, dias_prestamo=0)  # Préstamo inmediato vencido
        self.assertTrue(prestamo.es_vencido())
