#funciones lambda es una funcion anonima, son pequeñas (una sola linea de codigo)
#no es posible asignar una funcion directamente a una variable

"""mi_funcion = def sumar(a,b):
    return a + b
 """
#no se necesita agregar parentesos y la palabra return aunque debe regresar una expresion valida
#se usa la palabra reservada lambda
mi_funcion_lambda = lambda a,b: a+ b
print(mi_funcion_lambda(5,6))

# funcion lambda que no recibe argumentos pero si debe retornar
mi_funcion_lambda = lambda: 'Funcion sin argumentos'
print(f'Llamar funcion lambda sin argumentos: {mi_funcion_lambda()}')

# funcion lambda con parametros por default
mi_funcion_lambda = lambda a=2,b=3: a + b
print(f'Resultado argumentos por default: {mi_funcion_lambda(4,6)}')

# funcion lambda con argumentos variables *args y **kwargs
mi_funcion_lambda = lambda *args,**kwargs: len(args) + len(kwargs)
print(f'Resultado argumentos variables: {mi_funcion_lambda(1,2,3, a=5,b=6)}')

#funcion lambda con argumentos variables y valores por default
mi_funcion_lambda = lambda a,b,c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado funcion lambda: {mi_funcion_lambda(1,2,4, 5,6,7,e=5,f=7)}')