#un decorador es una funcion que recibe una funcion y regresa otra
#lo utilizamos para extender funcionalidad
#1-funcion decorador (a) 
#2-funcion a decorar (b)
#3-funcion decorada (c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args,**kwargs):
        #pass
        print('antes de ejecutar la funcion')
        resultado = funcion_a_decorar_b(*args,**kwargs) 
        print('despues de ejecutar la funcion')
        return resultado    
    return funcion_decorada_c   

""" @funcion_decorador_a
def mostrar_msj():
    print('hola desde funcion mostrar_msj')
    
mostrar_msj()

@funcion_decorador_a
def imprimir():
    print('hola desde funcion imprimir')    
imprimir() """

@funcion_decorador_a
def sumar(a,b):
    return a + b

resultado = sumar(5,6) 
print(f'Resultado suma {resultado}')