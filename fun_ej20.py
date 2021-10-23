"""
Ejercicio 20: Fechas mágicas

Una fecha mágica es una fecha en la que el día multiplicado por el mes es 
igual al año de dos dígitos. Por ejemplo, junio 10,1960 es una fecha mágica 
porque junio es el sexto mes y 6 veces 10 es 60, que es igual al año de dos
dígitos. Escriba una función que determine si una fecha es mágica o no.
Use su función para crear un programa principal que encuentre y muestre
todas las fechas mágicas del siglo XX.

"""

from utiles import encabezado,dias_mes


def magica(dia,mes,anio):
	if dia * mes < 99:
		return anio == dia * mes
			


def todos_los_magicos():
	dia = 1
	for anio in range(1,99):
		for mes in range(1,13):
			while dia <= dias_mes(mes,anio):
				if magica(dia,mes,anio):
					print (str(dia).zfill(2), str(mes).zfill(2), str(anio).zfill(2), end="\t")
				dia +=1
			dia = 1

titulo = "Ejercicio 20: Fechas mágicas"
indicaciones = "fecha en la que el día por el mes es igual al año de dos dígitos"

encabezado(titulo,indicaciones)

dia = int(input("Ingrese día :"))
mes = int(input("Ingrese mes :"))
anio = int(input("Ingrese año :"))

print(magica(dia,mes,anio))
todos_los_magicos()