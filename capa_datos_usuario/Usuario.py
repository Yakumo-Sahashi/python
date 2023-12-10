from logger_base import log

class Usuario:
    
    def __init__(self,id_usuario=None,usuario=None,password=None):
        self._id_usuario = id_usuario
        self._usuario = usuario
        self._password = password
        
    def __str__(self):
        return f"ID usuario: {self._id_usuario}, usuario: {self._usuario}, pass: {self._password}"

    @property
    def id_usuario(self):
        return self._id_usuario
    
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario    
    
    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self.password = password
        
if __name__ == '__main__':
    usuario1 = Usuario(1,'yakumo','1234')
    log.debug(usuario1)
    #simular un insert
    usuario1 = Usuario(usuario='issei',password='jpe')
    log.debug(usuario1)
    #simular delete
    usuario1 = Usuario(id_usuario=1)
    log.debug(usuario1) 