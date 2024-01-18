#simulacion de sobrecarga de constructores
#otras formas de crear objetos

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    @classmethod
    def crear_persona_vacia(cls):
        #al retornar cls con parentesis se manda a llamar de manera indirecta al metodo init
        return cls(None,None)
    
    @classmethod
    def crear_persona_con_valores(cls,nombre,apellido):
        return cls(nombre,apellido)
    
    def __str__(self):
        return f'nombre: {self.nombre}, apellido: {self.apellido}'
             

persona1 = Persona('juan','perez')
print(persona1)
persona_vacio = Persona.crear_persona_vacia()
print(persona_vacio)
persona_con_valores = Persona.crear_persona_con_valores('karla','gomez')
print(persona_con_valores)
