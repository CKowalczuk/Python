"""
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas
de dos ciudades se cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver 
el nombre de la ciudad 1.

Si el primer número es menor que el segundo, debe devolver 
el nombre de la ciudad 2.

Si ambos números son iguales, debe devolver el nombre de ambas.

"""
from utiles import encabezado

def relacion(a,b):
	if a > b:
		return "Primera"
	elif a < b:
		return "Segunda"


titulo = "Desafío 2 - Toneladas Recicladas"
indicaciones = "Determinar la ciudad que recicló la mayor cantidad de material"


encabezado(titulo,indicaciones)

print("Ingrese el Nombre de la primer ciudad y a continuación la cantidad de toneladas")

ciudad1 = input("Ciudad: ")
a = int(input("Toneladas: "))

ciudad2 = input("Ciudad: ")
b = int(input("Toneladas: "))

if relacion(a,b) == "Primera":
	print("Con %i toneladas, %s es la ciudad de mayor reciclado" %(a,ciudad1))
elif relacion(a,b) == "Segunda":
	print("Con %i toneladas, %s es la ciudad de mayor reciclado" %(b,ciudad2))
else:
	print("Con %i toneladas, %s y %s reciclaron la misma cantidad de toneladas" %(a,ciudad1, ciudad2))


