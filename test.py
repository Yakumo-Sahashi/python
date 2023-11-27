#print("Hola mundo") #impresion de texto por consola
#variables
miVariable = 10
""" print(id(miVariable)) """
#id(miVariable) se usa para saber la direccion de memoria de la variable (referencia de memoria)
""" print(type(miVariable)) """
#type(miVariable) devuelve el tipo de dato de la variable
#hint permite señalar el tipo de dato de una variable x: str = "cadena"
""" cadena = "mundo"
print("Hola ", cadena) """
#convertir a enterto int(variable)
#convertir a str str(miVariable)
""" print(str(miVariable))

if miVariable:
    print("Verdadero")
else:
    print("Falso") """
    
#entrada de teclado variable = input()
""" entrada1 = int(input("Ingresa el primer numero: ")) 
entrada2 = int(input("Ingresa el segundo numero: "))
resultado = entrada1 + entrada2
print("El contenido ingresado es: ", resultado)  """
#interpolacion necesita tener la letra f al principio
""" print(f"El contenido ingresado es: {miVariable ** 3}")

alto = int(input("Ingresa la altura: "))
ancho = int(input("Ingresa el ancho: "))

area = alto * ancho
perimetro = (alto + ancho) * 2

print(f"El area es: {area}\nEl perimetro es:", perimetro) """

#operadores de asignacion
""" miVariable += 2
print(miVariable) """

#numero = int(input("Ingresa un numero: "))

""" if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar") """
#not para trabajar con logica inversa
#operador ternario (?)

#print(f"El numero {numero} es par") if numero % 2 == 0 else print(f"El numero {numero} es impar")

#valor None indica que una variable aun no tiene ningun valor
""" variable = None

print(variable) """

#ciclo while
#condicion = 5
""" while condicion < 3:
    print(f'Numeo {condicion}')
    condicion += 1
else:
    print('fin del ciclo while')
     """
#ejercicio
""" while condicion > 0:
    print(f'Numeo {condicion}')
    condicion -= 1 """
#ciclo for
#cadena = 'hola mundo'

""" for letra in cadena:
    print(letra)
else:
    print('fin del ciclo for') """
    
#brake
""" for letra in cadena:
    if letra == 'a':
        print(letra)
        break
else:
    print('fin del ciclo for')
     """
     
""" for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}') """
#continue
""" for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
 """
 
 #listas

#nombres = ['sarada','sakura','sasuke','haruka']
""" print(nombres[0])
#navegacion inversa
print(nombres[-1])
#rango de valores
print(nombres[1:3])
print(nombres[1:]) """

""" for nombre in nombres:
    print(nombre) """
    
#obtner la longitud de una lista len(nombres)
#print(len(nombres))
#agregar elementos a una lista .append("elemento")
#nombres.append('yakumo')
#agregar elementos en posiciones especificas nombres.insert(1, 'kira')
#nombres.insert(1, 'kira')
#remover un elemento por valor nombres.remove('kira')
#nombres.remove('kira')
#remover por ultimo elemento nombres.pop()
#nombres.pop()
#elmininar indice especifico del nombres[0]
#del nombres[0]
#limpiar todo el contenido de un arreglo nombres.clear()
#nombres.clear()
#borrar la lista por completo del nombres
#del nombres
#print(nombres)

#tupla son inmutables no se pueden modificar
#definir una tupla
""" frutas =  ('naranja','sandia','melon',) #se declara con parentesis """
#longitud de una tupla
#la visualizacion de una tupla funciona igual que en una lista
""" for i in frutas:
    #quitar el salto de linea de una inpresion, se modifica el parametro end = "signacion del nuevo valor"
    print(i, end= ' ') """
    
#cambiar le valor de una tupla
#se pueden pasar los elementos de una tupla a una lista y luego convertirlo nuevamente a tupla despues de modificar
#convertir de tupla a lista con la funcion list(tupla)
""" frutaLista = list(frutas)
frutaLista[1] = 'manzana'
#convertir de lista a tupla con la funcion tuple(lista)
frutas = tuple(frutaLista)
print(frutas)
#eliminar por completo una tupla 
del frutas; """

#ejercicio tuplas y listas -- mostrar los numeros menores a 5
""" tupla = (12, 1, 8, 3, 2, 5, 8)
lista = []

for i in tupla:
    if i < 5:
        lista.append(i)
print(lista) """

#coleccion de tipo set (es como un objeto)

#no tiene un orden y no permite elementos duplicados
#se pueden modoficar sus elementos
#se pueden añadir nuevos elementos
""" planetas = {'marte', 'jupiter', 'venus'}
#al imprimirse siempre va a cambiar su orden
#se puede obtener la longitud al igual que en una lista
print(planetas) """
#podemos verificar si un elemento existe en la coleccion set
""" print('marte' in planetas) #devuelve un boleano """
#agregar un nuevo elemento .add('elemento')
""" planetas.add('tierra')
print(planetas)
#eliminar elementos en caso de no existir el elemento mandara un error .remove('elemento')
planetas.remove('tierra')
#eliminar un elemento sin producir un error en caso de no encontrarlo .discard('elemento')
planetas.discard('jupiter')
#eliminar todos los elementos .clear()
planetas.clear()
#eliminar por completo la coleccion set del 
del planetas
print(planetas) """

#diccionarios 

#funciona como un objeto con keys o un arreglo asociativo, no hay indices
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
""" print(diccionario)
#para obtener la longitud aplica la misma funcion que en una lista
print(len(diccionario)) """
#acceder a un elemento especifico
#mediante key
""" print(diccionario['OOP'])
#mediante funcion .get('key)
print(diccionario.get('IDE'))
#modificacion de elementos
diccionario['IDE'] = 'integrated development enviroment' """
""" print(diccionario) """
#recorrer elementos
#para acceder a los valores key y valor por separado se utiliza la funcion .items() directamente en el diccionario
""" for termino, valor in diccionario.items():
    print(termino, valor)
#para acceder solo a las keys se utiliza la funcion .keys()
for termino in diccionario.keys():
    print(termino)
#para obtener el valor relacionado a las keys se utiliza la funcion .values()
for valor in diccionario.values():
    print(valor) """
#comprobar la existencia de algun elemento se especifica la key
""" print('IDE' in diccionario) #devuelve un boleano
#agregar elementos
diccionario['PK'] = 'Prinmari Key'
print(diccionario)
#remover elemento mediante la funcion .pop('key')
diccionario.pop('IDE')
print(diccionario)
#eliminar todos los elementos de un diccionario
diccionario.clear()
print(diccionario)
#eliminar totalmente el diccionario
del diccionario
print(diccionario) """