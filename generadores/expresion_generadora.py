#expresion generadora (es un generador anonimo)
#para definirlo en una variable se usa parentesis
mutiplicacion = (valor*valor for valor in range(4))
#print(mutiplicacion)
print(type(mutiplicacion))
print(next(mutiplicacion))
print(next(mutiplicacion))
print(next(mutiplicacion))
print(next(mutiplicacion))

#tambien se puede pasar una expresion generadora a una funcion sin el uso de parentesis
import math
suma = sum(valor*valor for valor in range(4))
print(f'Resultado suma: {suma}')

#tambien podemos usar una lista o cualquier otro iterador
lista = ['juan','perez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

#crear un string a partir de un generador creado a partir de una lista
lista = ['karla','gomez']
contador = 0
#definimos una funcion incrementar
def incrementar():
    global contador
    contador += 1
    return contador

#la primera parte es el yield, la segunda es el for, entre parentesis
generador = (f'{incrementar()}.{nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'cadena generada: {cadena}')