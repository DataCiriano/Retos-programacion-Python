#Programa que escribe los números del 0 al 100 
#Los múltiplos de 3 los cambia por Fizz y los de 5 por Buzz
#Si son múltiplos de 3 y de 5 los cambia por FizzBuzz

def fizzbuzz():
    for i in range(1,101):
        if (i%3 == 0) and (i%5 == 0):
            print("FizzBuzz")
        elif (i%3 ==0):
            print("Fizz")
        elif (i%5 == 0):
            print("Buzz")
        else:
            print(i)
    
fizzbuzz()

        