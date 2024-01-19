"""
***LA CASA ENCANTADA***
Este es un reto especial por Halloween.

Te encuentras explorando una mansión abandonada llena de habitaciones.
En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
Tu misión es encontrar la habitación de los dulces.

Se trata de implementar un juego interactivo de preguntas y respuestas por terminal. (Tienes total libertad para ser creativo con los textos).

🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4 que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
(16 habitaciones, siendo una de entrada y otra donde están los dulces)
Esta podría ser una representación:
    🚪⬜️⬜️⬜️
    ⬜️👻⬜️⬜️
    ⬜️⬜️⬜️👻
    ⬜️⬜️🍭⬜️
❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto. Si no lo aciertas no podrás desplazarte.
🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte. (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse 
las opciones posibles).
🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y tengas que responder dos preguntas para salir de ella.
"""

"""
    PASOS DE RESOLUCIÓN
    
    1- Generar casa de 4x4
    2- Crear la puerta de la casa de forma aleatoria
    
"""
import random #importamos este módulo para generar un n° aleatorio 

def create_house() -> (list, list):
    
    house = [list(["⬜️"] * 4) for _ in range(4)]
    
    if random.choice([True, False]):
        #Columnas perímetro
        door = [random.randint(0,3), random.choice([0,3])]
        #generamos un n° aleatorio del 0 al 3 para generar una fila random 
    else:
        door = [random.choice([0,3]), random.randint(0,3)]
    
    house[door[0]][door[1]] = "🚪"
    
    def generate_candy(door: list) -> list:
        candy = [random.randint(0,3), random.randint(0,3)]
        if candy[0] == door[0] and candy[1] == door[1]:
            return generate_candy(door)
        return candy
    
    candy = generate_candy(door)
    
    house[candy[0]][candy[1]] = "🍭"
    
    for row in house:
        print("".join(map(str, row)))
        
    return house, door


def move(position: list) -> list: #pasamos una lista con la posición inicial y devolvemos otra lista con la posición a la que se desplazó
    
    row, col = position[0], position[1]
    
    movements = "N S E O"
    
    if row == 0:
        movements = movements.replace("N ", "")
    if row == 3:
        movements = movements.replace("S ", "")
    if col == 0:
        movements = movements.replace("O ", "")
    if col == 3:
        movements = movements.replace("E ", "")
    
    movement = input(f"¿Hacia donde te quieres desplazar[{movements}]?: ").upper()
    
    if movement in movements:
        if movement == "N": 
            position = [row - 1, col]
        elif movement == "S": 
            position = [row + 1, col]
        elif movement == "E": 
            position = [row, col + 1]
        elif movement == "O": 
            position = [row, col - 1]
    
        return position
    else:
        print("Desplazamiento incorrecto. Selecciona una de las opciones válidas.")
        return move(position)

def riddle():
    
    riddles = [("¿Dónde está la Gran Muralla China?", "China"),
                ("¿Cuál es la capital de Canadá?", "Ottawa"),
                ("¿Dónde se encuentra el Cristo Redentor?", "Río de Janeiro, Brasil"),
                ("¿Cuál es la capital de Australia?", "Canberra"),
                ("¿En qué país está ubicada la Acrópolis de Atenas?", "Grecia"),
                ("¿Cuál es la capital de España?", "Madrid"),
                ("¿Dónde se encuentra el Coliseo Romano?", "Roma"),
                ("¿Cuál es la capital de Sudáfrica?", "Ciudad del Cabo"),
                ("¿En qué país se encuentra el Kilimanjaro?", "Tanzania"),
                ("¿Cuál es la capital de México?", "Ciudad de México"),
                ("¿Dónde se encuentra la Gran Pirámide de Giza?", "Egipto"),
                ("¿Cuál es la capital de Argentina?", "Buenos Aires"),
                ("¿En qué país se encuentra la Ópera de Sídney?", "Australia"),
                ("¿Cuál es la capital de Rusia?", "Moscú"),
                ("¿Dónde se encuentra la Estatua de la Libertad?", "Nueva York")
    ]
    
    current_riddle = riddles[random.randint(0, len(riddles)-1)]
    
    while True:
        answer = input(f"{current_riddle[0]}: ")
        
        if answer.lower() == current_riddle[1].lower():
            print("Respuesta correcta\n")
            return
        else:
            print("Respuesta incorrecta\n")
    
house, door = create_house()

position = door #así tengo en una variable la posición inicial del personaje
print(f"Posición Inicial: {position}")

print("""
      👻 BooooooOOOOoo!!
      Si quieres encontrar los dulces de la casa encantada 🏰
      tendrás que buscarlos por sus habitaciones
      Pero recuerda, no podrás moverte si antes no respondes 
      correctamente a su enigma
""")

while True:
    position = move(position)
    print((f"Posición: {position}"))

    house_room = house[position[0]][position[1]]

    if house_room == "⬜️":
        print("Responde correctamente a está pregunta para continuar avanzando: \n")
        riddle()
        
        ghost = random.randint(1,10) == 1
        if ghost:
            print("""👻 BooooooOOOOoo!! 
                  Para salir de esta habitación deberás responder una pregunta más""")
            riddle()

    elif house_room == "🍭":
        print("""
            👻 BooooooOOOOoo!!
            ¡Felicidaes, has encontrado los dulces 🍭
            y escapado de la casa!""")
        break