"""
Ejercicio 16: Dígitos hexadecimales y decimales

Escriba dos funciones, hex2int e int2hex, que conviertan entre dígitos hexadecimales
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E y F) y enteros de base 10. La función
hex2int es responsable de convertir una cadena que contiene un solo dígito 
hexadecimal en un entero de base 10, mientras que la función int2hex es 
responsable de convertir un entero entre 0 y 15 en un solo dígito hexadecimal. 
Cada función tomará el valor para convertir como su único parámetro y devolverá
el valor convertido como el único resultado de la función. Asegúrese de que la 
función hex2int funcione correctamente para letras mayúsculas y minúsculas. Sus
funciones deberían finalizar el programa con un mensaje de error significativo
si se proporciona un parámetro no válido.

"""
from utiles import encabezado


def hex2int(hexa):
	equival = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
	hexa = hexa.lower()
	if hexa > "9":
		return equival[hexa]
	else:
		return hexa


def int2hex(ente):
	equival = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
	ente = int(ente)
	if ente > 9:
		return equival[ente]
	else:
		return ente


titulo = "Ejercicio 16: Dígitos hexadecimales y decimales"
indicaciones = "Convertir cadenas Hexadecimales y enteras"

encabezado(titulo,indicaciones)

hexa=input("Ingrese una valor Hexadecimal entre 1 y f : ")
ente=input("Ingrese un entero entre 0 y 15            : ")

print("El valor entero del Hexadecimal ingresado es :",hex2int(hexa))
print("El valor Hexadecimal del entero ingresado es :",int2hex(ente))
