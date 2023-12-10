from logger_base import log
import mysql.connector as db
import sys

class Conexion:
    _DATABASE = 'test'
    _USERNAME = 'root'
    _PASSWORD = ''
    _DB_PORT = '3306'
    _HOST = 'localhost'
    _conexion = None
    _cursor = None    
    _config = {'user':_USERNAME,'password':_PASSWORD,'host':_HOST,'port':_DB_PORT,'database':_DATABASE,'raise_on_warnings':True}
    
    @classmethod
    def obtener_conexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = db.connect(**cls._config) 
                log.debug(f"Conexion exitosa: {cls._conexion}")
                return cls._conexion
            except Exception as e:
                log.debug(f"Ocurrio una excepcion al obtener la conexion: {e}")
                sys.exit()#terminamos todo el programa si no se puede conectar a la db
        else:
            return cls._conexion
        
    @classmethod
    def obtener_cursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtener_conexion().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener el cursor: {e}')
                sys.exit()
        else:
            log.debug(f'El cursor esta abierto actualmente: {cls._cursor}')
            return cls._cursor
         
    @classmethod
    def conexion_final(cls):
        cls._cursor = None if cls._cursor is None else cls._cursor.close()      
        cls._conexion = None if cls._conexion is None else cls._conexion.close()  
        log.debug(f'Conexion cerrada: {cls._cursor} {cls._conexion}')
               
        

if __name__ == '__main__':
    Conexion.obtener_conexion()
    Conexion.obtener_cursor()