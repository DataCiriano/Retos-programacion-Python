#Función que reciba dos palagras (string) y retorne verdadero o falso según sean o no anagramas
#Un anagrama consiste en reordenar TODAS las letras de una palabra para formar otra

#LA PRIMERA SOLUCIÓN ES LA QU SE ME OCURRIO A MÍ Y ES CORRECTA, LA SEGUNDA ME LA DIÓ CHAT-GPT Y ES MAS AVANZADA

def es_anagrama():
    
    palabra_01 = input("Introduzca la primera palabra: ").lower().replace(" ","")
    palabra_02 = input("Introduzca l segunada palabra: ").lower().replace(" ","")
    
    letra_igual = 0
    
    if (len(palabra_01) != len(palabra_02)):
        print("Las palabras introducidas tienen diferente número de caracteres, no pueden ser una anagrama la una de la otra.")
    else:
        for letra in palabra_01:
            if letra in palabra_02:
                letra_igual += 1
                if letra_igual == len(palabra_02):
                    print("La primera palabra es anagrama de la segunda.")
            else:
                print("La primera palabra no es anagrama de la segunda.")
                break    
        
es_anagrama()

from collections import Counter

def anagrama_mejorado():
    
    palabra_01 = input("Introduzca la primera palabra: ").lower().replace(" ","")
    palabra_02 = input("Introduzca l segunada palabra: ").lower().replace(" ","")
    
    if (len(palabra_01) != len(palabra_02)):
        print("Las palabras introducidas tienen diferente número de caracteres, no pueden ser una anagrama la una de la otra.")
        return
    
    contador_01 = Counter(palabra_01)
    contador_02 = Counter(palabra_02)
    
    if contador_01 == contador_02:
        print("La primera palabra es anagrama de la segunda.")
    else:
        print("La primera palabra NO es anagrama de la segunda.")
        
    
anagrama_mejorado()

"""El módulo collections proporciona una variedad de estructuras de datos y utilidades. Uno de los objetos más útiles que ofrece es el Counter, 
que se utiliza para contar elementos en una colección"""
#Counter es una subclase de dict (diccionario) y permite contar las ocurrencias de elementos en una secuencia.
#Creamos un Counter pasándole una secuencia iterable (lista, tupla o cadena)