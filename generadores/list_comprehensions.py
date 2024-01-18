
numeros = range(10)
lista_pares = []

#creamos una nueva lista con los valores pares

for numero in numeros:
    #revisamos si es un numero par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)
        
print(f'lista pares: {lista_pares}')

#los mismo con listcomprehensions
#[expresion for variable in coleccion if condicion]
#la condicion de if es opcional
lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero %2 == 0]
print(f'lista pares comprehensions: {lista_pares}')

#ejemplo similar con dos condiciones
#solo se agrega el valor a la lista si cumple con amabas condiciones
#en este caso debe ser un numero divisible entre 2 y divisible entre 6
pares = [numero for numero in range(50) if numero %2 ==0 if numero %6 == 0]
print(f'lista divisible entre 2 y 6: {pares}')


#agregando if else
lista_pares = []
lista_impares = []

for numero in range(10):
    if numero%2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
        
print(f'pares: {lista_pares}')
print(f'impares: {lista_impares}')

#mimso ejemplo con listcomprehensions
lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero%2 == 0 else lista_impares.append(numero) for numero in range(10)]
print(f'pares: {lista_pares}')
print(f'impares: {lista_impares}')

#lista de listas
lista_listas = [[1,2,3],[4,5,6],[7,8,9,10]]
#convertimos la lista de listas en una sola lista
lista_simple = [valor for sublista in lista_listas for valor in sublista]
print(f'lista simple: {lista_simple}')

#creamos una lista de numeros pares a partir de la lista_listas
#sin list comprehensions
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor%2 == 0:
            lista_pares.append(valor)
            
print(f'pares: {lista_pares}')

#con list comprehensions
lista_pares = []
lista_pares = [valor for sublista in lista_listas for valor in sublista  if valor%2 == 0]
print(f'pares: {lista_pares}')