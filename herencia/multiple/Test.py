from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5,"verde")
print(f'El calculo del area del cuadrado es: {cuadrado1.calcular_area()}')   

#metodo MRO - Method Resolution Order

#permite conocer la jerarquia de clases 
print(Cuadrado.mro())