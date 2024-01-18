
"""
Crea una función que calcule el número de la columna de una hoja de Excel teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
"""

import string #este modulo me permite generar automáticamente las letras del alfabeto

def calculate_column_number(column_name: str):
    
    column_number = 0 #inicializamos el valor de la columna
    
    alphabet = list(string.ascii_uppercase) #list transforma las letras generadas por el método string en una lista
    
    for letter in column_name.upper(): #upper() es para asegurarnos por si meten una minúscula
        
        column_number = (column_number * len(alphabet)) + (alphabet.index(letter) + 1) #index devuelve el índice 
    
    
    return column_number


print(calculate_column_number("A"))
print(calculate_column_number("Z"))
print(calculate_column_number("AA"))
print(calculate_column_number("CA"))



"""
     column_number = (column_number * len(alphabet)) + (alphabet.index(letter) + 1)
     
     el primer paréntesis multiplica el número de columna por la longitud de todas als letras para poder operar cuando tenemos una columna
     definida por mas de una letra
     el segunto término suma el valor de la siguiente letra 
"""