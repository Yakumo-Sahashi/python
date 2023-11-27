#herencia
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
                
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
        
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._edad}')
    
    
    def __str__(self):#sobre escribe el metodo de la clase pader object
        return f'Persona: [ Nombre: {self._nombre} Edad: {self._edad}]'
        

#se usan parametros de invoacion para indicar de quien heredara sus caracteristicas
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)#se manda a traer el metodo inicializador de la clase padre
        self.sueldo = sueldo
        
    def __str__(self):#sobre escribe el metodo de la clase pader Persona
        #accedemos al metodo str para no repetir bloques de codigo super().__str__()
        return f'Empleado: [Sueldo: {self.sueldo}], {super().__str__()}'
   
if __name__ == '__main__':
    empleado1 = Empleado('yakumo',25,5000)
    empleado1.mostrar_detalle()