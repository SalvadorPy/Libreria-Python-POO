class librosEnGeneral:
    def __init__(self, titulo, numeroPaginas, annoPublicacion, precio, numeroEdicion):
        self.titulo = titulo
        self.numeroPaginas = numeroPaginas
        self.annoPublicacion = annoPublicacion
        self.precio = precio
        self.numeroEdicion = numeroEdicion
    def __str__(self):
        libro=(
            f"Nombre del libro: {self.titulo}\n "
            f"Páginas: {self.numeroPaginas}\n"
            f"Año de publicación:{self.annoPublicacion}\n"
            f"Precio:{self.precio}\n"
            f"Edición:{self.numeroEdicion}\n")

        return libro






"""


book1 = literatura("La primer semana", 200, 1999, 259.99, 1, "Amor", "No")
book2 = ficction("Adios", 250, 2006, 500.00, 3, "Si")
book3 = noFicction("Mecanica cuantica para principiantes", 1000, 2020, 890.00, 1, "Sí")

print(book1.pelicula)
"""