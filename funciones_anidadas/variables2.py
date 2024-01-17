# mas funciones anidadas y alcance de variables

def funcion_externa():
    variable_local_externa = 'variable local externa'
    
    def funcion_anidada():
        variable_local_anidada = 'variable local anidada'
        #para poder modificar la variable local externar sin crear una nueva se debe utilizar nonlocal
        nonlocal variable_local_externa
        variable_local_externa = 'nuevo valor variable local externa'
        
    funcion_anidada()
    
    print(f'valor variable local externa: {variable_local_externa}')
    
funcion_externa()