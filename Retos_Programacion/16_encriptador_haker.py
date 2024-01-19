"""
Escribe un programa que reciba un texto y transforme lenguaje natural a
 "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 se caracteriza por sustituir caracteres alfanuméricos.
 Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 con el alfabeto y los números en "leet".
 (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

def haker_language(text):
    texto_leet = ""
    traductor = {
        "a": "4",
        "b": "|3",
        "c": "[",
        "d": "[)",
        "e": "3",
        "f": "|=",
        "g": "9",
        "h": "#",
        "i": "1",
        "j": "_]",      
        "k": "|<",
        "l": "|_",
        "m": "[V]",           
        "n": "|\|",
        "o": "Q",
        "p": "|°",         
        "q": "()_",
        "r": "/2",
        "s": "$",
        "t": "7",
        "u": "(_)",
        "v": "\/",
        "w": "\/\/",
        "x": "}{",
        "y": "'/",
        "z": "%",
        "0": "o",
        "1": "L",
        "2": "Z",
        "3": "E",
        "4": "A",
        "5": "S",
        "6": "b",
        "7": "T",
        "8": "B",
    }
    
    for caracter in text:
        if caracter.lower() in traductor:
            texto_leet += traductor[caracter.lower()]
        else:
            texto_leet += caracter
    
    return texto_leet


texto = input("Introduzca un texto para tranasformarlo: ")
print(haker_language(texto))