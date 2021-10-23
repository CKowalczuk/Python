"""
Realiza una función separar(lista) que tome una lista que tenga datos de cantidad
de árboles plantados en diferentes ciudades de Argentina durante la cuarentena.
Luego la función debe devolver dos listas ordenadas. La primera con las cantidades
que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.
"""

from utiles import encabezado

def separar(lista):
    # print("Elementos de la lista mayores a 100")
    mayores100 = []
    menores100 = []
    for x in range(len(lista)):
        if lista[x]>100:
            mayores100.append(lista[x])
        else:
            menores100.append(lista[x])
        	
    lista.sort()
    print("Elementos Ordenados: ", lista)
    print("Elementos Mayores a 100: ", mayores100)
    print("Elementos Menores o iguales a 100: ", menores100)


# bloque principal del programa


titulo = "Desafío 3 - Arboles Plantados en Cuarentena"
indicaciones = "Devolver listas ordenadas"


lista = [200,50,100,80,120,90,85,75,70,105]

encabezado(titulo,indicaciones)
# lista=carga_lista()
separar(lista)

