import mysql.connector

config = {
    'user':'root','password':'','host':'localhost','port':"3306",'database':'test','raise_on_warnings':True
}
conexion = mysql.connector.connect(**config) 

try:
    #al usar with si falla algun movimiento se genera un rollback o se guardan los cambios
    with conexion:
        with conexion.cursor() as cursor:
            """ sentencia = 'SELECT * FROM t_persona WHERE id_persona = %s'
            id_persona = input('Proporciona un valor de ID: ')
            cursor.execute(sentencia,(id_persona,))
            registros = cursor.fetchone()
            print(f"conexion con mysql: {registros}") """
            sentencia = 'INSERT INTO t_persona(nombre,apellido,email) VALUES(%s,%s,%s)'
            valores = ('issei','yagami','sahashi')           
            cursor.execute(sentencia,valores)
            #modifica o insertar varios registros #cursor.executemany(sentencia,valores)
            conexion.commit() #| se usa en caso no usar with
            #cursor.lastrowid se usa para recuperar el id del dato insertado
            registros_insertados = cursor.rowcount
            print(f"registros insertados: {registros_insertados}")
except Exception as e:
    print(f"Error en la conexion: {e}")
finally:
    conexion.close()