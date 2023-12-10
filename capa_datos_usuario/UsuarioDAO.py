from logger_base import log
from CursorPool import CursorPool
from Usuario import Usuario

class UsuarioDAO:
    
    _SELECCIONAR = 'SELECT * FROM t_usuario'
    _INSERTAR = 'INSERT INTO t_usuario(usuario,password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE t_usuario SET usuario=%s, password=%s WHERE id_usuario = %s'
    _ELIMINAR = 'DELETE FROM t_usuario WHERE id_usuario = %s'
    
    
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls, usuario):
        with CursorPool() as cursor:  
            valores = (usuario.usuario,usuario.password)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount   
            
    @classmethod
    def actualizar(cls, usuario):
        with CursorPool() as cursor:   
            valores = (usuario.usuario,usuario.password,usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount      
            
    @classmethod
    def eliminar(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount          
        
if __name__ == '__main__':
    #insert
    """ usuario1 = Usuario(usuario='yakumo',password='1234')
    usuarios_insertador = UsuarioDAO.insertar(usuario1)
    log.debug(f"Usuarios insertados: {usuarios_insertador}")  """
    #update 
    """ usuario1 = Usuario(2,'sasuke','Uchiha')
    usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
    log.debug(f"Usuarios actualizados: {usuarios_actualizados}") """
    #delete 
    """ usuario1 = Usuario(id_usuario=3)
    usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
    log.debug(f"Usuarios eliminadas: {usuarios_eliminados}") """
    #seleccionar registros
    usuarios = UsuarioDAO.seleccionar() 
    for usuario in usuarios:
        log.debug(usuario)