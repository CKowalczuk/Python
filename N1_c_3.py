"""
Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen
 a continuación.

Ingredientes comunes: Verduras y berenjena.

Ingredientes Receta 1: Lentejas y apio.

Ingredientes Receta 2: Morrón y Cebolla..

Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta
le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir 
3 ingrediente (entre la receta elegida y los comunes.) y el tipo de receta. Al final se debe mostrar 
por pantalla la receta elegida y todos los ingredientes.
"""

comunes ="Verduras y berenjena"
Receta1 =["Lentejas","apio"]
Receta2 =["Morrón","Cebolla"]

print()
print("Receta 1 -",comunes, "con Opcionales (1) ", Receta1[0],"o", Receta1[1])
print("Receta 2 -",comunes, "con Opcionales (1) ", Receta2[0],"o", Receta2[1])

eleccion = int(input("Indique el tipo de receta que desea"))

print(eleccion)

if eleccion == 1:
	opcional = int(input("Indique el Opcional 1 " + Receta1[0] +"o 2 " +Receta1[1]))
	print("OK, los ingredientes de su pedido son:", comunes, "con", Receta1[opcional -1])
else:
	opcional = int(input("Indique el Opcional 1 " + Receta2[0] +"o 2 " +Receta2[1]))
	print("OK, los ingredientes de su pedido son:", comunes, "con", Receta2[opcional -1])
