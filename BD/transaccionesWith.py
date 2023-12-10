import mysql.connector as db

config = {'user':'root','password':'','host':'localhost','port':"3306",'database':'test','raise_on_warnings':True}
conexion = db.connect(**config) 

try:
    with conexion:
        with conexion.cursor() as cursor:
            print(f'{cursor}')
            sentencia = 'INSERT INTO t_persona(nombre,apellido,email) VALUES(%s,%s,%s)'
            valores = ('issei','yagami','sahashi')
            cursor.execute(sentencia,valores)
            conexion.commit()
except Exception as e:
    print(f"Error se hizo un rolback {e}")
finally:
    conexion.close()