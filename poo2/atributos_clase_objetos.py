
class Persona:
    contador_personas = 0
    
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        

#mostrar atributos de un objeto
persona1 = Persona('juan','perez')
#__dict__ despliega los atributos asociados a este objeto
print(persona1.__dict__)

#crear un atributo al vuelo
print(persona1.contador_personas) #accediendo al atributo de clase
#pero no es posible modificarlo con el objeto, sino con la clse
persona1.contador_personas = 10
print(persona1.__dict__)

#el atributo anterior oculta el atributo de clase
print(Persona.contador_personas) #atributo de clase
print(persona1.contador_personas) #atributo de objeto1

#segundo objeto
persona2 = Persona('karla','gomez')
print(persona2.__dict__)
print(persona2.contador_personas)

#asociar un atributo de clase al vuelo

Persona.persona2 = 20
print(Persona.persona2)
