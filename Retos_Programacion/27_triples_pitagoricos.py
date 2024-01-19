
"""
    Crea una función que encuentre todos los triples pitagóricos (ternas) menores o iguales a un número dado.
        - Debes buscar información sobre qué es un triple pitagórico.
        - La función únicamente recibe el número máximo que puede aparecer en el triple.
        - Ejemplo: Los triples menores o iguales a 10 están formados por (3, 4, 5) y (6, 8, 10).
 """
 
def triples_pitagoricos(max:int):
    triples = []
    
    for a in range (1, max+1):
        for b in range (a, max+1):
            c = (a**2 + b**2)**0.5 #Calcular hipotenusa
            
            if c.is_integer() and c <= max:
                triples.append((a,b,int(c))) #Convertimos c a entero para que no muestre decimales en el resultado final
                
    return triples
             
max = int(input("Introduzca el numero máximo para calcular los triples pitagóricos: "))

resultado= triples_pitagoricos(max)
print(resultado)