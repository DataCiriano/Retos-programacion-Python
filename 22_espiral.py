"""
Crea una función que dibuje una espiral como la del ejemplo.
    - Únicamente se indica de forma dinámica el tamaño del lado.
    - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚

    Ejemplo espiral de lado 5 (5 filas y 5 columnas):
                     ════╗
                     ╔══╗║
                     ║╔╗║║
                     ║╚═╝║
                     ╚═══╝
"""
def draw_spiral(size):

    for row in range(0, size):
        spiral = ""
        horizontal = row == 0
        for col in range(0, size):
            if row + col == size - 1:
                spiral += "╗" if col >= row else "╚"
                horizontal = col < row
            elif row - col == 1 and row < (size / 2):
                spiral += "╔"
                horizontal = True
            elif row == col and row >= (size / 2):
                spiral += "╝"
                horizontal = False
            else: 
                spiral += "═" if horizontal else "║"
        
        print(spiral)


draw_spiral(0)
draw_spiral(1)
draw_spiral(2)
draw_spiral(3)
draw_spiral(5)
draw_spiral(20)
draw_spiral(50)