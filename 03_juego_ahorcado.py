

import random

class JuegoAhorcado:
    def __init__(self):
        self.palabras = []
        self.palabra_aleatoria = None
        self.intentos = None
        self.intento = 0
        self.palabra_adivinada = None

    def introduccion(self):
        print("BIENVENIDO AL JUEGO DEL AHORCADO\n--------------------------------\n")
        print("Se seleccionará una palabra aleatoria de una lista y dispondrás de 5 intentos para adivinarla. ¡¡¡Buena suerte!!! ")

    def obtener_palabra(self):
        with open("Retos_programacion\\palabras_ahorcado.txt", "r", encoding="UTF-8") as archivo:
            self.palabras = [linea.strip() for linea in archivo]

        self.palabra_aleatoria = random.choice(self.palabras)
        self.palabra_adivinada = "_" * len(self.palabra_aleatoria)

        print(f"La palabra que debes adivinar tiene: {len(self.palabra_aleatoria)} caracteres")
        
    def numero_intentos(self):
        self.intentos = 3 * len(self.palabra_aleatoria)
        print(f"Tiene {self.intentos} intentos para adivinar la palabra")

    def intentar(self):
        while self.intento < self.intentos:
            letra = input("Introduce una letra: ")

            if letra in self.palabra_aleatoria:
                print("¡Letra correcta!")
                # Actualizar la palabra parcialmente adivinada
                nueva_palabra_adivinada = ""
                for i in range(len(self.palabra_aleatoria)):
                    if self.palabra_aleatoria[i] == letra:
                        nueva_palabra_adivinada += letra
                    else:
                        nueva_palabra_adivinada += self.palabra_adivinada[i]
                self.palabra_adivinada = nueva_palabra_adivinada
            else:
                print("Letra incorrecta")

            print("Palabra parcialmente adivinada:", self.palabra_adivinada)

            self.intento += 1
            print("Intento", self.intento, "de", self.intentos)
            
            if self.palabra_adivinada == self.palabra_aleatoria:
                print("¡¡¡Felicidades conseguiste adivinar la palabra!!!")
                break
            
        if self.palabra_adivinada != self.palabra_aleatoria:
            print(f"Fin del juego, la palabra era: {self.palabra_aleatoria}")

    def iniciar_juego(self):
        self.introduccion()
        self.obtener_palabra()
        self.numero_intentos()
        self.intentar()

# Uso del juego
juego = JuegoAhorcado()
juego.iniciar_juego()