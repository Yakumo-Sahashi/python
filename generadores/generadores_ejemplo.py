#generador de numeros del 1 al 5
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('se reanuda la ejecucion de funcion')
        
#utilizamos el generador
generador = generador_numeros()        
print(f'Objeto generador: {generador}')
print(type(generador))

#consumimos los valores del generador
for valor in generador:
    print(f'numero producido: {valor}')
    
#consumir demanda
generador = generador_numeros()
#si no se vuelven a generar se produce un error
print(f'cosumimos a demanda: {next(generador)}')

#otra forma de consumir un generador
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        #se usa next porque no solicita el siguiente numero de manera automatica como en el for
        print(f'Impresion valor generado: {valor}')
    except StopIteration as e:
        print('se termino de iterrar el generador')
        break