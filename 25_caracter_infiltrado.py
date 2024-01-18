
"""Crea una función que reciba dos cadenas de texto casi iguales, a excepción de uno o varios caracteres. 

La función debe encontrarlos y retornarlos en formato lista/array.
    - Ambas cadenas de texto deben ser iguales en longitud.
    - Las cadenas de texto son iguales elemento a elemento.
    - No se pueden utilizar operaciones propias del lenguaje que lo resuelvan directamente.

 Ejemplos:
    - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
    - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
"""
 
 
def descubrir_infiltrado():
    
    longitud_correcta = False
    lista_01 = []
    lista_02 = []
    lista_distintos = []
    
    print("\nSe le van a pedir dos cadenas de texto que deben tener el mismo número de caracteres.\n")
    
    while longitud_correcta == False:
    
        cadena_01 = input("Introduzca la primera cadena de texto: ")
        cadena_02 = input("Introduzca la segunda cadena de texto: ")
        
        if len(cadena_01) == len(cadena_02):
            longitud_correcta = True
            break
        else:
            print("\nLas cadenas de texto introducidas no tienen el mismo número de caracteres. Vuelva a intentarlo.\n")
    
    for letra in cadena_01:
        lista_01.append(letra)
    
    for letra in cadena_02: 
        lista_02.append(letra)
        
    for letra_01, letra_02 in zip (lista_01, lista_02):
        if letra_01 != letra_02:
            lista_distintos.append(letra_01)
            lista_distintos.append(letra_02)
                
    print(lista_distintos)
    
    


descubrir_infiltrado()