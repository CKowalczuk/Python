#ESTA LA CREE PERO SIN LAS RESTA Y SUMAS SUCESIVAS EN DIVISION Y MULTIPLICACION RESPECTIVAMENTE

i = "si"
while  i != "no":
        print("hola bienvenido a calculadora atom")
        print("por favor digite la primera cifra que desea operar")
        n1 = input()
        try:
            entero = int(n1)
            print("digite otra cifra")
            n2 = input()
            try:
                entero = int(n2)
                print("a).suma")
                print("b).resta")
                print("c).multiplicación")
                print("d).division")
                print("e).potencia")
                print("f).modulo")
                opcion = input()
                m = ["a", "b", "c", "d", "e", "f"]
                if (opcion in m):
                    if  (opcion == "a"):
                        suma = float(n1) + float(n2)
                        print(f"su resultado es {suma}")
                        i = input("desea seguir (si o no) ")
                    if  (opcion == "b"):
                        resta = float(n1) - float(n2)
                        print(f"su resultado es {resta}")
                        i = input("desea seguir (si o no) ")
                    if (opcion == "c"):
                        multiplicacion = float(n1) * float(n2)
                        print(f"su resultado es {multiplicacion}")
                        i = input("desea seguir (si o no) ")
                    if (opcion == "e"):
                        potencia = float(n1) ** float(n2)
                        print(f"su resultado es {potencia}")
                        i = input("desea seguir (si o no) ")
                    if (opcion == "f"):
                        modulo = float(n1) % float(n2)
                        print(f"su resultado es {modulo}")
                        i = input("desea seguir (si o no) ")
                    if (opcion == "d"):
                        if (int(n1) == 0):
                            print("no se puede dividir entre cero")
                            if (int(n2) == 0):
                                print("no se puede dividir entre cero")
                            else:
                                division = float(n1) / float(n2)
                                print(f"su resultado es {division}")
                                i = input("desea seguir (si o no)")
                        else:
                            division = float(n1) / float(n2)
                            print(f"su resultado es {division}")
                            i = input("desea seguir (si o no)")
                else:
                    print("opcion incorrecta")
                    i = input("desea seguir (si o no)")
            except:
                print("por favor solo digite numeros")
                i = input("desea seguir (si o no)")
        except:
            print("por favor solo digite numeros")
            i = input("desea seguir (si o no)")