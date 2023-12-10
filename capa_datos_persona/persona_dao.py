from Conexion import Conexion
from Persona import Persona
from logger_base import log

class PersonaDAO:
    
    '''
    DAO (Data Access Object)
    CRUD (Create Read Update Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM t_persona'
    _INSERTAR = 'INSERT INTO t_persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE t_persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM t_persona WHERE id_persona = %s'
    
    
    @classmethod
    def seleccionar(cls):
        Conexion.conexion_final()
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0],registro[1],registro[2],registro[3])
                    personas.append(persona)
                return personas
        
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:   
                valores = (persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._INSERTAR,valores)
                Conexion.obtener_conexion().commit()
                return cursor.rowcount   
            
    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:   
                valores = (persona.nombre,persona.apellido,persona.email,persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                Conexion.obtener_conexion().commit()
                return cursor.rowcount          
    @classmethod
    def eliminar(cls, persona):
        Conexion.conexion_final()
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:   
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR,valores)
                Conexion.obtener_conexion().commit()
                return cursor.rowcount          
        
if __name__ == '__main__':
    #insertar registro
    """ persona1 = Persona(nombre='sakura',apellido='uchiha',email='sakura@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f"Personas insertadas: {personas_insertadas}") """
    #update 
    """ persona1 = Persona(61,'Sasuke','Uchiha','sasuke@mail.com.mx')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f"Personas actualizadas: {personas_actualizadas}") """
    #delete 
    persona1 = Persona(id_persona=63)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f"Personas eliminadas: {personas_eliminadas}")
    #seleccionar registros
    personas = PersonaDAO.seleccionar() 
    for persona in personas:
        log.debug(persona)