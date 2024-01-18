

#PROGRAMA QUE PIDE AL USUARIO QUE TIPO DE ÁREA DESEA CALCULAR, LE PIDE LOS DATOS PARA ELLO Y LE DEVUELVE EL RESULTADO

import math

class Figuras:
    def __init__(self):
        self.opciones = {
            "1": self.calcular_circulo,
            "2": self.calcular_rombo,
            "3": self.calcular_triangulo,
            "4": self.calcular_rectangulo,
            "5": self.salir
        }
        
    def mostrar_menu(self):
        print("### CALCULADORA DE FIGURAS ###")
        print("Opción 1: Calcular área de un círculo dado el radio")
        print("Opción 2: Calcular área de un rombo dadas sus diagonales")
        print("Opción 3: Calcular área de un triángulo dadas su base y su altura")
        print("Opción 4: Calcular área de un rectángulo dadas su base y su altura")
        print("Opción 5: Salir")
        
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese la opción deseada del 1 al 5 para obtener su cálculo de área: ")
            
            if opcion in self.opciones:
                self.opciones[opcion]()
            else:
                print("Opción inválida. Por favor seleccione una opción válida.")
                
    def calcular_circulo(self):
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            area = math.pi * (radio ** 2)
            print("El área del círculo es:", area)
        except ValueError:
            print("Valor inválido. Asegúrese de ingresar un número válido para el radio.")

    def calcular_rombo(self):
        try:
            diagonal_mayor = float(input("Ingrese la longitud de la diagonal mayor del rombo: "))
            diagonal_menor = float(input("Ingrese la longitud de la diagonal menor del rombo: "))
            area = (diagonal_mayor * diagonal_menor) / 2
            print("El área del rombo es:", area)
        except ValueError:
            print("Valor inválido. Asegúrese de ingresar números válidos para las diagonales.")

    def calcular_triangulo(self):
        try:
            base = float(input("Ingrese la longitud de la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = (base * altura) / 2
            print("El área del triángulo es:", area)
        except ValueError:
            print("Valor inválido. Asegúrese de ingresar números válidos para la base y la altura.")

    def calcular_rectangulo(self):
        try:
            base = float(input("Ingrese la longitud de la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = base * altura
            print("El área del rectángulo es:", area)
        except ValueError:
            print("Valor inválido. Asegúrese de ingresar números válidos para la base y la altura.")

    def salir(self):
        print("¡Hasta luego!")
        exit()

# Crear instancia de la clase CalculadoraFiguras y ejecutar el programa
calculadora = Figuras()
calculadora.ejecutar()









