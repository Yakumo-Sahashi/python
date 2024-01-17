#profundizando en diccionarios

#los dic guardan un orden a diferencia de un set

diccionario = {'nombre':'juan','apellido':'perez','edad':28}
print(diccionario)

#los diccionarios son mutables pero las llaves no
""" diccionario = {(1,2):'valor'}
#se puede utilizar una tupla como llave porque su valor es inmutable
print(diccionario) """

#se agrega una llave si no se encuentra
diccionario['departamento'] = 'sistemas'
print(diccionario)

#no hay valores duplicados en las llaves de un diccionario (si ya existe se reemplaza)
diccionario['nombre'] = 'juan carlos'
print(diccionario)

# recuperar un valor indicando una llave
print(diccionario['nombre'])
# si no encuentra la llave lanza una excepcion

#metodo get recupera una llave y si no existe no lanza una excepcion
#podemos regresar un valor en caso de no existir la llave
print(diccionario.get('nombre','no se encontro la llave'))
#no moficia el diccionario

#setdefault si modifica el dicccionario en caso de no encontrar la llave y se puede agregar un valor por default
nombre = diccionario.setdefault('Nombre','Valor por default')
print(nombre)
print(diccionario)

#imprimir con print
from pprint import pprint as pp
""" help(pp) """
pp(diccionario,sort_dicts=False)