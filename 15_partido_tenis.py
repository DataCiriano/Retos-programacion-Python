"""
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos. 
 """
 
 #Enumerados: es una forma de definir variables que solo pueden tomar ceirtos valores predefinidos, es como definir constantes
"""En este caso los puntos solo puden ser del jugador 1 (P1) o del jugador 2 (P2), por eso usamos la bibiloteca enum y forzamos que la variable
 points tenga solo estos dos valores posibles"""
 
from enum import Enum
 
class Player(Enum): #La clase creada debe heredar de Enum
    P1 = 1 #Como Enum se emplea para crear constantes es un buena práctiva escribirlas con mayúsculas
    P2 = 2
 
 
def tennis_game(points: list): #se pome el :list para indicar que el parámetro points debe ser de tipo lista

    game = ["Love", "15", "30", "40"]
    p1_points = 0
    p2_points = 0
    finished = False #booleano para controlar si el juego ha acabado (un jugador a ganado) y siguen entrando más datos, arroje un error
    error = False
    
    for player in points:
        
        error = finished #Como el for funciona para todos los puntos del array necesitamos igualar el error al finished 
        #Asi cuando el juego haya acabado y haya mas datos en el array de entrada marcará que los puntos no son correctos
        
        if player == Player.P1:
            p1_points +=1
        elif player == Player.P2:
            p2_points += 1
            
        if p1_points >= 3 and p2_points >= 3: #Aqui ya entra la parte de Deuce o Advance
            
            if not finished and abs(p1_points - p2_points) <= 1: 
                #Se pone el not finished para bligar a que si n ha acabado el partido se sigan metiendo lso datos y mostrando las ventajas
                #Se pone el abs para que se tome el valor absoluto, si p2_p0ints fuera mayor que p1_points darái erros
                #También se podríahacer poniendo: or (p2_points - p1_points) <= 1 asi se contemplan las dos opciones
                
                if p1_points == p2_points:
                    print("Deuce")
                elif  p1_points > p2_points:
                    print("Advance P1")
                else:
                    print("Advance P2")
            else:
                finished = True #marcamos que si no se dan las condiciones del if el juego debe acabar ya que un jugador habrá ganado
                
        else:
            if p1_points < 4 or p2_points < 4:
                print(f"{game[p1_points]} -- {game[p2_points]}")
            else:
                finished = True
    
    if error:
        print("Los puntos jugados no son correctos")
    else:
        if p1_points > p2_points:
            print("Ha ganado el Jugador 1")
        else:
            print("Ha ganado el jugador 2")
     
     
     
     
tennis_game([Player.P1, Player.P1, Player.P2, Player.P2, Player.P1, Player.P2, Player.P1, Player.P1])