""" import numpy as np

a=np.array([1,1,1,1,1])

print(a+10)


cadena = ""
for j in range(1,6):
     for i in range(0,j):
          cadena = cadena + str(j)
print(cadena) """


class Persona:

     def __init__(self, edad, nombre):
          self.edad = edad
          self.nombre = nombre
          print( "Se ha creado a ", self.nombre, " de ", self.edad)

     def hablar(self,palabras ):
          print( self.nombre, ': ', palabras)

try:
    juan = Persona(30, "Juan")
    juan.hablar()
except Exception as e:
    print(f"ocurrio un error: {e}, type: {type(e)}")