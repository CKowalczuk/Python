"""
Ejercicio 19: Reducir una fracción a los términos más bajos

Escriba una función que tome dos enteros positivos que representan el 
numerador y el denominador de una fracción como sus dos únicos parámetros.
El cuerpo de la función debe reducir la fracción a los términos más bajos 
y luego devolver el numerador y el denominador de la fracción reducida como
resultado. Por ejemplo, si los parámetros pasados a la 
función son 6 y 63, las funciones deberían volver 2 y 21. Incluya un 
programa principal que permita al usuario ingresar un numerador y un 
denominador. Entonces su programa debería mostrar la fracción reducida.

"""
from utiles import encabezado

def fraccion(num,den):
	if num > den:
		div=den
	else:
		div=num

	while div > 1:
		if num % div == 0 and den % div == 0:
			num = num//div
			den = den//div
		div -=1

	return num,den





titulo = "Ejercicio 19: Reducir una fracción a los términos más bajos"
indicaciones = "Devuelve la fracción minima equivalente"

encabezado(titulo,indicaciones)

numerador = int(input("Ingrese el Numerador  : "))
denominador = int(input("Ingrese el Denominador: "))

print(fraccion(numerador,denominador))