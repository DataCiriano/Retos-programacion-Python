#Reto de programación ára "dibujar una escalera"

"""
    Crea una función que dibuje una escalera según su número de escalones.
    - Si el número es positivo, será ascendente de izquiera a derecha.
    - Si el número es negativo, será descendente de izquiera a derecha.
    - Si el número es cero, se dibujarán dos guiones bajos (__).

    Ejemplo: 4 escalones
            _
          _|       
        _|
      _|
    _|

"""

def dibujar_escalera(steps: int):

    if steps > 0: #escalera subida
        for step in range(steps + 1):
            spaces = "  " * (steps - step) #en cada escalón debemos dejar 2 espacios
            solo_peldaño = "_" if step == 0 else "_|"
            print(f"{spaces}{solo_peldaño}")

    elif steps < 0:
        for step in range(abs(steps) + 1): #abs nos da el valor absoluto
            spaces = " " * ((step * 2) - 1) 
            solo_peldaño = "_" if step == 0 else "|_"
            print(f"{spaces}{solo_peldaño}")

    else:
        print("__")


dibujar_escalera(10)

dibujar_escalera(-4)