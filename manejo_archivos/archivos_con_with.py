
from ManejoArchivos import ManejoArchivos

#with abre y cierra el archivo de manera automatica
#se abre el archivo y se asigna el contenido a una variable
#uso nativamente de with
""" with open('prueba.txt','r',encoding='utf8') as archivo:  """
#uso con sobreescritura de metodos
with ManejoArchivos('prueba.txt') as archivo: 
    print(archivo.read())    
    """ 
        metodos internos de with
        __enter__ abre el archivo
        __exit__ cierra el archivo
    """
    