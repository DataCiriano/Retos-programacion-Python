#Programa que realice la sucesión de Fibnacci lso 50 primeros números de la sucessión empezando en el 0

def fibonacci():
    
    lista_fibonacci = [1]
    
    a = 0
    b = 1
    
    for i in range(2,50): # Generamos 50 términos, empezando desde el tercer término (índice 2).
        c = a + b
        a = b
        b = c
        
        lista_fibonacci.append(c)   
        
    print(lista_fibonacci) 
    
    
fibonacci()

#Con una función lambda quedaría así
"""
fibonacci = lambda n: [0, 1] + [fibonacci(i-1) + fibonacci(i-2) for i in range(2, n+1)]
print(fibonacci(51))
"""