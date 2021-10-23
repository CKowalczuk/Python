# Les dejo la consigna del ejercicio complementario:
# 	Nos interesa mantener una agenda de contactos. Para eso vamos a desarrollar un programa en Python, que nos permita:
# 	1) Agregar una persona a nuestra lista de contactos.
# 	2) Eliminar personas de nuestra lista de contactos.
# 	3) Editar la información de una persona en nuestra lista de contactos.
# 	4) Listar información de todos nuestros contactos.
# 	   La lista debe mostrase de forma ordenada (alfabéticamente por apellido, de manera ascendente)
# 	5 ) Buscar información de un contacto en particular, por nombre o apellido (si existen mas de una coincidencias mostrarlas)
# 	De una persona nos interesa almacenar la siguiente información:
# 		- Nombre
# 		- Apellido
# 		- Dirección
# 		- Teléfono
# 		- Email
	
# 	Aclaraciones: Elijan las estructuras de datos mas convenientes para el escenario.
# 	Vamos a trabajar solo con variables, por lo que siempre, inicialmente cuando ejecutamos nuestros programas, la lista de contactos se encontrara vacia.
# 	Las acciones se deberán realizar dentro de un menú interactivo, donde el usuario elije la opción a realizar, y puede decidir salir del programa en algún momento.



def opciones_sino(si_no):
    while not si_no in ['si', 'no']:
        si_no = input('elija una opcion (si o no): ')
    return si_no

def imprimir_usuario_string(usuario, agenda_contactos):
        usuario_string = [(f'{c} : {v}') for c, v in agenda_contactos[usuario].items()]
        usuario_string = ', '.join(usuario_string)
        print(usuario_string)

   
def imprimir_datos_diccionario(diccionario):
    print(diccionario)
    for i in diccionario.keys():
        cada_dato = [f'USUARIO {i}:\n'] + [(f'{c} : {v}') for c, v in diccionario[i].items()]
        cada_dato = ' '.join(cada_dato)
        print(cada_dato)
    



agenda_contactos = {}
datos_usuario = {'1': 'usuario', '2': 'nombre', '3': 'apellido', '4': 'direccion', '5': 'telefono', '6': 'email'}
opcion = ''


while opcion != '6':

    print('\nBienvenidos')
    print('Elija una de las opciones: \n 1. Agregar usuario \n 2. Eliminar usuario \n 3. Editar usuario \n 4. Ver lista de informacion de todos los usuarios. \n 5 Buscar informacion de un usuario \n 6. Salir programa')

    opcion = input('Elija una opcion: ')

    if opcion == '1':
        usuario = input('ingrese un nombre de usuario para registrarse: ')
        nombre = input('Ingrese nombre: ')
        apellido = input('Ingrese apellido: ')
        direccion = input('Ingrese direccion: ')
        telefono = input('Ingrese telefono: ')
        email = input('Ingrese email: ')
    
        agenda_contactos.update({usuario: {'nombre': nombre, 'apellido': apellido, 'direccion': direccion, 'telefono': telefono, 'email': email}})
        


    if opcion == '2':
        eliminar_contacto = input('ingrese el usuario del contacto que quiere eliminar: ')

        try:
            imprimir_usuario_string(eliminar_contacto, agenda_contactos)
                        
            elegir_eliminar = opciones_sino(input('desea eliminar? si o no: '))
            if elegir_eliminar == 'si':
               agenda_contactos.pop(eliminar_contacto)
               
        except KeyError:
            print('EL CONTACTO INGRESADO NO EXISTE, INTENTE DE NUEVO')

    if opcion == '3':
        usuario_modificar = input('que contacto quiere modificar? ingrese usuario: ')
        try:
            if agenda_contactos[usuario_modificar]:
                dato_a_modificar = input('Que dato quiere modificar? 1: Usuario 2: nombre, 3: apellido, 4: direccion, 5: telefono, 6: email \n')
                nuevo_valor = input('ingrese nuevo valor: ')
                if dato_a_modificar == '1':
                    agenda_contactos[nuevo_valor] = agenda_contactos[usuario_modificar].copy()
                    del agenda_contactos[usuario_modificar] 
                    imprimir_usuario_string(nuevo_valor, agenda_contactos)

                else:
                    agenda_contactos[usuario_modificar][datos_usuario[dato_a_modificar]] = nuevo_valor
                    imprimir_usuario_string(usuario_modificar, agenda_contactos)
            
        except KeyError:
            print('EL CONTACTO INGRESADO NO EXISTE, INTENTE DE NUEVO')

    if opcion == '4':
        print('Esta es la infomracion de todos los contactos: \n')
        imprimir_datos_diccionario(agenda_contactos)
    
    if opcion == '5':
        busqueda = input('buscar usuario por: \n1. nombre usuario \n2. nombre \n3. apellido\n Ingresar parametro de busqueda: ')

        usuario = input('Ingrese el dato del usuario que quiere consultar sus datos: ')
        try:
            if busqueda == '1':
                imprimir_usuario_string(usuario, agenda_contactos)                      
            elif busqueda in ['2', '3']:
                print('Los siguientes usuarios coinciden con su busqueda')
                for i in agenda_contactos.keys():
                    if  agenda_contactos[i][datos_usuario[busqueda]] == usuario:
                        print('USUARIO:', i)
                        imprimir_usuario_string(i, agenda_contactos)
            else:
                print('PATRON DE BUSQUEDA INEXISTENTE')
            
        except KeyError:
            print('EL CONTACTO INGRESADO NO EXISTE, INTENTE DE NUEVO')
