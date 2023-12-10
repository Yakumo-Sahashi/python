from logger_base import log
from Usuario import Usuario
from UsuarioDAO import UsuarioDAO
opcion = None

while opcion != 5:
    try:
        print('Opciones'.center(50,'-'))
        print('1. Lista de usuarios')
        print('2. Agregar usuario')
        print('3. Actualizar usuario')
        print('4. Eliminar usuario')
        print('5. Salir')
        opcion = int(input('Escribe tu ipcion (1-5): '))
        
        if opcion == 1:
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios:
                log.debug(usuario)  
        elif opcion == 2:
            nombre_usuario = input('Proporciona el nombre de usuario: ')
            password = input('Proporciona el password: ')
            usuario = Usuario(usuario=nombre_usuario,password=password)
            usuarios_insertados = UsuarioDAO.insertar(usuario)
            log.debug(f"Usuarios insertados: {usuarios_insertados}")
        elif opcion == 3:
            id_usuario = int(input('ID de usuario a actualizar: '))
            nombre_usuario = input('Proporciona el nombre de usuario: ')
            password = input('Proporciona el password: ')
            usuario = Usuario(id_usuario,nombre_usuario,password)
            usuarios_actualizados = UsuarioDAO.actualizar(usuario)
            log.debug(f"Usuarios actualizados: {usuarios_actualizados}") 
        elif opcion == 4:
            id_usuario = int(input('ID de usuario a eliminar: '))
            usuario = Usuario(id_usuario=id_usuario)
            usuarios_eliminados = UsuarioDAO.eliminar(usuario)
            log.debug(f"Usuarios eliminadas: {usuarios_eliminados}") 
            
    except Exception as e:
        log.error(f"Se ha producido un error: {e}")
        opcion = None
else:
    log.debug("programa finalizado".center(50,'-'))