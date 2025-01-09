import unittest
from utils_mate.basic_math import suma, resta, multiplicacion, division

class TestBasicMath(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        with self.assertRaises(ValueError):
            division(6, 0)
