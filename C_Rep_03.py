"""
3) Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas.
"""
res=0
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
for x in range(num2):
	res+=num1

print("Resultado : ",res)
