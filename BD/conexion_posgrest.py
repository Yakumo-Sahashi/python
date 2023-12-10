import psycopg2
conexion = psycopg2.connect(user='postgres',password='root',host='localhost',port="5432",database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM t_persona WHERE id_persona = %s'
            id_persona = input('Proporciona un valor de ID: ')
            cursor.execute(sentencia,(id_persona,))
            registros = cursor.fetchone()#recupera un registro
            #registros = cursor.fetchall()#recupera una lista de registros
            print(registros)
except Exception as e:
    print(f"Error en la conexion: {e}")
finally:
    conexion.close()
    