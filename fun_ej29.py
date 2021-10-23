"""
Ejercicio 29: Conversiones entre base decimal y binaria

Realizar dos funciones una que nos permita convertir un número entero a 
binario, y otra que nos permita convertir un numero binario a decimal, 
convertir_a_binario recibe un número entero y devuelve una cadena con la 
representación del número en binario y convertir_a_decimal recibe una cadena 
con la representación binaria de un número y devuelve el número en decimal.
Crea un programa principal que permita convertir un numero ingresado por el 
usuario de decimal a binario o de binario a decimal según corresponda.
"""
from utiles import encabezado, ent2bin, bin2ent



titulo = "Ejercicio 29: Conversiones entre base decimal y binaria"
indicaciones = "Convierte un numero en entero en binario viceversa"

encabezado(titulo,indicaciones)

entero= int(input("Ingrese el número Entero a Convertir a Binario: "))
print("")
print("El número Binario correspondiente al ingresado es : ", ent2bin(entero))
print("")
binario= input("Ingrese el número Binario a Convertir a Entero: ")
print("")
print("El número Entero correspondiente al ingresado es : ", bin2ent(binario))