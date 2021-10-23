#Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos valores A y B. 
#El programa no permitirá introducir valores negativos para A y B y verificará que A es menor que B. 
#Si A es mayor que B, se deben intercambiar los valores.
import time

print("\nCALCULO DE SUMA DE MULTIPLOS DE CINCO DE UN RANGO DE NUMEROS")
numero_1=None
numero_2=None
rango_a=None
rango_b=None
acumulador=0
while numero_1 !=0: 
    numero_1=input("\nIngrese el primer número del rango: ")
    if not numero_1.isdigit():
        print("\nNo se admite letras ni números negativos, ingrese el primer valor del rango: ")
        time.sleep(1)
        continue
    numero_1=int(numero_1)
    break
while numero_2 !=0:
    numero_2=input("\nIngrese el segundo número del rango: ")
    if not numero_2.isdigit():
        print("\nNo se admite letras ni numeros negativos, ingrese el segundo valor del rango: ")
        time.sleep(1)
        continue
    numero_2=int(numero_2)
    break
if numero_1>numero_2:
    rango_a=numero_2
    rango_b=numero_1+1
else:
    rango_a=numero_1
    rango_b=numero_2+1
x=list(range(rango_a , rango_b)) #se uso para comprobar que las validadciones y requisitos del ejercicio se cumplen
#print (x)
# cuando es multiplo de 5 un numero? cuando su division por 5 da modulo 0.
for i in x:
    if i % 5 ==0:
        acumulador=acumulador+i
        continue
print("-----------------------------------------------------------------------------------------------")
print("LA SUMA DE LOS NUMEROS MULTIPLOS DE 5 QUE EXISTEN EL EN RANGO QUE DEFINISTE ES DE: ","|",acumulador,"|")
print("-----------------------------------------------------------------------------------------------")
time.sleep(1)