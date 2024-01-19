"""
Crea un programa que analice texto y obtenga:
 - Número total de palabras.
 - Longitud media de las palabras.
 - Número de oraciones del texto (cada vez que aparecen un punto).
 - Encuentre la palabra más larga.
 
Todo esto utilizando un único bucle.
"""
import nltk
import re

def text_analyzer(text):
    
    total_sentences = 0
    total_words = 0
    average_len_words = 0
    
    sentences = nltk.sent_tokenize(re.sub(r'[\n]', " ",text)) #obtenemos las frases sin tener en cuenta los saltos de línea
    total_sentences = len(sentences)
    
    words = nltk.word_tokenize(re.sub(r'[.,]', '', text)) #obtenemos las palabras sin tener en cuenta los puntos y las comas
    total_words = len(words)
    
    for word in words: 
        average_len_words += len(word) #sumamos la longitud de todas las pabras 
    
    average_len_words = average_len_words / total_words
    
    longest_word = max(words, key=len)
    
    print(f"El número total de frases en el texto es: {total_sentences}")
    print(f"El número total de palabras en el texto es: {total_words}")
    print(f"La longitud media de las palabras el texto es: {average_len_words}")
    print(f"La palabra más larga del texto es: {longest_word}")
    
   

text = """
Nos encontramos en un
periodo de guerra civil. Las
naves espaciales rebeldes,
atacando desde una base
oculta, han logrado su 
primera victoria contra
el malvado Imperio
Galáctico.

Durante la batalla, los 
espías rebeldes han
conseguido apoderarse de 
los planos secretos del
arma total y definitiva del
Imperio, la ESTRELLA
DE LA MUERTE,
una estación espacial
acorazada, llevando en sí
potencia suficiente para
destruir a un planeta
entero.

Perseguida por los 
siniestros agentes del 
Imperio, la Princesa Leia 
vuela hacia su patria, a
bordo de su nave espacial,
llevando consigo los
planos robados, que
pueden salvar a su pueblo
y devolver la libertad a la
galaxia....
"""

text_analyzer(text)
            