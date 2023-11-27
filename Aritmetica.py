""" class Aritmetica:
    
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    
    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB
    
aritmetica1 = Aritmetica(20,5)

print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicacion: {aritmetica1.multiplicar()}')
#indicamos la cantidad de ceros (digitos) que se mostrara :.2f (formato)
print(f'Division: {aritmetica1.dividir():.1f}') """

#ejercicio area rectangulo

class Area:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular(self):
        return self.base * self.altura
    
    
base = float(input('Proporciona la base: '))
altura = float(input('Proporciona la altura: '))
area1 = Area(base, altura)
print(f'Area del rectangulo: {area1.calcular()}')
        