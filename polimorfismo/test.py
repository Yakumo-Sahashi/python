from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    """ imprimimos la clase a la cual le pertenece el objeto al que apuntamos"""
    print(type(objeto))
    """ print(objeto.mostrar_detalles()) """
    """ preguntamos si el objeto es una instancia de una clase especifica """
    #objeto a evaluar, Clase a la que debe pertenecer
    if isinstance(objeto, Gerente):
        print(objeto.departamento)
    
empleado = Empleado('Juan',5000)
gerente = Gerente('Luis',10000,'Sistemas')

imprimir_detalles(empleado)
imprimir_detalles(gerente)