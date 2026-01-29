from literatura import literatura
from no_ficction import  noFicction
from ficction import ficction

def cargarDatos():
    titulo = str(input("Escribe el titulo del libro: \n"))
    numeroPaginas = int(input("¿Cuántas páginas tiene?\n"))
    annoPublicacion = int(input("Escribe el año de publicacion: \n"))
    precio = float(input("Ingresa el precio:\n"))
    numeroEdicion = int(input("Ingresa el numero de edición: \n"))
    print("1.-Literatura\n 2.-No-ficction \n 3.-Ficction\n")
    respuesta = int(input("Escoge el tipo de libro\n"))
    if respuesta == 1:
        sentimientoPregunta = str(input("Ingresa el sentimiento que evoca la pelicula: \n"))
        peliculaPregunta = str(input("¿Hay película de este libro?"))
        lit=literatura(titulo, numeroPaginas, annoPublicacion, precio, numeroEdicion, sentimientoPregunta, peliculaPregunta)
        books.append(lit)
    elif respuesta == 2:
        ejerciciosPregunta = str(input("¿Hay ejercicios en este libro?"))
        noficc = noFicction(titulo, numeroPaginas, annoPublicacion, precio, numeroEdicion, ejerciciosPregunta)
        books.append(noficc)
    elif respuesta == 3:
        peliculaPregunta = str(input("¿Hay película de este libro?"))
        ficc = ficction(titulo, numeroPaginas, annoPublicacion, precio, numeroEdicion, peliculaPregunta)
        books.append(ficc)
    else:
        print("Intentalo de nuevo")
books=[]

respuesta = str(input("Quieres agregar libro?\n\n"))

while respuesta=="Si":
    cargarDatos()
    
    respuesta = str(input("Quieres agregar libro?\n\n"))

y=1

for x in books:
    print("\t\tLIBRO "+str(y))
    print(x)
    y+=1
    



