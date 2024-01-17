valores = 1,2,3;
print(valores)
print(type(valores))

#es equivalente a la desestructuracion en js
valor1,valor2,valor3 = 1,2,3
v1,v2,v3 = valores
print(v1)
print(valor2)

#al poner * al principio esta variable alamacenara en forma de lista todos los datos siguientes
val1,val2,*val3 = 1,2,3,4,5,6,7,8,9

print(val3)

#en caso de poner mas variables estas alamacenan el contenido de forma inversa
val1,val2,*val3,val4,val5 = 1,2,3,4,5,6,7,8,9
print(val3)


#con listas funciona igual

val1,val2,*val3,val4,val5 = [1,2,3,4,5,6,7,8,9]
print(val3)


def regresa_datos():
    return 1,2,3

val1,val2,val3 = regresa_datos()

print(val1,val2,val3)

#obtener ayuda
#help(str.partition)

#divide una cadena usando un caracter especifico, se genera una tupla, pero este tambien se guarda
""" variable = '17:20'.partition(':')

print(type(variable)) """

hora,separador,minutos = '17:20'.partition(':')

print(hora,minutos)