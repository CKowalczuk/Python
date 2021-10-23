"""
Ejercicio 18: Días en un mes

Escriba una función que determine mostrar cuántos días hay en un mes en
particular. Su función tomará dos parámetros: el mes como un número entero
entre 1 y 12, y el año como un número entero de cuatro dígitos. 
Asegúrese de que su función informa el número correcto de días en 
febrero para los años bisiestos. Incluya un programa principal que
lea un mes y un año del usuario y muestre el número de días en ese mes.
"""
from utiles import encabezado


def dias_mes(mes,anio):
	meses_30_dias = [4, 6, 9, 11]
	dias = 0
	if month == 2:
		if anio % 4 == 0:
			dias = 29
		else:
			dias = 28
	else:
		if mes in meses_30_dias:
			dias = 30
		else:
			dias = 31
	return dias



titulo = "Ejercicio 18: Días en un mes"
indicaciones = "Devuelve el número de días de un mes ingresado"

encabezado(titulo,indicaciones)



year = int(input("Ingrese año a consultar (AAAA): "))
month = int(input("Ingrese día a consultar (MM)  : "))


print("En el mes %i del año %i, los días son %i" % (month,year,dias_mes(month,year)))



