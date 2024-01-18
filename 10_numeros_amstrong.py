
#Los números amstrong o narcisistas son aquellos que su valor es igual a al suma de sus dígitos elevados al número de cifras que tengan

#Ej: 9 = 9^1 es número amstrong, pero 10 = 1^2 + 0^2 != 10 no es número narcisista
# Realizar un programa que devuelva si el núemero introducido por el usuario es un número amstrong o no

def es_amstrong():
    
    num = input("Introduzca el número que desee comprobar: ")
    
    numero_cifras = len(num)
    numero = int(num)
    resultado = 0
    
    for i in num:
        resultado += int(i) ** numero_cifras
    
    if (numero == resultado):
        return f"El número {num} es un número amstrong."
    else:
        return f"El número {num} no es un número amstrong."
        

print(es_amstrong())

        
    
    
    
    
