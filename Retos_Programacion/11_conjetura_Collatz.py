
#Conjuetura matemática para enteros POSITIVOS solamente

#Si el número introucido es par se divide entre 2 hasta alcanzar el resultado de 1
#Si el número introducido es impar se multiplica por 3 y se le suma 1, despues se divide entre 2 hasta el resultado final de 1

def conjetura_collatz(num):
    numero = num
    pasos = 0
    
    while num != 1:
        
        if num%2 == 0: 
            num = num/2
        else:
            num = 3*num +1
            
        pasos += 1
            
    print(f"El número de pasos necesarios para el número {numero} es: {pasos}")
        
numero = int(input("Introduzca un número entero: "))
conjetura_collatz(numero)
        