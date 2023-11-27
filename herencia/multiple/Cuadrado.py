#herencia multiple se le pasa como parametro las clases de las cual hereda   
from FiguraGeometrica import FiguraGeometrica
from Color import Color
#as para renombrar una clase  from Color import as NuevoNombre

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #para herencia multiple se inicializan los atributos de las clases padre accediendo al metodo inicializador directamente con el nombre de la clase
        #se utiliza self porque estamos trabajando direcctamente sobre el metodo init
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def calcular_area(self):
        return self.alto * self.ancho  
            