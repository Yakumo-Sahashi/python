class ManejoArchivos:
    #metodo constructor
    def __init__(self,nombre):
        self.nombre = nombre
        
    def __enter__(self):
        #mensaje de aviso de apertura de archivo
        print("Obtenemos el recurso".center(50,'-'))
        #apertura del archivo
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        #se retorna el contenido del archivo
        return self.nombre
    #recibe los datos relacionados a un posible error
    def __exit__(self,tipo_excepcion,valor_excepcion,traza_error):
        #mensaje de cierre de archivo
        print("Cerramos el recurso".center(50,'-'))
        #valida si el archivo se encuentra abierto aun
        if self.nombre:
            #en caso de estar abierto lo cierra
            self.nombre.close()