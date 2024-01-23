"""
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""

def agenda():
    dict_agenda = {"Bomberos": '1234', "Policia": '091', "Emergencias": '112'}

    while True:
        def menu():
            print("""Accediendo a la agenda de contactos...\n
                Elija una opción por favor:
                -------------------------------------------
                Opcion 1: Nuevo contacto 
                Opción 2: Busqueda de un contacto existente
                Opción 3: Editar contacto existente
                Opcion 4: Eliminar un contacto existente
                Opcion 5: Salir\n""")
        menu()

        opcion = int(input("Indique una opción: "))
        
        match opcion:

            case 1:
                agregar_contacto(dict_agenda)

            case 2:
                buscar_contacto(dict_agenda)

            case 3:
                editar_contacto(dict_agenda)

            case 4:
                eliminar_contacto(dict_agenda)

            case 5:
                print("¡Gracias por usar nuestra agenda! ¡Hasta luego!")
                break


def agregar_contacto(diccionario):
    nombre = input("Introduzca el nombre del nuevo contacto: ").lower().capitalize()
    telefono = input("Introduzca un número de teléfono de máximo 11 dígitos: ")
    
    while not (telefono.isdecimal() and len(telefono) > 0 and len(telefono) <= 11):
        telefono = input("Número de teléfono inválido. Vuelva a intentarlo: ")
        
    diccionario[nombre] = telefono
    print(f"¡Contacto {nombre} añadido correctamente!\n")
    imprimir_contactos(diccionario)


def buscar_contacto(diccionario):
    print("-----Buscador de contactos-----")
    contacto = input("Introduzca el nombre del contacto: ").lower().capitalize()

    if contacto in diccionario:
        print(f"{contacto}: {diccionario[contacto]}\n")
    else:
        respuesta = input("No hay ningún contacto en la agenda con ese nombre. ¿Desea realizar otra acción? Y/N ").lower()
        if respuesta != 'y':
            print("¡Gracias por usar nuestra agenda! ¡Hasta luego!")


def editar_contacto(diccionario):
    print("-----Editor de contactos-----")
    imprimir_contactos(diccionario)
    contacto = input("Indique el nombre del que desea editar: ").lower().capitalize()

    if contacto in diccionario:
        respuesta = input("¿Desea editar el nombre del contacto (1) o el número (2)? : ")
        if respuesta == '1':
            nuevo_nombre = input("Introduzca el nuevo nombre de contacto: ").lower().capitalize()
            diccionario[nuevo_nombre] = diccionario.pop(contacto)
        elif respuesta == '2':
            nuevo_numero = input("Introduzca el nuevo número de teléfono: ")
            while not (nuevo_numero.isdecimal() and len(nuevo_numero) <= 11):
                nuevo_numero = input("Número de teléfono inválido. Vuelva a intentarlo: ")
            diccionario[contacto] = nuevo_numero
        print("Contacto editado correctamente.\n")
        imprimir_contactos(diccionario)
    else:
        print("No hay ningún contacto en la agenda con ese nombre.\n")


def eliminar_contacto(diccionario):
    print("-----Eliminar un contacto-----")
    imprimir_contactos(diccionario)
    contacto = input("¿Qué contacto desea eliminar? ").lower().capitalize()

    if contacto in diccionario:
        valor_eliminado = diccionario.pop(contacto)
        print(f"Se eliminó el contacto {contacto} con el valor {valor_eliminado}\n")
        imprimir_contactos(diccionario)
    else:
        print("No hay ningún contacto en la agenda con ese nombre.\n")


def imprimir_contactos(diccionario):
    print("Estos son los contactos almacenados en la agenda:")
    for nombre, telefono in diccionario.items():
        print(f"{nombre}: {telefono}")
    print()


agenda()