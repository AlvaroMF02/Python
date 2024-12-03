class Calculadora:
    """
    Esta clase nos da métodos para hacer operaciones basicas
    """
    def suma(self, n1, n2):
        """
        Calcula la suma de dos números

        >>> calc = Calculadora()
        >>> calc.suma(5, 10)
        15
        >>> calc.suma(50, 10)
        60
        >>> calc.suma(7, -3)
        4
        """
        return n1 + n2

    def resta(self, n1, n2):
        """
        Calcula la resta de dos números

        >>> calc = Calculadora()
        >>> calc.resta(10, 5)
        5
        >>> calc.resta(50, 20)
        30
        >>> calc.resta(7, 10)
        -3
        """
        return n1 - n2

    def multiplicacion(self, n1, n2):
        """
        Calcula la multiplicación de dos números

        >>> calc = Calculadora()
        >>> calc.multiplicacion(5, 10)
        50
        >>> calc.multiplicacion(2, 0)
        0
        >>> calc.multiplicacion(-3, 3)
        -9
        """
        return n1 * n2

    def division(self, n1, n2):
        """
        Calcula la división de dos números

        >>> calc = Calculadora()
        >>> calc.division(10, 5)
        2.0
        >>> calc.division(20, 4)
        5.0
        >>> calc.division(7, 2)
        3.5
        """
        return n1 / n2
