"""
Ejercicio 10: Precedencia del operador

Escriba una función llamada precedencia que devuelve un número entero que representa
la precedencia de un operador matemático. Una cadena que contiene el operador se
pasará a la función como su único parámetro. Su función debe devolver 1 
para + y -, 2 para * y /, y 3 para ˆ. Si la cadena que se pasa a la función 
no es uno de estos operadores, la función debería devolver -1. Incluya un 
programa principal que lea un operador del usuario y muestre la precedencia 
del operador o un mensaje de error que indique que la entrada no era un operador.

En este ejercicio, se usa ˆ para representar la exponenciación, en lugar de 
la elección de Python de **, para facilitar el desarrollo de la solución.
"""

from utiles import encabezado
OP_1 = "+-"
OP_2 = "*/"
OP_3 = "ˆ"

def precedencia(operador):
	if operador in OP_1:
		return 1
	elif operador in OP_2:
		return 2
	elif operador in OP_3:
		return 3
	else:
		return -1



titulo = "Ejercicio 10: Precedencia del operador"
indicaciones = "Obtener la precedencia de un operador matemático"

encabezado(titulo,indicaciones)

operador = input("Ingrese el operador a verificar :")
if precedencia(operador) > 0:
	print("La precedencia del operador %s es %i " % (operador, precedencia(operador)))
else:
	print("El valor ingresado no es iun operador válido para verificar")
