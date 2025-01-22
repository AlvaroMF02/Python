import unittest
from utils_mate.advanced_math import potencia, raiz_cuadrada, factorial

class TestAdvancedMath(unittest.TestCase):
    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_raiz_cuadrada(self):
        self.assertEqual(raiz_cuadrada(4), 2)
        with self.assertRaises(ValueError):
            raiz_cuadrada(-1)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-5)
