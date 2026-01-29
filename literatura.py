from librosG import librosEnGeneral

class literatura(librosEnGeneral):
    def __init__(self, titulo, numeroPaginas, annoPublicacion, precio, numeroEdicion, sentimientoPregunta, peliculaPregunta):
        # Lo siguiente es como la asignación:
        super().__init__(titulo, numeroPaginas, annoPublicacion, precio, numeroEdicion)
        self.sentimiento = sentimientoPregunta
        self.pelicula = peliculaPregunta