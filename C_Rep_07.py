"""
7) Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos 
valores A y B. El programa no permitirá introducir valores negativos para A y B y verificará que A 
es menor que B. Si A es mayor que B, se deben intercambiar los valores.

"""
numA = 0
numB = 0
while numA <= 0 or numB <=0:
	numA = int(input("Ingrese el valor de A: "))
	numB = int(input("Ingrese el valor de B: "))
if numA > numB:
	x = numA
	numA = numB
	numB = x
for x in range(numA,numB):
	if x % 5 == 0:
		print(x)



