
#Porgrama que permite al jugador tratar de adivinar un número aleatorio 

import random

class AdivinarNumeroAleatorio:
    
    def __init__(self):
        
        self.numero_aleatorio = None
        self.limite_numero = None
        self.num_usuario = None
        self.intentos = None
        self.intento = 0
        
    def obterner_aleatorio(self):
        while True:
            try:
                self.limite_numero = int(input("Introduzca el mayor número aleatorio posible: "))
                
                self.numero_aleatorio = random.randint(1, self.limite_numero)
                print(f"El número aleatorio generado es: {self.numero_aleatorio}")
                break
            except ValueError:
                print("No ha introducido unn número válido, vuelva a intentarlo.")
        
    def numero_intentos(self):
        
        if (self.limite_numero > 10):
            self.intentos = 20
            print(f"Dispone de {self.intentos} intentos.")
        else:
            self.intentos = 10
            print(f"Dispone de {self.intentos} intentos.")
            
        
    def dar_pistas(self):
        
        while self.intento <= self.intentos:
            while True:
                try:
                    self.num_usuario = int(input("Introduzca un número: "))
                    
                    if self.num_usuario < self.numero_aleatorio:
                        print(f"Número incorrecto, el número aleatorio es mayor. Te quedan {(self.intentos-1)-self.intento} intentos para acertar.")
                    elif self.num_usuario > self.numero_aleatorio:
                        print(f"Número incorrecto, el número aleatorio es menor. Te quedan {(self.intentos-1)-self.intento} intentos para acertar.")
                    else:
                        print("¡Felicidades has acertado, el número aleatorio es el mismo que introdujiste!")
                        break
                
                    self.intento += 1
                
                except ValueError:
                    print("No ha introducido unn número válido, vuelva a intentarlo.")
                
            
        print("Fin del juego.")
    
    def iniciar_juego(self):
        self.obterner_aleatorio()
        self.numero_intentos()
        self.dar_pistas()



juego = AdivinarNumeroAleatorio()
juego.iniciar_juego()