"""
Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente base de datos MySQL:
    - Host: mysql-5707.dinaserver.com
    - Port: 3306
    - User: mouredev_read
    - Password: mouredev_pass
    - Database: moure_test

 Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
    - SELECT * FROM `challenges`

 Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
"""

import mysql.connector

config = {
    "host": "mysql-5707.dinaserver.com",
    "port": "3306",
    "user": "mouredev_read",
    "password": "mouredev_pass",
    "database": "moure_test"
}

connection = mysql.connector.connect(**config) #Se ponen ** para desempaquetar el diccionario 
cursor = connection.cursor()

query = "SELECT * FROM challenges" #Queremos todo (*) de la tabla "challenges"

cursor.execute(query) #Ejecutamos la consulta

result = cursor.fetchall() #Obtenemos los resultados de la consulta

for row in result: #Mostramos los resultados con el bucle for línea a línea 
    print(row)

cursor.close() #Cerramos el cursor y la conexión para liberar los recursos
connection.close()

"""
Sin desempaquetar el diccionario, la conexión podría hacerse pasando los datos de la base de datos ditectamente como agumento de la función 
connnect asi:

connection = mysql.connector.connect(
    host= "mysql-5707.dinaserver.com",
    port = "3306",
    user = "mouredev_read",
    password = "mouredev_pass",
    database = "moure_test"
)
"""