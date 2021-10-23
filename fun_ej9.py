"""
Ejercicio 9: ¿Un string representan un entero?

En este ejercicio escribirá una función llamada es_entero que determina si los 
caracteres en una cadena representan un número entero válido. Al determinar si 
un string representa un número entero, debe ignorar cualquier espacio en blanco 
inicial o final. Una vez que se ignora este espacio en blanco, una cadena 
representa un número entero si su longitud es al menos 1 y solo contiene dígitos, 
o si su primer carácter es + o - y el primer carácter va seguido de uno o más 
caracteres, todos los cuales son dígitos Escriba un programa principal que lea 
una cadena del usuario e informe si representa o no un número entero.

Sugerencia: Puede encontrar los métodos lstrip, rstrip y / o strip para cadenas 
útiles cuando complete este ejercicio.
"""

from utiles import encabezado

def es_entero(cadena):
	bandera = False
	cadena = cadena.strip()
	if len(cadena) >= 1:
		if cadena. isdigit():
			return "valida"
		else:
			for x in cadena:
				if "+" in x or "-" in x:
					pass
				else:
					if not x.isdigit():
						bandera = True
			if not bandera:
				return "valida"
			else:
				return "invalida"


titulo = "Ejercicio 9: ¿Un string representan un entero?"
indicaciones = "Ingrese un número para validar si es entero"

encabezado(titulo,indicaciones)

cadena=input("Ingrese un número entero: ")

print("")

print("El valor ingresado en una cadena %s para transformar en entero" %es_entero(cadena))