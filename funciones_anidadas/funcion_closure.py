#un closure es una funcion que define a otra y ademas la puede regresar 
#la funcion anidada puedes acceder a las variables locales definidas
#en la funcion principal o externa

#funcion principal
""" def operacion(a,b):
    #definimos una funcion interna o anidada
    def sumar():
        return a + b
    
    #retornar la funcion
    return sumar """

def operacion(a,b):
    return lambda: a + b    

mi_funcion_closure = operacion(5,2)
print(f'Resultado de la funcion closure: {mi_funcion_closure()}')

#llamar la funcion regresada al vuelo
print(f'Resultado de funcion closure al vuelo: {operacion(1,4)()}')

#