#un generador es una funcion especial en python, retorna una secuencia de valores
#susprende la ejecucion de la funcion yield (producir) (no se usa return)

def generador():
    yield 1
    print('se reanuda la ejecucion')
    yield 2
    print('se reanuda la ejecucion')
    yield 3
    
#consumimos el generador a demanda
gen = generador()

#con cada llamada consumimos un valor 
print(next(gen))
print(next(gen))
print(next(gen))
#si tratamos de consumir mas valores de los que produce el generador lanza un error de StopIteration

#consumiendo los valores del generador con un ciclo for
for valor in generador():
    print(f'numero generado: {valor}')