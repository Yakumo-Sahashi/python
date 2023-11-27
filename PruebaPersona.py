from encapsulamiento import Persona
#center(50,'-') permite centrar texto recibe como parametros la cantidad de caracteres y el tipo de caracter a utilizar
print('creacion de objetos'.center(50,'-'))
persona1 = Persona('sakura','uchiha',30)
persona1.mostrar_detalle()
#print(__name__)

#destructor
print('eliminacion de objetos'.center(50,'-'))
#para eliminar un objeto se utiliza la palabra reservada del al igual que para eliminar variables
del persona1
#existe un recolector de basura que se encarga de eliminar de manera automatica los objetos que no estan apuntados por una variable o si el programa termina su ejecucion


#herencia
#todas las clases en python heredan directamente de la clase object de manera automatica al menos que se especifique otro padre
