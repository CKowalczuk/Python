"""
Ejercicio 8: Capitalízalo

Muchas personas no usan letras mayúsculas correctamente, especialmente cuando 
escriben en dispositivos pequeños como teléfonos inteligentes. En este ejercicio,
escribirá una función que capitaliza los caracteres apropiados en una cadena. 
Una "i" minúscula debe reemplazarse por una "I" mayúscula si está precedida y 
seguida de un espacio. El primer carácter de la cadena también debe estar en 
mayúscula, así como el primer carácter no espacial después de un ".", "!" o "?" 
Por ejemplo, si la función se proporciona con la cadena "¿a qué hora tengo que estar allí? ¿cuál es la dirección?" entonces debería devolver la cadena "¿A qué 
hora tengo que estar allí? ¿Cuál es la dirección?". Incluya un programa principal 
que lea una cadena del usuario, la capitalice utilizando su función y muestre el 
resultado.
"""
from utiles import encabezado

def capitalice(frase):
	carac_iniciales ="¡¿"
	carac_finales = ".!?"
	bandera_i = False
	bandera_f = False
	bandera_n = False
	salida = ""

	for x in frase:
		# determina si es el primer caracter de la frase
		if salida == "":
			x = x.upper()
			salida += x
			bandera_n = True


		# busca inicio de pregunta o exclamacion
		if bandera_i:
			x = x.upper()
			salida += x
			bandera_i = False
			bandera_n = True
		if (x in carac_iniciales):
			bandera_i = True
			

		# busca fin de pregunta o exclamacion
		if bandera_f:
			if x != " " and x !=".":
				x = x.upper()
				salida += x
				bandera_f = False
				bandera_n = True
		if (x in carac_finales):
			bandera_f = True

		# si no hay novedades, usa caracter normal
		if bandera_n:
			bandera_n = False
		else:
			salida += x
	return salida

titulo = "Ejercicio 8: Capitalízalo"
indicaciones = "Capitaliza los caracteres apropiados en una cadena"

encabezado(titulo,indicaciones)

cadena = input("Ingrese una frase: ")

print("")
print("Corregido:")
print(capitalice(cadena))