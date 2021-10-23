"""
# Imprimir los valores pasados como parámetro.

def indeterminados(*args):
    for arg in args:
        print(arg)

indeterminados(5, "Hola", [1, 2, 3, 4, 5])


def indeterminados(**kwargs):
    # Esta función imprime los valores pasados como parámetro
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

indeterminados(n=5, c="Hola", l=[1, 2, 3, 4, 5])



def super_funcion(*args, **kwargs):
    # Esta función imprime los valores pasados como parámetro por posición y nombre
    total = 0
    for arg in args:
        total += arg
        print("Total", "=>", total)
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

super_funcion(50, -1, 1.56, 10, 20, 300, c="Hola", n=3)

"""

# Modificar el valor de los elementos pasados como parámetro.
def funcion(x, y):
# Esta función actualiza los valores de los argumentos pasados Como parámetro
    x = x + 3
    # y = y + [3]
    y.append(23)
    print(x, y)

x =  22
y =  [22]
funcion(x, y)
print(x, y)
