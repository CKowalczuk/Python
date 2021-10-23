"""
Ejercicio 4: Mediana de tres valores

Escriba una función que tome tres números como parámetros y devuelva el valor 
medio de esos parámetros como resultado. Incluya un programa principal que lea 
tres valores del usuario y muestre su mediana.

Sugerencia: El valor medio es el medio de los tres valores cuando se ordenan 
en orden ascendente. Se puede encontrar usando declaraciones if, o con un poco 
de creatividad matemática.
"""

from utiles import encabezado

	        # 3 1 2   
def mediana(a,b,c):
	
	if a > b and b > c:
			return b
	elif b > a and a > c:
			return a
	elif c > a and a > b:
			return a
	elif c > b and b > a:
			return b
	elif a > c and c > b:
			return c
	elif b > c and c > a:
			return c
	else:
		return "El cálculo se realiza con números diferentes"





titulo = "Ejercicio 4: Mediana de tres valores"
indicaciones = "Ingrese tres números y obtenga el valor de la mediana"

encabezado(titulo,indicaciones)

a = int(input("Ingrese el primer número  :"))
b = int(input("Ingrese el segundo número :"))
c = int(input("Ingrese el tercer número  :"))

print("la Mediana de los números ingresados es :", mediana(a,b,c))
