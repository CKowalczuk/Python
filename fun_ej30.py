"""
Ejercicio 30: Números romanos

Crear un programa que convierta un número entero (mayor que 1 y menor o igual 
que 1000) a su representación en números romanos. Use la función en un 
programa principal y pruebe su código en varias combinaciones de valores
diferentes.

"""

from utiles import encabezado

def romano(entero):
	runidad=""
	rdecena=""
	rcentena=""
	ur = {0:"",1: "I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
	dr = {0:"",1: "X",2:"XX",3:"XXX",4:"XL",5:"L",6:"LX",7:"LXX",8:"LXXX",9:"XC"}
	cr = {0:"",1: "C",2:"CC",3:"CCC",4:"XD",5:"D",6:"DC",7:"DXX",8:"DCCC",9:"CM"}
	
	if len(entero)==1:
		runidad=ur[int(entero[0])]
	elif len(entero) == 2:
		rdecena=dr[int(entero[0])]
		runidad=ur[int(entero[1])]
		# unidad=entero[0]
		# decena=entero[1]
	elif len(entero) == 3:
		rcentena=cr[int(entero[0])]
		rdecena=dr[int(entero[1])]
		runidad=ur[int(entero[2])]

	return rcentena+rdecena+runidad


titulo = "Ejercicio 30: Números romanos"
indicaciones = "Convertir en numeros romanos un entero entre 1 y 1000"

encabezado(titulo,indicaciones)

entero= input("Ingrese el entero a convertir: ")
print("")
print(romano(entero))
