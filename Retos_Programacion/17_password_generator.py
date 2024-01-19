#Generados de contraseñas

"""
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 Podrás configurar generar contraseñas con los siguientes parámetros:
 Longitud: Entre 8 y 16.
    - Con o sin letras mayúsculas.
    - Con o sin números.
    - Con o sin símbolos.
 (Pudiendo combinar todos estos parámetros entre ellos)
"""
import random

def password_generator(length=8, capitals=False, numbers=False, symbols=False): #Damos valores predefinidos a los parámetros
    
    #Fuente: https://www.ascii-code.com/ (son los números de la primera columna DEC)
    #print(chr(48)) El 48 corresponde con el caracter 0
    
    caracteres = list(range(97,123))  #Recordemso que el range no incluye el falor final por eso si queremos el 122 ponemos 123
    password = ""
    
    if capitals:
        caracteres += list(range(65,91))
    if numbers:
        caracteres += list(range(49,58))
    if symbols:
        caracteres += list(range(33,48)) + list(range(58,65)) + list(range(91,97)) #concatemos listas con +
        
    
    if length < 8:
        final_length = 8
    elif length > 16:
        final_length = 16
    else:
        final_length = length
   
    while len(password) < final_length:
       password += chr(random.choice(caracteres)) 
       #chr() devuelve el caracter asociado al código ascii que le pasemos 
       
    return password
    

    
print(password_generator(4)) #Contraseña menor a 8 caracteres devuelve al menos 8
print(password_generator(34)) #Contraseña mayor de 16 caracter devuelve un máximo de 16
print(password_generator(12)) #Contraseña con una longitud ente 8-16 devuelve del valor deseado

print(password_generator(10,True)) #Contraseña con letras en mayúsculas

print(password_generator(12,True,True)) #Cntraseña con mayúsculas y números

print(password_generator(12,True,True,True)) #Contraseña con mayúsculas, números y símbolos



