'''
Consigna 2: Validación de nombre de usuario

Escribir un programa que solicite el ingreso de un nombre de usuario.

Se deberá verificar que se cumplan las siguientes condiciones:

El nombre de usuario debe contener como mínimo 8 caracteres y como máximo 15. Caso contrario informar
Longitud mínima es de 8 caracteres si es que no se cumplió esta condición.
Longitud máxima permitida de 15 caracteres, si es que no se cumplió esta condición.
El nombre de usuario debe contener al menos alguna vocal en mayúscula. 
Caso contrario informar este error El nombre de usuario debe contener al menos algún carácter especial (*, #, &, @). 
Caso contrario informar este error. 
Al final informar si el usuario ingresado es un usuario valido o no, de acuerdo a las reglas anteriormente mencionadas

'''


# Validación de nombre de usuario #

user = None

# Usuario #
while user is None:
    user = input("Ingrese un nombre de usuario: ")
    if len(user) > 15:
        print("Longitud maxima permitida es 15 caracteres.")
        user = None
    elif len(user) < 8:
        print("Longitud minima permitida es 8 caracteres.")
        user = None
    elif not any(i in {"A", "E", "I", "O", "U"} for i in user):
        print("El nombre debe contener por lo menos una vocal mayúscula.")
        user = None
    elif not any(i in {"*", "#", "&", "@"} for i in user):
        print("El nombre debe contener por lo menos una caracter especial: *, #, &, @.")
        user = None
    else:
        print("El nombre de usuario es correcto.")
