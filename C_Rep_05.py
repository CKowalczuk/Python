"""
5) Solicitar el ingreso de números al usuario y emitir un mensaje para determinar si es par o impar.
El ciclo debe finalizar cuando el usuario ingresa 0.

"""
num = None

while num != 0:
	num = int(input("Ingrese un número : "))
	if num % 2 != 0:
		print("Impar")
	else:
		print("Par")
	