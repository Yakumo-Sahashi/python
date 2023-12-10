from logger_base import log
#import mysql.connector as db
from mysql.connector import pooling
#from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'test'
    _USERNAME = 'root'
    _PASSWORD = ''
    _DB_PORT = '3306'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None   
    _config = {'user':_USERNAME,'password':_PASSWORD,'host':_HOST,'port':_DB_PORT,'database':_DATABASE,'raise_on_warnings':True}
    
    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pooling.MySQLConnectionPool(pool_name="mypool",pool_size=cls._MAX_CON,**cls._config)
                """ cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                                                    host=cls._HOST,
                                                    user=cls._USERNAME,
                                                    password=cls._PASSWORD,
                                                    port=cls._DB_PORT,
                                                    database=cls._DATABASE) """
                log.debug(f"Creacion de pool exitosa: {cls._pool}")
                return cls._pool
            except Exception as e:
                log.debug(f"Error al obtener el pool: {e}")
                sys.exit()
        else: 
            return cls._pool
    
    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().get_connection()
        log.debug(f"conexion obtenida del pool: {conexion}")
        return conexion
    
    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()
        log.debug(f"Regresamos la conexion al pool: {conexion}")
        
    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().close()
        log.debug(f"conexiones cerradas")        
        
           
        

if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion()
    conexion2 = Conexion.obtener_conexion()
    conexion3 = Conexion.obtener_conexion()
    conexion4 = Conexion.obtener_conexion()
    conexion5 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion5)
    conexion6 = Conexion.obtener_conexion()