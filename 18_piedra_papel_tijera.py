"""
Crea un programa que calcule quien gana más partidas al piedra,
 papel, tijera, lagarto, spock.
 - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 - La función recibe un listado que contiene pares, representando cada jugada.
 - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 """"🦎"
def cachipun(secuence):
    puntosJ1 = 0
    puntosJ2 = 0
    
    for jugada in secuence:
        
        if jugada[0] != jugada[1]:

            if jugada[0]== "🗿" and (jugada[1] == "🦎" or jugada[1] == "✂️"  ):
                puntosJ1 += 1
            elif jugada[0] == "📄" and (jugada[1] == "🖖" or jugada[1] == "🗿" ):
                puntosJ1 += 1
            elif jugada[0] == "✂️" and (jugada[1] == "🦎" or jugada[1] == "📄" ):
                puntosJ1 += 1
            elif jugada[0] == "🦎" and (jugada[1] == "🖖" or jugada[1] == "📄" ):
                puntosJ1 += 1
            elif jugada[0] == "🖖" and (jugada[1] == "✂️" or jugada[1] == "🗿" ):
                puntosJ1 += 1
            else:
                puntosJ2 += 1
    
    if puntosJ1 > puntosJ2:
        print("¡¡¡¡Felicidades Jugador 1 eres el ganador!!!")
    elif puntosJ1 < puntosJ2:
        print("¡¡¡¡Felicidades Jugador 2 eres el ganador!!!")
    else:
        print("Parece que hay un empate entre el Jugador 1 y el Jugador 2")
    
 
 
secuence_tie= [("🗿","✂️"),("✂️","🗿"),("📄","✂️"),("🖖","✂️")]
cachipun(secuence_tie)

secuence_J1_win = [("🗿","✂️"),("✂️","🗿"),("🖖","✂️"),("🦎","📄")]
cachipun(secuence_J1_win)
     
secuence_J2_win = [("🗿","✂️"),("🖖","🗿"),("📄","✂️")]
cachipun(secuence_J2_win)

sec =[("🗿","🗿")] #Si los jugadores sacan el mismo resultado nadie gana
cachipun(sec)

#Otra forma de hacerlo es almacenar las regals del juego en un diccionario y comprbar lso resultados obtenidos con él para ver quien gana
     
