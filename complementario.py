"""
Nos interesa mantener una agenda de contactos. Para eso vamos a desarrollar
 un programa en Python, que nos permita:
1) Agregar una persona a nuestra lista de contactos.
2) Eliminar personas de nuestra lista de contactos.
3) Editar la información de una persona en nuestra lista de contactos.
4) Listar información de todos nuestros contactos.
           La lista debe mostrase de forma ordenada (alfabéticamente por 
           apellido, de manera ascendente)
5 ) Buscar información de un contacto en particular, por nombre o apellido 
(si existen mas de una coincidencias mostrarlas)
De una persona nos interesa almacenar la siguiente información:
        - Nombre
        - Apellido
        - Dirección
        - Teléfono
        - Email
        
Aclaraciones: Elijan las estructuras de datos mas convenientes para el 
escenario.
Vamos a trabajar solo con variables, por lo que siempre, inicialmente cuando 
ejecutamos nuestros programas, la lista de contactos se encontrara vacia.
Las acciones se deberán realizar dentro de un menú interactivo, donde el 
usuario elije la opción a realizar, y puede decidir salir del programa en 
algún momento.
"""        
import os

def menu():
    opciones="abcde"
    
    os.system("cls")
    print("\tAGENDA DE CONTACTOS")
    print("\t-------------------\n")
    print("\tA - Agregar Persona")
    print("\tB - Eliminar Persona")
    print("\tC - Editar Persona")
    print("\tD - Listar Agenda")
    print("\tE - Buscar Persona")
    print("\tX - Salir")

    print("")
    opcion = input("Ingrese Opción: ")
    if opcion.lower() in opciones:
        return opcion.lower()
    elif opcion.lower() == "x":
        print("Salida")
        return opcion.lower()
        

def agregar_persona():

    os.system("cls")
    print("\tAgregar Persona")
    print("\t-------------------\n")
    Apellido = input ("Apellido   : ")
    if Apellido in agenda:
        print("Ya existe un registro con ese Apellido")
        print("Presione una tecla para reintentar, 'X' para Salir")
        if input().lower() == "x":
            pass
    else:
        Nombre = input   ("Nombre     : ")
        Direccion = input("Direccion  : ")
        Telefono = input ("Telefono   : ")
        Email = input    ("Email      : ")       
        agenda[Apellido] = [Direccion, Nombre, Telefono, Email]

    print("Presione cuanlquier tecla para agregar mas registros, 'x' para terminar")
    if input().lower() == "x":
        pass
    return agenda
            
def eliminar_persona():

    os.system("cls")
    print("\tEliminar Registro")
    print("\t-------------------\n")
    Apellido = input ("Apellido   : ")
    if Apellido in agenda:
        print("Va a eliminar el registro con ese Apellido")
        print("Presione una tecla para confirmar, 'X' para Salir")
        if input().lower() == "x":
            pass
        else:
            del agenda[Apellido]
    print("Presione cuanlquier tecla para eliminar mas registros, 'x' para terminar")
    if input().lower() == "x":
        pass

def editar_persona():

    os.system("cls")
    print("\tEditar Registro")
    print("\t-------------------\n")
    Apellido = input ("Apellido   : ")
    while True:
        if Apellido in agenda:
            print("Va a Editar el registro con ese Apellido")
            print("Presione una tecla para confirmar, 'X' para Salir")
            if input().lower() == "x":
                break
            else:
                print ("1 -Nombre     : ",agenda[Apellido][0])
                print ("2 -Direccion  : ",agenda[Apellido][1])
                print ("3 -Telefono   : ",agenda[Apellido][2])
                print ("4 -Email      : ",agenda[Apellido][3])      
                print("")
                
                while True:
                    modificar = input("Indique el Número de dato a modificar: ")
                    nuevo_valor =""
                    if modificar == "1":
                        nuevo_valor = input ("Nuevo Nombre   : ")
                    elif modificar == "2":
                        nuevo_valor = input ("Nueva Dirección: ")
                    elif modificar == "3":
                        nuevo_valor = input ("Nuevo Teléfono : ")
                    elif modificar == "4":
                        nuevo_valor = input ("Nuevo Email    : ")
                    else:
                        print("Valores válidos 1 a 4, para cancelar presione 'x'")
                        modificar = input("Indique el Número de dato a modificar: ")
                        if modificar.lower() == "x":
                            break
                    if nuevo_valor != "":
                        agenda[Apellido][int(modificar)-1] = nuevo_valor
                        print("Registro Modificado")
                        modificar=""
        else:
            print("Registro no encontrado, para cancelar presione 'x'")
            print("Presione una tecla para Reintentar, 'X' para Salir")
            Apellido = input ("Apellido   : ")
            if input().lower() == "x":
                break
        
def listar_agenda():  
    os.system("cls")
    print("\tListar Agenda")
    print("\t-------------------\n")
    agenda_ordenada = sorted(agenda)
    for Apellido in agenda_ordenada:
        print(Apellido, "\t", agenda[Apellido][0],"\t", agenda[Apellido][1],"\t", agenda[Apellido][2],"\t", agenda[Apellido][3])
    input()    

def buscar_contacto():
    os.system("cls")
    print("\tBuscar Contacto")
    print("\t-------------------\n")
    criterio = input ("Ingrese el criterio de Búsqueda (1- Apellido 2- Nombre) : ")
    if criterio == "1":
        busqueda = input ("Apellido   : ")
        print(agenda.get(busqueda,"No encontrado"))


        # for Apellido in agenda:
        #     if busqueda in Apellido:
        #         print(Apellido, agenda[Apellido][0], agenda[Apellido][1], agenda[Apellido][2], agenda[Apellido][3])
        input()        
 
    elif criterio == "2":
        busqueda = input ("Nombre     : ")

        for c, v in agenda.items():
            if busqueda in v:
                # print(c, agenda[c])
                # y para que salga solo como string:
                print(c, ', '.join(agenda[c]))

        input()               



global agenda
agenda = {}
agenda = {"Alvarez": ["Ramonita", "SinNombre123", "111111111a", "111111111a@gmail.com"],
"Fernandez": ["Gustavo", "Cualquie 5678", "77777777b", "77777777b@gmail.com"],
"Insaurralde": ["Esteban", "Otro lado 333", "66666666e", "66666666e@gmail.com"],
"Dalvonse": ["Roberto", "Por ahi 3265", "44444444d", "44444444d@gmail.com"],
"Hablores": ["Roberto", "calle x 888", "55555555h", "55555555h@gmail.com"],
"Gutierrez": ["Sandra", "Luis y Lieda", "33333333f", "33333333f@gmail.com"],
"Felices": ["Tatiana", "Guastavino sn", "22222222g", "22222222g@gmail.com"]}


ejecutar = True
while ejecutar:
    opcion = menu()
    if opcion == "a":
        agregar_persona()
    elif opcion == "b":
        eliminar_persona()
    elif opcion == "c":
        editar_persona()
    elif opcion == "d":
        listar_agenda()
    elif opcion == "e":
        buscar_contacto()
    elif opcion == "x":
        ejecutar=False

