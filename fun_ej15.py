"""
Ejercicio 15: Verificar una contraseña

En este ejercicio escribirá una función que determina si una contraseña es buena 
o no. Definiremos como una buena contraseña aquella que tenga una longitud de al 
menos 8 caracteres y contenga al menos una letra mayúscula, al menos una letra 
minúscula y al menos un número. Su función debe devolver verdadero si la contraseña 
que se le pasó, como único parámetro, es buena, de lo contrario debería devolver
falso. Incluya un programa principal que lea una contraseña del usuario e informe 
si es buena o no.

"""

from utiles import encabezado

def verificar_contrasenia(contrasenia):
	bandera_may = False
	bandera_min = False
	bandera_num = False
	bandera_lon = True
	mayu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	minu = "abcdefghijklmnopqrstuvwxyz"
	nume = "0123456789"

	if len(contrasenia) == 8:
		for x in contrasenia:
			if x in mayu:
				bandera_may = True
			if x in minu:
				bandera_min = True
			if x in nume:
				bandera_num = True
	else:
		bandera_lon = False

	if bandera_lon and bandera_may and bandera_min and bandera_num:
		return True
	else:
		return False


titulo = "Ejercicio 15: Verificar una contraseña"
indicaciones = "Verifica si contiene 8 caracteres, menos 1 Mayúscula, 1 minúscula y 1 número"

encabezado(titulo,indicaciones)

contrasenia = input("Ingrese una contraseña para verificar: ")

if verificar_contrasenia(contrasenia):
	print("Contraseña Correcta")
else:
	print("Contraseña Incorrecta")

