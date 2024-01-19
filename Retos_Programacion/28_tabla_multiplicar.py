 
""" 
Crea un programa que sea capaz de solicitarte un número y se encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
    - Debe visualizarse qué operación se realiza y su resultado.
    Ej: 1 x 1 = 1
        1 x 2 = 2
        1 x 3 = 3
        ...
"""

def tabla_multiplicar(tabla):
    for i in range (1,10+1):
        print(f"{tabla} * {i} = {i*tabla}")
        

tabla = int(input("Introduzca la tabla de multiplicar que desee ver: "))

resultado = tabla_multiplicar(tabla)
print(resultado)
    
    
    
    
