#Programa que muestre lso números primos desde el 1 al 100

def es_primo(num):
    
    lista_primos = []
    
    for x in range(2, num+1):
        primo = True
        for y in range(2,x):
            if x % y == 0:
                primo = False
                break
        
        if primo:
            lista_primos.append(x)
    
    return lista_primos
        
    
    

resultado = es_primo(100)
print(resultado)