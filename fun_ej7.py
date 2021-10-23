"""
Si tiene 3 varillas, posiblemente de diferentes longitudes, puede o no ser posible
colocarlas para que formen un triángulo cuando sus extremos se toquen. Por ejemplo,
si todas las varillas tienen una longitud de 6 centímetros. entonces uno puede
construir fácilmente un triángulo equilátero con ellos. Sin embargo, si una 
varillas es de 6 centímetros de largo, mientras que los otros dos son cada uno
de solo 2 centímetros de largo, entonces no se puede formar un triángulo. 
En general, si una longitud es mayor o igual que la suma de las otras dos, 
entonces las longitudes no pueden usarse para formar un triángulo. De lo 
contrario, pueden formar un triángulo. Escriba una función que determine 
si tres longitudes pueden formar un triángulo. La función tomará 3 parámetros
y devolverá un resultado booleano. Además, escriba un programa que lea 3 
longitudes del usuario y muestre el comportamiento de esta función.
"""

from utiles import encabezado

def triangulo_valido(a,b,c): 
	#se hace la verificación por la negativa de la formula de comparacion
	return a+b <= c or a+c <= b or b+c <= a

titulo = "Ejercicio 7 : ¿Es un triángulo válido?"
indicaciones = "Determinar si tres longitudes pueden formar un triángulo"

encabezado(titulo,indicaciones)

a = int(input("Varilla 1: "))
b = int(input("Varilla 2: "))
c = int(input("Varilla 3: "))

if triangulo_valido(a,b,c):
	print("Las longitudes ingresadas son válidas para formar un triángulo")
else:
	print("Las longitudes ingresadas NO son válidas para formar un triángulo")

