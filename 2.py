from pynput import keyboard as kb
numeros = "'1''2''3''4''5''6''7''8''9''0'"
ingresado = ""

def pulsa(tecla):
    global numeros
    global ingresado
    if tecla == kb.Key.enter:
        return False
    else:
        if kb.is_pressed('1'):
            ingresado = ingresado + str(tecla).strip("'")
        # print(str(tecla))



with kb.Listener(pulsa) as palabra:
    palabra.join()

print(ingresado)