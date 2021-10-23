"""
Ejercicio 28: Elementos en posiciones impares

Escriba una función llamada elementos_impares que, dada una lista, devuelve 
una lista nueva que contiene sólo los elementos impares de la lista original. 
El primer elemento de una lista (es decir, índice 0) es un elemento par. Por 
ejemplo para el caso de que se ejecute la función pasando como parámetro la 
lista [1, 2, 3, 4] la función debe retornar [2, 4]. Use la función en un 
programa principal y pruebe su código en varias combinaciones de valores 
diferentes.
"""


from utiles import encabezado

def elementos_impares(lista,cant):
	pos = 1
	impares = []
	while pos < cant:
		impares.append(lista[pos])
		pos +=2
	return impares
	

titulo = "Ejercicio 28: Elementos en posiciones impares"
indicaciones = "Obtener elementos de posiciones impares de la lista a ingresar"

encabezado(titulo,indicaciones)


lista = []
cant=0
cant= int(input("indique la cantidad de valores a ingresar: "))
for x in range(cant):
	elemento = int(input("Ingrese el valor %i a analizar: " %x))
	lista.append(elemento)

print("Los elementos de las posiciones impares de la lista ingresada son:")
print(elementos_impares(lista,cant))