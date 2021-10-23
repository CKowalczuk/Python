"""
Desarrollar una solución que calcule la suma de
los cuadrados de los n primeros números naturales: 1 + 22 + 32 +… + n2.
​
"""
acum=0
cuadrado=0
max=int(input("ingrese un numero: "))
x=max+1
for i in range(x):
	cuadrado= i**2
	acum=acum+cuadrado
	print("primer numero: %i, la suma acumulada: %i" % (cuadrado, acum))
