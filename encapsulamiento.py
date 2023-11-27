#clases y objetos

class Persona:
    def __init__(self, nombre, apellido, edad):
        #self._nombre = nombre
        #atributo encapsulado /se usa para indicar que no se debe acceder a esta propiedad desde fue de la clase y tampoco moficar sus valores
        #self.__nombre = nombre /impide que el atributo sea mdoficado fuera de la clase
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    #decorador /modifica el comportamiento de un metodo
    @property#encapsula el atributo y solo se puede acceder a el mediante el metodo
    #@property debido a su uso al llamar al metodo correspondiente no sera necesario usar () parametros de invocacion
    def nombre(self):#metodo get nombre
        return self._nombre
    
    @nombre.setter#indicamos que sera un metodo de tipo set
    def nombre(self, nombre):#metodo set nombre
        self._nombre = nombre
    #una variable de solo lectura no cuenta con un metodo set
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
        
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
        
    #metodo destructor /elmina un objeto -srive para liberar memoria
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__': #validacion para saber si se esta ejecutando este modulo como principal de no cumplirse no se ejecuta el bloque de codigo  
    persona1 = Persona('yakumo','sahashi',25)
    persona1.mostrar_detalle()
    persona1.nombre = 'sasuke'
    persona1.apellido = 'uchiha'
    persona1.edad = 30
    persona1.mostrar_detalle()


""" print(__name__)#podemos saber con que modulo se esta trabajando """