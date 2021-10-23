import os #importa libreria OS para funcion de limpiar la pantalla

def encabezado(tit, indic):
	os.system("cls")
	ancho = os.get_terminal_size()
	cadena_a_imprimir = ""
	for x in range(int(ancho.columns)):
		cadena_a_imprimir += "-"
	
	print(cadena_a_imprimir)
	print(tit)
	print(cadena_a_imprimir)
	print("")
	print(indic)
	print(cadena_a_imprimir)
	print("")


def dias_mes(mes,anio):
	meses_30_dias = [4, 6, 9, 11]
	dias = 0
	if mes == 2:
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

def ent2bin(ent):
# recibe un entero, lo divide por 2 sucesivamente y toma los restos, 
# los resultados se agregan a una cadena de forma inversa para formar
# el numero binario 
	aux=""
	while ent / 2 != 0:
		aux = str(ent % 2) + aux
		ent = ent // 2
	return aux

def bin2ent(bina):
# recibe un binario, lo recorre de atras hacia adelante, elevando 
# el producto de cada dígito por 2 a la potencia de su posición en la 
# cadena menos 1, el resultado se acumula
	aux = 0
	pot = len(bina)-1
	for x in bina:
		aux = aux + (int(x)* 2 ** pot)
		pot = pot -1
	return aux

def dias_mes(mes,anio):
	meses_30_dias = [4, 6, 9, 11]
	dias = 0
	if mes == 2:
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