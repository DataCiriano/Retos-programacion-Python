
#Crea una función que sea capaz de encriptar y desencriptar texto utilizando el algoritmo de encriptación de Karaca 

"""Encriptación de Karaka:
        -Primero debemos invertir la palabra introducida
        -Reemplazar las vocales según: a-->0, e-->1, i-->2, o-->3, u-->4
        -Añadir al final de la palabra "aca"
        -La función debe codificar y decodificar el texto introducido
        -Cualquier dato que le pasemos que no sea texto debe devolver un error o el dato orginal inválido
        -La cadena suminstrada puede contener espacios (habrá que limpiarla)
        -Para saber si la cadena proporcionada debe ser decodificada debe terminar en "aca" y tener al menos un número entre 0 y 4 
"""

def karaka(texto):
    
    texto = texto.lower() #ponemos el texto en minúsculas
    
    if texto.endswith("aca") and any(caracter.isdigit() for caracter in texto):
        
        texto = texto[:-3] #eliminamos el "aca" de final
        texto = texto[::-1] #invertimos el texto
        
        #Reemplazar los números por las vocales
        texto = texto.replace("0","a")
        texto = texto.replace("1","e")
        texto = texto.replace("2","i")
        texto = texto.replace("3","o")
        texto = texto.replace("4","u")
            
        return f"El texto decodificado es: {texto}"
        
    else:
        
        texto = texto.replace(" ","") #eliminamos los espacios del texto
        
        #Reemplazar las vocales por números
        texto = texto.replace("a","0")
        texto = texto.replace("e","1")
        texto = texto.replace("i","2")
        texto = texto.replace("o","3")
        texto= texto.replace("u","4")
        
        texto= texto[::-1] + "aca" #invertimos el texto y añadimos "aca" al final
                 
        return f"El texto codificado es: {texto}"

texto = input("Introduzca el texto que desea codificar/decodificar: ")
print(karaka(texto))