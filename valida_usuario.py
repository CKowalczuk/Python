# programa que solicite nombre de usuario
# se verifica cumplimiento de las siguientes condiciones
# el nombre contener entre 8 - 15 caracteres. informar si no se cumpieron las dos condiciones
# nombre Usuario por lo menos 1 Vocal Mayuscula. Caso contrario informar este error.
# nombre Usuario por lo menos 1  caracter especial (*, #, &, @). Caso contrario informar este error.
# Al infal informar si el usario ingresado es un usuario valido o no de acuerdo a las reglas antes
# mencionadas

print("8 - 15 caracteres, por lo menos 1 Vocal Mayuscula, por lo menos 1 caracter especial (*, #, &, @)  ")
correcto = None
while correcto != "ok":  # -------------------------valida la cantidad de caracteres
	palabra = str(input("Ingrese la password: "))
	contador = 0
	MensajeCantidad = ""
	for x in palabra:
		contador+=1
	if contador >= 8 and contador <= 15:
		correcto = "ok"
	else: MensajeCantidad = "No se ingresó la cantidad correcta de Caracteres"
	
	correcto = None
	chequeo_vocal = None
	chequeo_especial = None
	MensajeVocal = ""
	MensajeEspecial = ""

	for x in palabra:
		if x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
			chequeo_vocal = "x"
		if x =="*" or x == "#" or x == "&" or x == "@":
			chequeo_especial = "x"
	if chequeo_vocal == "x" and chequeo_especial == "x":
		correcto = "ok"
	if chequeo_vocal != "x":
		MensajeVocal = "No se ingresó Vocal Mayuscula"
	if chequeo_especial != "x":
		MensajeEspecial = "No se ingresó caracter Especial"
	print(MensajeVocal)
	print(MensajeEspecial)
	print(MensajeCantidad)
print("Password OK")
