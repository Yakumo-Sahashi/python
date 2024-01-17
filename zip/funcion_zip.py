#imprime las clases y funciones disponibles de manera automatica en python
""" print(dir(__builtins__))
help(zip) """

numeros = [1,2,3]
letras = ['a','b','c']
identificadores = 321,322,323,324,325
conjunto = {6,4,0,9,8,15,10}
#funcion zip
#combina listas de distintos tipos
#el iterable con menor elementos determina la cantidad de elementos a tomar de los demas

mezcla = zip(numeros,letras,identificadores,conjunto)
""" print(f'R: {mezcla}') """
#se debe convertir el resultado en una lista o tupla
""" print(f'R: {list(mezcla)}')
print(type(mezcla)) """


#iterar en paralelo

for numero, letra, id, aleatorio in zip(numeros,letras,identificadores,conjunto):
    print(f'Numero: {numero}, Letra: {letra}, ID: {id}, Aleatorio: {aleatorio}')
    
nueva_lista = []

for numero, letra, id, aleatorio in zip(numeros,letras,identificadores,conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
    
print(f'Nueva lista: {nueva_lista}')



# unzip
#hace un packing de diferentes iterables
mezcla = [(1,'a'),(2,'b'),(3,'c')]
numeros,letras = zip(*mezcla)
print(f'Numeros: {numeros}, Letras: {letras}')


#ordenamiento usando zip
letras = ['c','d','a','e','b']
numeros = [3,2,4,1,0]
mezcla = zip(letras,numeros)
print(tuple(mezcla))
print(sorted(zip(letras,numeros)))


#crear un dicccionario con zip y dos iterables

llaves = ['nombre','apellido','edad']
valores = ['juan','perez',18]
diccionario = dict(zip(llaves,valores))
print(diccionario)

#actualizar un elemento de un dicccionario
llave = ['edad']
nueva_edad = [28]
diccionario.update(zip(llave,nueva_edad))
print(diccionario)
