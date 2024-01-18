"""
Crea un programa que simule el comportamiento del sombrero selccionador del universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
"""

def sombrero_selecionador():
    
    griffindor = 0
    slythering = 0
    hufflepuff = 0
    ravenclaw = 0
    
    print("¡¡¡BIENVENIDO JÓVEN ESTUDIANTE!!!\n")
    nombre = input("¿Cúal es tu nombre? ")
    print(f"\nNo se para que te pregunto si ya lo se.\nTe llamas {nombre} ¿No es cierto?\n")
    print("Vamos a ver que hago contigo. ¿En que casa debería ponerte?\n")
    print("Necesito conocerte mejor así que voy a hacerte unas cuantas preguntas, piensa la respuesta que mas te guste\n")
    
    print("**PRIMERA PREGUNTA**\n")   
    pregunta1 = input("""Te encuentras jugando una aprtida de ajedrez mágico donde tanto tu como tus amigos sois varias piezas. ¿Cómo decides enfrentarlo?\n
        a) Trazas un plan audaz y valiente para ganar la partida sin importar si sales herido.\n
        b) Empleas tu astucia e inteligencia para estudiar las jugadas e ir un paso por delante del oponente.\n
        c) Dicutes las jugadas en equipo y apoyas a tus compañeros para lograr una victoria conjunta.\n
        d) Analizas cuidadosamente todas las opciones para tomar la decisiones basándote en la lógica y el razonamiento.\n""")
    
    while pregunta1 not in ["a","b","c","d"]:
        pregunta1 = (input("Esa no puede ser tu respuesta, piénsalo un poco y responde una de las opciones que te doy\n"))
        
    print("**SEGUNDA PREGUNTA**\n")    
    pregunta2 = input("""Tienes la oportunidad de liderar al equipo de quidditch de tu casa. ¿Cuál es tu enfoque?\n
        a) Motivas y animas a tus compañeros, infundiendo entusiasmo y positividad en el equipo aunque los resultados no sean lso mejores.\n
        b) Utilizas tu astucia y perspicacia para identificar las fortalezas de cada miembro del equipo y asignarles roles adecuados aunque no 
        todo el munso esté de acuerdo.\n
        c) Te Aseguras de que todos tengan voz y voto en el proyecto, promoviendo la justicia y la igualdad de oportunidades.\n
        d) Realizar investigaciones exhaustivas sobre los rivales para trazar la estrategia mas óptima de jeugo.\n""")
    
    while pregunta2 not in ["a","b","c","d"]:
        pregunta2 = (input("Esa no puede ser tu respuesta, piénsalo un poco y responde una de las opciones que te doy\n"))
    
    print("**TERCERA PREGUNTA**\n")   
    pregunta3 = input("""¿Qué cualidad valoras más en un amigo?\n
        a) La valentía y el coraje para enfrentar los desafíos de la vida juntos.\n
        b) La inteligencia y ambición para que sea una persona exitosa igual que tú.\n
        c) La lealtad y la amabilidad para estar presente y apoyarte en los buenos y malos momentos.\n
        d) La capacidad resolutiva y la curiosidad para explorar nuevas ideas y aprender juntos.\n""")
    
    while pregunta3 not in ["a","b","c","d"]:
        pregunta3 = (input("Esa no puede ser tu respuesta, piénsalo un poco y responde una de las opciones que te doy\n"))
        
    print("**CUARTA PREGUNTA**\n")      
    pregunta4 = input("""¿Qué tipo de actividad te apasiona más en tu tiempo libre?\n
        a) Participar en deportes o actividades físicas que requieran coraje y determinación como el quidditch.\n
        b) Resolver enigmas como dónde se encuentra la cámara de los Secretos.\n
        c) Contribuir al bienestar de la comunidad a través de actividades voluntarias como la preocupación por los elfos domésticos del 
        castillo.\n
        d) Explorar y aprender sobre diferentes temas en la sección prohibida de la biblioteca.\n""")
    
    while pregunta4 not in ["a","b","c","d"]:
        pregunta4 = (input("Esa no puede ser tu respuesta, piénsalo un poco y responde una de las opciones que te doy\n"))
        
    print("**QUINTA PREGUNTA**\n")   
    pregunta5 = input("""Te ves envuelto en una disputa con otro estudiante en Hogwarts debido a una diferencia de opiniones sobre la mejor 
        manera de proteger a los seres mágicos en el Bosque Prohibido. ¿Cuál es tu enfoque para resolver esta disputa?\n
        a) Defiendes tus principios con valentía y positividad, argumentando que la coexistencia pacífica es posible.\n
        b) Utilizas tu astucia e inteligencia para presentar un plan estratégico que proteja a los seres mágicos y minimice los riesgos\n 
        c) Buscas la empatía y el diálogo, tratando de entender las preocupaciones de la otra persona y encontrando un compromiso justo para.\n
        d) Realizas una investigación exhaustiva sobre los seres mágicos del bosque y sus necesidades, y presentas argumentos basados en el 
        conocimiento y la sabiduría.\n""")
    
    while pregunta5 not in ["a","b","c","d"]:
        pregunta5 = (input("Esa no puede ser tu respuesta, piénsalo un poco y responde una de las opciones que te doy\n"))
    
    if pregunta1 == "a":
        griffindor += 1
    elif pregunta1 == "b":
        slythering += 1
    elif pregunta1 == "c":
        hufflepuff += 1
    elif pregunta1 == "d":
        ravenclaw += 1
        
    if pregunta2 == "a":
        griffindor += 1
    elif pregunta2 == "b":
        slythering += 1
    elif pregunta2 == "c":
        hufflepuff += 1
    elif pregunta2 == "d":
        ravenclaw += 1
        
    if pregunta3 == "a":
        griffindor += 1
    elif pregunta3 == "b":
        slythering += 1
    elif pregunta3 == "c":
        hufflepuff += 1
    elif pregunta3 == "d":
        ravenclaw += 1
        
    if pregunta4 == "a":
        griffindor += 1
    elif pregunta4 == "b":
        slythering += 1
    elif pregunta4 == "c":
        hufflepuff += 1
    elif pregunta4 == "d":
        ravenclaw += 1
        
    if pregunta5 == "a":
        griffindor += 1
    elif pregunta5 == "b":
        slythering += 1
    elif pregunta5 == "c":
        hufflepuff += 1
    elif pregunta5 == "d":
        ravenclaw += 1
    
    print("**PORCENTAJES DE COMPATIBILIDAD**")
    print("_________________________________")
    print(f"Griffindor: {griffindor/5*100}%\nSlythering: {slythering/5*100}%\nHufflepuff: {hufflepuff/5*100}%\nRavenclaw: {ravenclaw/5*100}%\n")
    
    max_compatibilidad = max(griffindor,slythering,hufflepuff,ravenclaw)
    
    if max_compatibilidad == griffindor:
        print(f"{nombre} ¡¡¡Has demostrado ser un buen estudiante para Griffindor!!!")
    elif max_compatibilidad == slythering:
        print(f"{nombre} ¡¡¡Tu astucia e inteligencia te convierten en un perfecto Slythring!!!")
    elif max_compatibilidad == hufflepuff:
        print(f"{nombre} ¡¡¡En Hufflepuff encajarás perfectamente!!!")
    else:
        print(f"{nombre} ¡¡¡Ravenclaw es el lugar perfecto para saciar tu curiosidad de conocimiento!!!")


        
sombrero_selecionador()