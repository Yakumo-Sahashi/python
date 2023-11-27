class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f'Vehiculo: [color: {self.color}, ruedas: {self.ruedas} ]'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    def __str__(self):
        return f'Velocidad: [{self.velocidad}], {super().__str__()}'
    
class Bicicleta(Vehiculo):
    def __init__(self,color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return f'Tipo: [{self.tipo}], {super().__str__()}'
    
vehiculo1 = Vehiculo("azul", 4)
print(vehiculo1)

coche1 = Coche("rojo", 4, 100)
print(coche1)

bicicleta1 = Bicicleta('negro', 2, "classic")
print(bicicleta1)