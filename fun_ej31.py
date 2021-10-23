"""
Ejercicio 31: Calendario

Realizar un programa que pida un mes y un año (superior a 1900) y muestre 
el calendario del mes de esta manera:

 L   M   M   J   V   S   D

==========================
	 1   2   3   4   5   6

7    8   9  10  11  12  13

14  15  16  17  18  19  20

21  22  23  24  25  26  27

28  29  30  31

Para ello es necesario averiguar qué día de la semana (Lunes, Martes, …) 
corresponde con un fecha determinada.
"""
import calendar
from datetime import datetime, date
from utiles import encabezado, dias_mes


def calendario(anio,mes,primero):
	fila1=["","","","","","",""]
	fila2=["","","","","","",""]
	fila3=["","","","","","",""]
	fila4=["","","","","","",""]
	fila5=["","","","","","",""]
	fila6=["","","","","","",""]
	dia = 1
	for x in range(7):
		if x == primero:
			fila1[x] = dia
			dia +=1
			x+=1
			while x <= 6:
				fila1[x] = dia
				dia +=1
				x+=1
	for x in range(7):
		fila2[x] = dia+x
		fila3[x] = dia+x+7
		fila4[x] = dia+x+14
		if dia+x+21 <= dias_mes(mes,anio):
			fila5[x] = dia+x+21
		if dia+x+28 <= dias_mes(mes,anio):
			fila6[x] = dia+x+28

	
	print(fila1)
	print(fila2)
	print(fila3)
	print(fila4)
	print(fila5)
	print(fila6)


titulo = "Ejercicio 31: Calendario"
indicaciones = "Muestra el calendario del mes/año ingresado "

encabezado(titulo,indicaciones)


anio = int(input("ingrese año: "))
mes = int(input("ingrese mes: "))
primero = date(anio, mes, 1).weekday()



dias =  " L   M   M   J   V   S   D"
barra = "=========================="


print("%s / %s" %(mes,anio))
print(dias)
print(barra)
calendario(anio,mes,primero)

calendario_mes = calendar.month(anio, mes)
print("")
print("")
print("")
print("validacion con funcion date")
print(calendario_mes)



