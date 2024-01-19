"""
    Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia) de un lugar ficticio al pasar un número concreto de días según estas reglas:
        - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
        - Cada día que pasa:
            - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
            - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día siguiente aumenta en un 20%.
            - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día siguiente disminuye en un 20%.
            - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
        - La función recibe el número de días de la predicción y muestra la temperatura y si llueve durante todos esos días.
        - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
"""
import random

def climate_simulator(days):
    temp_init = int(input("Indique la temperatura inicial en grados Celsius: "))
    rain_prob_init = int(input("Indique la probabilidad de lluvia inicial en porcentaje: "))

    print(f"Temperatura inicial: {temp_init}")
    print(f"Probabilidad de lluvia inicial: {rain_prob_init}")

    temp_max = temp_init
    temp_min = temp_init
    days_with_rain = 0

    for i in range(1, days + 1):
        temp_probability = random.randint(1, 10)

        if temp_probability == 1:
            temp_init += 2
        elif temp_probability == 2:
            temp_init -= 2

        if temp_init > 25:
            rain_prob_init += 20

        if rain_prob_init > 100:
            rain_prob_init = 100
        elif rain_prob_init < 0:
            rain_prob_init = 0

        if temp_init < 5:
            rain_prob_init -= 20

        if rain_prob_init == 100:
            temp_init -= 1
            days_with_rain += 1

        temp_max = max(temp_max, temp_init)
        temp_min = min(temp_min, temp_init)

        rain = rain_prob_init == 100

        print(f"Día {i}: Temperatura {temp_init} Probabilidad de lluvia {rain_prob_init}% ¿Llueve? {rain}")

    print(f"\nResumen del periodo de simulación:")
    print(f"Temperatura máxima: {temp_max}")
    print(f"Temperatura mínima: {temp_min}")
    print(f"Días con lluvia: {days_with_rain}")


climate_simulator(14)