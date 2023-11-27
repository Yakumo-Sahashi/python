#variables de clase
class MiClase:
    #todos los objetos que pertenecen a esta clase tienen acceso a esta variable
    variable_clase = 'variable de clase'
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        
    #metodos estaticos se asocian a la clase
    #se utiliza el decorador staticmethod para indicar que el metodo es estatico
    #los metodos estaticos no pueden acceder a variables de instancia
    #no se pasa como parametro self porque hace referencia a un objeto y los metodos estaticos no pueden acceder a objetos
    @staticmethod
    def metodo_estatico():
        #para acceder a una variable de clase se debe hacer de manera indirecta / primero haciendo referencia a la clase a la cual le pertenece la viable(atributo)
        print(MiClase.variable_clase) 
             
    #metodo de clase
    #este si puede acceder a los atributos de clase
    @classmethod    
    def metodo_clase(cls):#cls oara representar que es el parametro de la clase en si
        #se utiliza cls en lugar de self para acceder a los atributos de clase
        print(cls.variable_clase) 
        
    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
              
""" print(MiClase.variable_clase)
miClase = MiClase('Variable de instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

#crear variables de clase en cualquier momento
MiClase.variable_clase2 = 'variable clase 2'
print(miClase.variable_clase2) """

#MiClase.metodo_estatico()
MiClase.metodo_clase()

#contexto estatico y dinamico
#el contexto dinamico puede acceder al estatico pero no a la inversa
#estatico / a nivel de clase (definicion metodos variables)
#dinamico / creacion de objetos meotodos (instancia)
miObjeto1 = MiClase('variable instancia')
miObjeto1.metodo_instancia()
