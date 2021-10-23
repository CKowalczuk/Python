"""
edad = int(input("Ingrese la edad: "))

if edad > 18:
	print("Persona Mayor de edad")
else:
	print("Persona Menor de edad")


#--------------------------------------------------

cont_correcta = "python"
contrasenia= input("Ingrese la contraseña: ")
cont = 0

while (contrasenia != cont_correcta) and (cont < 4):
	cont+=1
	print("La contraseña ingresada es incorrecta")
	print("Intentos restantes: ",5 - cont)
	contrasenia= input("Ingrese la contraseña: ")

if contrasenia == cont_correcta:
	print("Contraseña Correcta")
else:
	print("Cuenta Bloqueada")


#--------------------------------------------------

preguntas = int(input("Ingrese la cantidad de preguntas"))
respuestas = int(input("Ingrese la cantidad de respuestas correctas"))

porcentaje = (respuestas*100)/preguntas
print(porcentaje)

if porcentaje >= 90:
	print("EXCELENTE")
elif porcentaje >= 70:
	print("BUENO")
elif porcentaje >= 60:
	print("APROBADO")
else:
	print("NO ALCANZÓ")

#--------------------------------------------------


print("BIENVENIDOS A PIZZERIA BELLA NAPOLI")

pedido = input("Desea ordenar una Pizza Vegetariana? S/N: ")
while pedido != "S" and pedido != "N":
	print("Opción Incorrecta, Use S o N en Mayúsculas, gracias")
	pedido = input("Desea ordenar una Pizza Vegetariana? S/N: ")

if pedido == "S":
	print("Ingredientes: 1- Pimiento, 2- Rúcula")
	ing = int(input("Seleccione un Ingrediente 1 o 2"))
else:
	print("Ingredientes: 1- Jamon, 2- Panceta")
	ing = int(input("Seleccione un Ingrediente 1 o 2"))

print("Ingredientes de su pedido:\n","Tomates \n","Mozzarela\n")

if pedido == "S":
	if ing == 1:
		print("Pimiento")
	else:
		print("Rúcula")
else:
	if ing == 1:
		print("Jamon")
	else:
		print("Panceta")

#--------------------------------------------------

nombre = input("Ingrese su nombre: ")
turno = input("Ingrese su turno T (Tarde) o N (Noche): ")

if nombre < "M" and turno == "T":
	print("GRUPO A")
elif nombre > "N" and turno == "N":
		print("GRUPO A")
else:
	print("GRUPO B")

print(nombre < "M" and turno == "T")

"""
#--------------------------------------------------
