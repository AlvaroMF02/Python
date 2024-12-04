from datetime import datetime, timedelta

class Prestamo:
    """
    Representa un préstamo de un libro a un usuario
    """

    def __init__(self, usuario, libro, dias_prestamo=14):
        """
        Inicializa un nuevo préstamo
        """
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=dias_prestamo)

    def es_vencido(self):
        """Verifica si el préstamo está vencido.

        Returns:
            bool: True si el préstamo está vencido, False en caso contrario.
        """
        return datetime.now() > self.fecha_devolucion
