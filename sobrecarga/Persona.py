class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __add__(self,otro):
        return f"{self.nombre} {otro.nombre}"
    
    def __sub__(self,otro):
        return self.edad - otro.edad    

persona1 = Persona('Yakumo',21)
persona2 = Persona('Haruka',20)

print(persona1 + persona2)
print(persona1 - persona2)