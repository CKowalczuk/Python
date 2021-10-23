"""
Ejercicio 17: Conversiones de bases arbitrarias

Escriba un programa que permita al usuario convertir un número de una base a otra.
Su programa debe admitir bases entre 2 y 16 tanto para el número de entrada como 
para el número de resultado. Si el usuario elige una base fuera de este rango, se 
debe mostrar el mensaje de error apropiado y el programa debe salir. Divida su 
programa en varias funciones, incluida una función que convierte de una base 
arbitraria a una base 10, una función que convierte de una base 10 a una base 
arbitraria y un programa principal que lee las bases y el número de entrada del 
usuario.
"""


from utiles import encabezado

def ent2bin(ent):
# recibe un entero, lo divide por 2 sucesivamente y toma los restos, 
# los resultados se agregan a una cadena de forma inversa para formar
# el numero binario 
	aux=""
	while ent / 2 != 0:
		aux = str(ent % 2) + aux
		ent = ent // 2
	return aux

def ent2oct(ent):
# recibe un entero, lo divide por 8 sucesivamente y toma los restos, 
# los resultados se agregan a una cadena de forma inversa para formar
# el numero octal 

	aux=""
	while ent / 8 != 0:
		aux = str(ent % 8) + aux
		ent = ent // 8
	return aux

def ent2hex(ent):
# recibe un entero, lo divide por 16 sucesivamente y toma los restos,
# si el resto es mayor a 9 busca su equivalencia en un diccionario 
# los resultados se agregan a una cadena de forma inversa para formar
# el numero alfanumerico 
	aux=""
	equival = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
	while ent / 16 != 0:
		if ent % 16 > 9:
			aux = equival[(ent % 16)] + aux
		else:
			aux = str(ent % 16) + aux
		ent = ent // 16
	return aux

def bin2ent(bina):
# recibe un binario, lo recorre de atras hacia adelante, elevando 
# el producto de cada dígito por 2 a la potencia de su posición en la 
# cadena menos 1, el resultado se acumula
	aux = 0
	pot = len(bina)-1
	for x in bina:
		aux = aux + (int(x)* 2 ** pot)
		pot = pot -1
	return aux

def bin2oct(bina):
# recibe un binario, lo convierte en entero llamando a bin2ent y luego en
# octal con la funcion ent2oct 
	return(ent2oct(bin2ent(bina)))	

def bin2hex(bina):
# recibe un binario, lo convierte en entero llamando a bin2ent y luego en
# hexadecimal con la funcion ent2hex 
	return(ent2hex(bin2ent(bina)))	

def oct2bin(oct):
# recibe un octal, lo convierte en entero llamando a oct2ent y luego en
# binario con la funcion ent2bin 
	return(ent2bin(oct2ent(oct)))	

def oct2ent(oct):
# recibe un octal, lo recorre de atras hacia adelante, elevando 
# cada dígito el producto de cada digito * 8 a la potencia de su posición 
# en las cadena menos 1, el resultado se acumula

	aux = 0
	pot = len(oct)-1
	for x in oct:
		aux = aux + (int(x)* 8 ** pot)
		pot = pot -1
	return aux

def oct2hex(oct):
# recibe un octal, lo convierte en entero llamando a oct2ent y luego en
# hexadecimal con la funcion ent2hex 
	return(ent2hex(oct2ent(oct)))	

def hex2bin(hexa):
# recibe un hexadecimal, lo convierte en entero llamando a hex2ent y luego en
# binario con la funcion ent2bin 
	return(ent2bin(hex2ent(hexa)))	

def hex2ent(hexa):
# recibe un hexadecimal recorre la cadena desde atras hacia adelante
# verifica si el valor es mayor que 9, en cuyo caso busca su equivalente
# en el diccionario, para luego elevar el producto de cada digito por 16 
# a la potencia de su posición en la cadena menos 1, acumula los resultados
	aux = 0
	pot = len(hexa)-1
	equival = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
	
	for x in hexa:
		x = x.lower()
		if x > "9":
			x = equival[x]
		
		aux = aux + (int(x)* 16 ** pot)
		pot = pot -1
	return aux


def hex2oct(hex):
# recibe un hexadecimal, lo convierte en entero llamando a oct2ent y luego en
# octal con la funcion ent2oct 
	return(ent2oct(hex2ent(hex)))	




titulo = "Ejercicio 17: Conversiones de bases arbitrarias"

indicaciones = "Convertir un número de una base a otra"

encabezado(titulo,indicaciones)


print("1 - Entero")
print("2 - Binario")
print("3 - Octal")
print("4 - Hexadecimal")
print("")

opcion = input("indique la base del valor a ingresar:")
entrada = input("Ingrese un valor a convertir : ")

print("")
if opcion == "1":
	print("El equivalente en Binario es     : ", ent2bin(int(entrada)))
	print("El equivalente en Octal es       : ", ent2oct(int(entrada)))
	print("El equivalente en Hexadecimal es : ", ent2hex(int(entrada)))
elif opcion == "2":
	print("El equivalente en Entero es      : ", bin2ent(entrada))
	print("El equivalente en Octal es       : ", bin2oct(entrada))
	print("El equivalente en Hexadecimal es : ", bin2hex(entrada))
elif opcion == "3":
	print("El equivalente en Binario es     : ", oct2bin(entrada))
	print("El equivalente en Entero es      : ", oct2ent(entrada))
	print("El equivalente en Hexadecimal es : ", oct2hex(entrada))
elif opcion == "4":
	print("El equivalente en Binario es     : ", hex2bin(entrada))
	print("El equivalente en Octal es       : ", hex2oct(entrada))
	print("El equivalente en Entero es      : ", hex2ent(entrada))
