#Mostrar cuantos granso de maiz habría en cada uno de los 64 cuadrados de un tablero de ajedrez si se doblan con respecto al anterior

def granos_maiz():
    
    lista= [1]
    
    for i in range(64):
        lista.append(2*lista[-1])
    return lista
    

print(granos_maiz())

#Lo mismo pero en una línea con una función lambda
granos_maiz_lambda = lambda n: [2**i for i in range(n)]
print(granos_maiz_lambda(64))