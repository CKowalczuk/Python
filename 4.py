"""Calcula la sucesiónde números Fibonacci"""
# 'Calcula la sucesión de números Fibonacci'
# se definen las variables
a, b = 0, 1
while b < 2000:
    print(b),
    # se calcula la sucesión Fibonacci
    a, b = b, a + b