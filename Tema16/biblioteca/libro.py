class Libro():
    """
    Con esta clase se pueden ver los atributos de un libro creado
    """
    
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def cambiarTitulo(self,titNuev):
        """
        Cambia el título del libro que usa el metodo
        """
        self.titulo = titNuev
        
    def cambiarAutor(self,autNuev):
        """
        Cambia el autor del libro que usa el metodo
        """
        self.autor = autNuev
        
    def cambiarPaginas(self,paginas):
        """
        Cambia las páginas del libro que usa el metodo
        """
        self.paginas = paginas
        
        
    def __str__(self):
        return "Título: {}, Autor:{}, Páginas: {}".format(self.titulo,self.autor,self.paginas)
    
    