
numeros = [1,2,3]
print(numeros)
#en lugar de imprimir una lista imprime cada uno de los elementos (los desempaqueta)
print(*numeros)

print(*numeros,sep=' - ')

def suma(a,b,c):
    print(f'Resultado de la suma: {a + b + c}')

suma(*numeros)

#extraer algunas partes de una lista

mi_lista = [1,2,3,4,5,6]
a,*b,c,d = mi_lista
print(a,b,c,d)

#unir listas

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1,lista2]
print(f'Lista de listas: {lista3}')
lista3 = [*lista1, *lista2]
print(f'Unir las listas: {lista3}')

#Unir diccionarios

dic1 = {'a':1,'b':2,'c':3}
dic2 = {'d':4,'e':5}
dic3 = {**dic1, **dic2}
print(f'Unir dicccionarios: {dic3}')

#construir una lista a partir de un str

lista = [*'Hola mundo']
print(lista)
print(*lista, sep='')