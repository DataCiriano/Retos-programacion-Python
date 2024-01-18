import random

def generar_carton(): 
    numeros_posibles = (random.sample(range(1,90),15))
    numeros_posibles.sort()
    
    linea1 = numeros_posibles[:5]
    linea2 = numeros_posibles[5:10]
    linea3 = numeros_posibles[10:15]

    return linea1, linea2, linea3

def mostar_carton(carton):
    for linea in carton:
        print(" ".join(map(str, linea)))    

def sacar_numero(numeros_bombo):
    if numeros_bombo:
        numero = random.choice(numeros_bombo)
        numeros_bombo.remove(numero)
        print(f"Ha salido el número: {numero}\n")
        return numero
    else:
        print("No quedan más números en el bombo.")
        return None
    
def numero_en_linea(numero, cartones):
    linea1 = cartones[:5]
    linea2 = cartones[5:10]
    linea3 = cartones[10:15]
    
    print(linea1, linea2, linea3)

def juego():
    print("""\t!!BIENVENIDOS AL BINGO CICLISTA!!\n
          - Juego de 2 a 4 jugadores
          - Dos diferentes premios, línea y bingo.
          """)
    num_jugadores = int(input("Indique el número de jugadores: "))
    while (num_jugadores) < 2 or (num_jugadores > 4):
        print("Número de jugadores incorrectos, vuelva a intentarlo.")
        num_jugadores = int(input("Indique el número de jugadores: "))
        
    
    nombre_jugadores = []
    for i in range(num_jugadores):
        nombre = input(f"Indique el nombre del jugador {i+1}: ")
        nombre_jugadores.append(nombre)
    
    print(f"\nBienvenidos!!{nombre_jugadores}\nEstos son vuestros cartones para esta partida: ")
        
    partida = []
    aciertos = [0] * num_jugadores
    aciertos_jugador = [0] * num_jugadores
    
    
    for i in range(num_jugadores):
        print(f"\n{nombre_jugadores[i]}")
        carton = generar_carton()
        mostar_carton(carton)
        partida.append(carton)
    
    juego_terminado = False
    linea = 1
    numeros_bombo = list(range(1,91))
    
    while not juego_terminado:
        otro_numero = input("Pulsa intro para sacar un número.\n")
        numero = sacar_numero(numeros_bombo)
 
        for i in range(num_jugadores):
            numero_en_linea(numero, partida[i])
            
            """if numero_en_linea(numero, partida[i]):
                aciertos[i] += 1
                aciertos_jugador[i] += 1
                if aciertos[i] == 5 and linea != 0:
                    print(f"¡{nombre_jugadores[i]} ha completado una línea válida!")
                    linea = 0

            if aciertos[i] == 15:
                print(f"¡{nombre_jugadores[i]} ha completado su cartón! ¡Bingo!")
                juego_terminado = True
                break
        
        for i in range(num_jugadores):
            print(f"{nombre_jugadores[i]} lleva {aciertos_jugador[i]} aciertos.")"""
          
       
    
juego()


