#representacion de objetos (str, repr, format)

#despliega los metodos disponibles de una clase
#print(dir(object))

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # repr, más enfocado a los programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre:{self.nombre}, apellido:{self.apellido})'
    
    #str es mas enfocadi oara el usuario final u otros sistemas
    #la imprementacion por default llama al metodo repr
    
    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'
    
    #format su implementacion por default es str
    #se manda a llamar al usar f-string
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'

persona1 = Persona('Juan','Perez')
#ponemos !r para llamar especificamente al metodo repr
print(f'Mi objeto persona1: {persona1!r}')
#str - de manera automatica el metodo print llama al metodo str
print(persona1)
#format
print(f'{persona1}')