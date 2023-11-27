class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = self._validar_valor(alto)
        self._ancho = self._validar_valor(ancho)
         
    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        self._alto = alto
        
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho
        
    def __str__(self):
        return f'Figura: [alto: {self._alto}, ancho: {self._ancho}]'
    
    #solo se sebe acceder a este metodo desde dentro de la clase
    def _validar_valor(self, valor):
        validacion = valor if 0 < valor < 10 else 0
        if validacion == 0:
            print(f'Valor erroneo: {valor}')
        return validacion
    
    
class Color:
    def __init__(self, color):
        self._color = color
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
        
    def __str__(self):
        return f'[Color: {self._color}]'
        
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def __str__(self):
        return f'Cuadrado: {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'
    
    def area(self):
        return self._alto * self._ancho
    
class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)        
        Color.__init__(self, color)
        
    def __str__(self):
        return f'Rectangulo: {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'
    
    def area(self):
        return self._alto * self._ancho
    
print('Creacion objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(5,"azul")
print(cuadrado1)
print(f'El area del cuadrado es: {cuadrado1.area()}')

print('Creacion objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(9,5,"naranja")
print(rectangulo1)
print(f'El area del rectangulo es: {rectangulo1.area()}')
    