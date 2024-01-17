def calculadora(a,b, operacion='sumar'):
    #1- definir funcion anidada
    def sumar(a,b):
        return a + b
    
    def restar(a,b):
        return a - b
    
    def mutiplicar(a,b):
        return a * b
    
    def dividir(a,b):
        return a / b
    
    #2- llamamos a la funcion anidada
    if operacion == 'sumar':
        print(f'Resultado suma: {sumar(a,b)}')
    elif operacion == 'restar':    
        print(f'Resultado resta: {restar(a,b)}')
    elif operacion == 'mutiplicar':    
        print(f'Resultado multiplicar: {mutiplicar(a,b)}')
    elif operacion == 'dividir':    
        print(f'Resultado dividir: {dividir(a,b)}')
    
calculadora(5,6,'dividir')