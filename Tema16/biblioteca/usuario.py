class Usuario:
    """
    Con esta clase se pueden ver los usuarios de la biblioteca
    """

    def __init__(self, nombre, id):
        """
        Inicializa un nuevo usuario
        """
        self.nombre = nombre
        self.id = id
        self.libros = []

    def agregar_prestamo(self, libro):
        """
        sAgrega un libro al usuario
        """
        self.libros.append(libro)

    def devolver_libro(self, libro):
        """
        Devuelve un libro del usuario
        """
        if libro in self.libros:
            self.libros.remove(libro)
