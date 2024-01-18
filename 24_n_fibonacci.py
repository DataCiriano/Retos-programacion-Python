#Cálculo del n-ésimo término de la sucessión de Fibonacci con la fórmula de Binet 

#La fórmula de binet está explicada en el artículo sobre la serie de Fibonacci de la Wikipedia: 
# https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci

import math

# Calcular el número áureo
aureo = (1 + math.sqrt(5)) / 2

# Calcular el n-ésimo término de Fibonacci
def fibonacci_n(num):
    resultado = int((aureo**num - ((-aureo)**(-num)))/math.sqrt(5))
    return f"El {num} término de la serie de Fibonacci es: {resultado}"


num = int(input("Introduzca el término de la serie de Fibonacci que desea calcular: "))
print(fibonacci_n(num))
