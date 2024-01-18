#Programa que determine los años bisiestos desde el año 0 d.c. hast un año dado
#Ademas que determine el siguiente año bisiesto mas cercano al año dado

def bisiestos():
    
    num = int(input("Introduzca un año: "))
    lista = []
    
    for i in range(4,num+1,4):
        if i%100 == 0:
            if i%400 == 0:
                lista.append(i)
        elif i%4 == 0:
                lista.append(i)
    
    print(f"La lista de años bisiestos hasta el introducido es: {lista}")
                    

bisiestos()