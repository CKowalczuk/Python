cantidad = int(input("Ingrese la cantidad de la compra: "))
precio = float(input("Ingrese el Valor de la unidad: "))

if cantidad >= 10:
	print("Precio total de la compra :",(precio * 0.8)*cantidad)
else:
	print("Precio total de la compra :",(precio *cantidad))