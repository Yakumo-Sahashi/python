from ExceptionPersonalizada import ExceptionPersonalizada

resultado = None
a = 10
b = 1

#equivalente a un try catch en otros lenguajes
try:
    #10/0
    a = int(input('ingresa el primer numero: '))
    b = int(input('ingresa el segundo numero: '))
    if a == b:#validacion de un error personalizado
        raise ExceptionPersonalizada('numeros identicos')#mensaje que se arroja en caso de presentaser el error señalado
    resultado = a/b
    
except Exception as e:
    print(f"ocurrio un error: {e}, type: {type(e)}")
#se usa si no se presento ningun tipo de error
else:
    print("No se arrojo ninguna excepcion")
#siempre se ejecuta ya se haya presentado un error o no
finally:
    print("bloque finalizado")    
    
print(f"Resultado: {resultado}")
print("continuamos...")   
