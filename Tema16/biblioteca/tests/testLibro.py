import unittest
from biblioteca.libro import Libro

class TestLibro(unittest.TestCase):
    def test_prestar(self):
        libro = Libro("1984", "George Orwell", "1234567890")
        libro.prestar()
        self.assertFalse(libro.disponible)

    def test_devolver(self):
        libro = Libro("1984", "George Orwell", "1234567890")
        libro.prestar()
        libro.devolver()
        self.assertTrue(libro.disponible)
