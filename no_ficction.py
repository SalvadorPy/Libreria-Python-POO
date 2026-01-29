from librosG import librosEnGeneral
class noFicction(librosEnGeneral):
    def __init__(self, titulo, numeroPaginas, annoPublicacion, precio, numeroEdicion, ejerciciosPregunta):
        # Lo siguiente es como la asignación:
        super().__init__(titulo, numeroPaginas, annoPublicacion, precio, numeroEdicion)
        self.ejerciciosPregunta = ejerciciosPregunta