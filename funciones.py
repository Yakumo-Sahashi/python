#funciones 

#para definir una funcion se usa la palabra reservada def (define)
""" def mi_funcion():
    print('hola desde mi funcion')
    
#invocar una funcion tal y como se hace en otros lenguajes
#respeta el scope no puedes utilizar algo que no esta definido
mi_funcion() """

#argumentos de una funcion
""" def funcion_con_argumentos(nombre):
    print(f'Hola {nombre}')   

funcion_con_argumentos('Diego') 
 """
#retorno de una funcion
""" def sumar(a, b):
    return a + b

primer_numero = int(input('Ingresa el primer numero a sumar: '))
segundo_numero = int(input('Ingresa el segundo numero a sumar: '))
print(f'El resultado de la suma es: {sumar(primer_numero, segundo_numero)}') """

#valores por defecto en los argumentos de una funcion | funciona igual que en js
""" def sumar(a = 0, b = 0) -> int: #-> int permite indicar el tipo de dato que devolvera (no es obligatorio regresar ese tipo de dato)
    return a + b

print(f'El resultado de la suma es: {sumar(10)}')  """

#numero de argumentos dinamicos (n argumentos) sintaxis comun *args
#al usar el * al principio de nuestro argumento los convierte en una tupla y se puede iterar de la misma manera
""" def lista_nombres(*nombres):
    print(nombres)
    for nombre in nombres:
        print(nombre)
        
lista_nombres('yakumo','sakura','haruka','shinobu') """

#ejercicio de argumentos variables
#ejercicio 1
""" def sumar(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(f'El resultado de la suma es: {sumar(3,5,9)}') """
#ejercicio 2
""" def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

print(f'El resultado de la multiplicacion es: {multiplicar(3,5,15)}')  """

#recibir un diccionario completo utilizar doble ** en documentacion **kwargs
""" def lista_terminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')    
        
lista_terminos(nombre='yakumo', apellido='saitou') """

#distintos tipos de datos como argumentos
""" 
def desplegar_nombres(nombres):
    for nombre in nombres:
        print(nombre)
        
nombres = ['haruka', 'sakura', 'yakumo','sasuke']
desplegar_nombres(nombres)#lista
desplegar_nombres('nombres')#cadena
desplegar_nombres((10,11))#tupla
desplegar_nombres([10,11])#lista """

#recursividad

#ejemplo factorial de un numero
""" def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
    
numero = int(input('Ingresa un numero a calcular su factorial: '))  
print(f'El factorial de {numero} es: {factorial(numero)}') """

#ejercicio recursividad

#imprimir los valores de un numero de manera descendente (solo numeros positivos)

""" def numeros(numero):
    if numero > 0:
        print(numero)
        numeros(numero-1)
    elif numero < 0:
        print('Solo se permite numeros mayores a 0!')
    else:
        return
             
numeros(1) """

#calculadora de impuestos
""" 
def calcular_impuestos(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)

pago = float(input('Proporciones el pago sin impuesto: '))
impuesto = float(input('Proporciones el monto del impuesto: '))
print(f'Pago con impuesto: {calcular_impuestos(pago, impuesto)}') """

#convertidor de celsuis a f

""" def grados_f(c):
    return (c * 1.8) + 32

def grados_c(f):
    return (f-32)/1.8

c = float(input('Ingresa °C: '))
f = float(input('Ingresa °F: '))

print(f'GRADOS CELSIUS A FAHRENHEIT: {grados_f(c)}')
print(f'FAHRENHEIT A CELSIUS: {grados_c(f)}') """