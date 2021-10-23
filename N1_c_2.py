"""
Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en 
Python que dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 
opciones:

Tamaño Normal: Mensaje "Pez en buenas condiciones"

Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"

Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"

Tamaño sobredimensionado: Mensaje "Pez contaminado"

"""

tamanio = ["", "1- Normal","2- Por debajo de lo normal","3- Un poco por encima de lo normal", "4- Sobredimensionado"]
contaminacion = ["","Pez en buenas condiciones","Pez con problemas de nutrición","Pez con síntomas de organismo contaminado","Pez contaminado"]

print("Indique la opción correspondiente al tamaño del pez")
print()
print(tamanio[1])
print(tamanio[2])
print(tamanio[3])
print(tamanio[4])
print()
op=int(input())


print("Nivel de Contaminación estimada: ")
print(contaminacion[op])

