
cont = 0
suma = 0

N = int(input("Ingrese tope maximo: "))

while cont <= N:
	suma = suma + cont
	cont = cont + 1

print("La suma total es: ",suma)

#----------------------------------------------

numero = int(input("Escriba un número positivo: "))
while numero < 0:
	print("¡Ha escrito un número negativo! Inténtelo de nuevo")
	numero = int(input("Escriba un número positivo: "))

print("Gracias por su colaboración")


#----------------------------------------------

c = 0
while c <= 5:
	c+=1
	print("c es igual a: ",c)
else:
	print("Se ha completado toda la iteración y c vale", c)


#----------------------------------------------

print("Comienzo")

for i in range(3):
	print("Hola ", end="")

print("Final")


#----------------------------------------------


while True:
	op = input('Ingrese cualquier palabra, termina con FIN--> ')
	if op == 'FIN':
		break
	else:
		print(op)
		print('Terminó la ejecución con FIN')


#----------------------------------------------

for letra in "Python":
	if letra == "h":
		break
print("Letra actual :", letra)


#----------------------------------------------

var = 10

while var > 0:
	var = var -1
	if var == 5:
		break
	print("Valor actual de la variable :", var)