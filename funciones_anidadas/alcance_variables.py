#alcance de variables (scope)

var_global = 'Variable global'

def imprimir():
    #accder a una variable global
    #se utiliza para poder acceder a la variable local dentro del bloque de codigo
    global var_global
    
    print(f'Variable global desde una funcion: {var_global}')
    #definicion de variable local
    var_local = 'variable local'
    print(f'Variable local accedida desde una funcion: {var_local}')
    var_global = 'nuevo valor Variable global'
    def funcion_anidada():
        print(f'Variable local funcion anidada: {var_local}')
        
    funcion_anidada()
    
imprimir()
print(f'variable global fuera de funcion: {var_global}')

