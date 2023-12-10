#conector a base de datos
import psycopg2

#conexion a db
conexion = psycopg2.connect(user='postgres',password='root',host='localhost',port="5432",database='test_db')

#print(conexion)

#creacion de un objeto de tipo cursor
cursor = conexion.cursor()

#query de consulta
sentencia = 'SELECT * FROM t_persona'
#ejecucion de consulta
cursor.execute(sentencia)
#asociacion de la consulta
registros = cursor.fetchall()

#cierre del objeto cursor
cursor.close()
#cierre de la conexion
conexion.close()

print(registros)

for persona in registros:
    print(persona)