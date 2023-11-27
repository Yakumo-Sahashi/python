#clases y objetos

class Persona:
    #pass palabra reservada para indicar que ya no se procesara nada mas, tambien se utiliza en funciones si se quiere declarar pero no se le pone ningun contenido
    #metodo inicializador funje como el constructor (El constructor esta oculto y se manda a llamar por el lenguaje)
    #permite agredar atributos e inicializar
    def __init__(self, nombre, apellido, edad, *valores, **terminos):#metodo de tipo dunder
    #__init__ double underscore (dunder)
    #self hace referencia al parametro que se va a crear (se puede renombrar)
        #atributo de instancia
        self.nombre =  nombre#self equivalente a this en js
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    #el parametro self se debe agregar a todos los metodos de instancia   
    #seles conoce como metodos de instancia por que se relacionan con los objetos que se crearan
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')
    
""" print(type(Persona)) """

persona1 = Persona('yakumo','sahashi',25,'5517797884',2,3,4, m='manzana',p='pera') #instancia de clase no es necesario utilizar new

#print(persona1.nombre)
#acceder a un metodo mediante un objeto
""" persona1.mostrar_detalle()
#acceder a un metodo utilizando directamente la clase pero se debe pasar como referencia un objeto
Persona.mostrar_detalle(persona1) """
#agregar un nuevo atributo a la clase mediante un objeto
persona1.telefono = '5517797884'
print(persona1.mostrar_detalle())
#metodos de instancia de una clase
