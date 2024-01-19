"""
Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""
import math

def par_primo_fibonacci(num):
    
    resultado = f"El {num} "
    
    #Comprobar si el número es par
    if num % 2 == 0:
        resultado += "es par, "
    else:
        resultado += "es impar ,"
        
    # resultado += "es par" if num % 2 == 0 else "es impar"  Así se haría la comprobación de si es par con una ternaria
        
    #Comprobar si el número es primo
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                resultado += "no es primo, "
                break
        else:
            resultado += "es primo, "
    else:
        resultado += "no es primo, "
        
    #Comprobar si es fibonacci
    
    if num in fibonacci(num+2): 
        resultado += "es Fibonacci."
    else:
        resultado += "no es Fibonacci."
        
    #Sumo 2 para que la lista de Fibonacci se calcule con seguridad hasta un número mayor del introducido por el usuario
    #Si no sumamos 2 para el cálculo de la lista de Fibonacci los números 2, 3 y 5 da erros y no lso considera Fibonacci cuado si son
    
    return resultado


def fibonacci(num): #Función para calcular la lisa de fibonacci hasta un número introducido
    lista_fibonacci = [1]
    a = 0
    b = 1
    
    for i in range(2,num): #También podría sumar aqui 2 y que la lsita se calcule hasta dos términos más 
        c = a + b
        a = b
        b = c
        
        lista_fibonacci.append(c)
        
    return lista_fibonacci
    
    
    
num = int(input("Introduzca un número entero: "))
print(par_primo_fibonacci(num)) 


