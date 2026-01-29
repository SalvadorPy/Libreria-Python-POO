from librosG import librosEnGeneral
class ficction(librosEnGeneral):
    def __init__(self, titulo, numeroPaginas, annoPublicacion, precio, numeroEdicion, peliculaPregunta):
        # Lo siguiente es como la asignación:
        super().__init__(titulo, numeroPaginas, annoPublicacion, precio, numeroEdicion)
        self.pelicula = peliculaPregunta