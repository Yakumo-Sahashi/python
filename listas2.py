#creacion basica
nombre = ['juan','karla','pedro']
#usando el metodo split 
#si este no recibe un racter por defecto utiliza un espacio en blanco
nombre2 = 'laura maria gonzalo ernesto'.split()

#suma de listas
#de esta manera no se alteran las listas originales
print(f"sumar listas {nombre + nombre2}")

#extender una lista con otra lista
#al usar la funcion extend si se alteran las listas originales
#recibe como argumento la lista a sumar
nombre.extend(nombre2)
print(f"Extender las lista 1 con la 2: {nombre}")

#indices
numeros = [10,40,15,4,20,90]
#obtener el indice del primer elemento encontrado en una lista
#ayuda a encontrar el indice de un elemento dentro de una lista
print(f"indice 4: {numeros.index(4)}")

#invertir el orden de los elementos de una lista
#modifica directamente la lista
numeros.reverse()

print(f"lista invertida {numeros}")

#ordenar ascendente
numeros.sort()
print(f"ordenada: {numeros}")

#ordenar descendente
#se pasa como argumento reverse con un valor de verdadero
numeros.sort(reverse=True)
print(f"ordenada des: {numeros}")

#min y max de una lista
print(f"valor mimino: {min(numeros)}")

print(f"valor maximo: {max(numeros)}")

#copiar los elementos de una lista
#la funcion copy permite copiar los elementos de una lista a otra
numeros2 = numeros.copy()
print(f"copia de lista: {numeros2}")
#realiza una copia superficial
print(f"Misma referencia? {numeros is numeros2}") #is para preguntar si es la misma referencia de memoria
print(f"Mismo contenido? {numeros == numeros2}")#== para preguntar si el mismo contenido

#copia mendiante el uso del constructor de la lista
numeros2 = list(numeros)
print(f"Misma referencia? {numeros is numeros2}") #is para preguntar si es la misma referencia de memoria
print(f"Mismo contenido? {numeros == numeros2}")#== para preguntar si el mismo contenido

#copia con slicing
numeros2 = numeros[:]
print(f"Misma referencia? {numeros is numeros2}") #is para preguntar si es la misma referencia de memoria
print(f"Mismo contenido? {numeros == numeros2}")#== para preguntar si el mismo contenido


#Multiplicacion de listas
#se genera una copia de la misma referencia de memoria
lista_multi = 5*[[2,5]]

print(lista_multi)
print(f"Misma referencia? {lista_multi[0] is lista_multi[1]}")
print(f"Mismo contenido? {lista_multi[0] == lista_multi[1]}")
lista_multi[2].append(10)
print(lista_multi)

#Matrices en python

matriz = [[10,20],[30,40,50],[60,70,80,90]]
print(f'Matriz: {matriz}')
print(f'Renglon 0, columna 0: {matriz[0][0]}')
print(f'Renglon 2, columna 2: {matriz[2][2]}')
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')

lista_listas = [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
#ordenar por el largo de los elementos de la lista
lista_listas.sort(key=len)
print(f'ordenada {lista_listas}')

#sorted built-in --->ya esta integrada en el lenguaje de python

nombres1 = ['juan carlos','karla','pedro','esperanza']
nombres1 = sorted(nombres1)
print(f'ordenada {nombres1}')

#ordenar descendente
nombres1 = sorted(nombres1,reverse=True)
print(f'ordenada {nombres1}')

#ordenar por la cantidad de caracteres (largo)
nombres1 = sorted(nombres1,key=len)
print(f'orden caracteres {nombres1}')

#built-in reversed
nombres1 = reversed(nombres1)
#es necesario convertir a una lista o tupla
print(f'orden {list(nombres1)}')


