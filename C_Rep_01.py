# 1) Determinar el número mayor de 10 números ingresados.


x = 1
num1 = 0
mayor = 0
print("Ingrese 10 Números para determinar el mayor")
for x in range(10):
	num1 = int(input(str(x+1)+"°: "))
	if num1 > mayor:
		mayor = num1

print("El mayor número ingresado es:", mayor)
