
#-----FUNCIONES RECURSIVAS-----

#Función recursiva: es aquella función que se llama a si misma dentro de su propia ejecución


#Función que imprime los números desde un inicio hasta un final:

def print_numbers_recursive(start:int, end:int):
    if start <= end:
        print(start)
        print_numbers_recursive(start + 1, end)

print_numbers_recursive(0, 100)



#Función factorial:

def factorial(num:int) -> int:
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
answer = int(input("¿De qué número desea calcualr el factorial? "))

result = factorial(answer)
print(f"El factorial de {answer} es {result}")



#Función que devuelve el valor de la serie de Fibonacci por la posición:

def fibonacci(position:int):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)
    
answer = int(input("¿Qué posición de la serie de Fibonacci desea conocer? "))    
    
result = fibonacci(answer)
print(f"El valor de Fibonacci de la posición {answer} es: {result}")
    


#Función que suma los dígitos de un número:

def digits(num):
    if num == 0:
        return 0
    else:
        return numero % 10 + digits(num // 10)

result= digits(12345)
print(result)