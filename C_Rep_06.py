"""
6) Imprimir, contar y sumar los múltiplos de 2 que hay entre una serie de números, tal que el segundo
sea mayor o igual que el primero.

"""
contador = 0
suma = 0
num1 = int(input("Ingrese un número : "))
num2 = int(input("Ingrese un número : "))

for x in range(num1,num2):
	if x % 2 == 0:
		contador+=1
		suma+=x
		print(x, contador, suma)