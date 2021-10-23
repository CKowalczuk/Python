# 2) Desarrollar una solución que calcule la suma de los cuadrados de los n primeros números
# naturales: 1 + 22 + 32 +… + n2.
# contador = 0
print("Cálculo de la suma de los cuadrados de los n primeros números naturales:")
iteraciones = int(input("Indique la cantidad de Iteraciones: "))
resultado = 0
for contador in range(1,iteraciones+1):
	resultado = resultado + contador * contador

print("Resultado: ",resultado)