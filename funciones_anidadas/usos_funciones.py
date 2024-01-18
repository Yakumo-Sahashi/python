#las funciones en python son ciudadanas de primera clase

#definir la funcion 
def sumar(a,b):
    return a + b

#1- asignar una funcion a una variable (no se usa parentesis)
mi_funcion = sumar

#llamamos la funcion mediante la variable a la cual se asigno
print(mi_funcion(5,6))

#2- funcion como argumento

def operacion(a,b,sumar_arg):
    print(f'Resultado suma: {sumar_arg(a,b)}')
    
operacion(4,5,sumar)
operacion(4,2,mi_funcion)

#3- retornar una funcion
def retornar_funcion():
    #retornamos una funcion
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'Resultado suma: {mi_funcion_retornada(2,3)}')