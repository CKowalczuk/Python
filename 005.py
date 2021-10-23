"""
edad = int(input("Ingrese la edad: "))

if edad >= 18:
	print("Persona Mayor de edad")
else:
	print("Persona Menor de edad")
"""

# --------------------------------------------------------------

importe = float(input("Ingrese el importe de la compra para calcular el descuento: "))
descuento = 0.0

if importe >= 1500:
	print("Descuento 30%")
	descuento = importe * 0.3
elif importe >= 1000:
	print("Descuento 20%")
	descuento = importe * 0.2
elif importe >= 750:
	descuento = importe * 0.1
	print("Descuento 10%")
elif importe >= 500:
	descuento = importe * 0.05
	print("Descuento 5%")
else:
	print("No se aplica descuento")
print("importe de la venta: ", importe - descuento)

