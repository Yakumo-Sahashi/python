#profundizando en el uso de set
#es una coleccion de elementos unicos y es mutable
#los elementos que almacena un set deben ser inmutables

#conjunto = {[1,2],[3,4]}

conjunto = {'juan',True,18.0}
print(conjunto)

#set vacio
""" conjunto = {} #genera un diccionario vacio
print(type(conjunto)) """

conjunto = set()
print(conjunto)
print(type(conjunto))

#mutable
conjunto.add('juan')
print(conjunto)

#contiene valores unicos
conjunto.add('juan')
print(conjunto)

#crear un set a partir de un iterable
conjunto = set([4,5,7,8,4])
print(conjunto)

#podemos agregar mas elementos o incluso otro set
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

#copiar un set (copia poco profunda, solo copia referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
print(f'Es igual el contenido? {conjunto_copia == conjunto}')
print(f'Es la misma referencia? {conjunto_copia is conjunto}')


#operaciones de conjuntos con set
#personas con distintas caracteristicas

pelo_negro = {'juan','karla','pedro','maria'}
pelo_rubio = {'lorenzo','laura','marco'}
ojos_cafe = {'karla','laura'}
menores_30 = {'juan','karla','maria'}

# funcion de UNION | todos los ojos de color cafe y pelo rubio (no se repiten elementos)
print(ojos_cafe.union(pelo_rubio))
#invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))

#intersection recupera los elementos que existen en ambos conjuntos | solo personas con pelo cafe y pelo rubio (conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

#difference recupera los elementos que se encuentrar en el primer conjunto (no es conmutativa)
print(pelo_negro.difference(ojos_cafe))

#(diferencia simetrica) pelo negro u ojos cafe, pero no ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

#preguntar si un set esta contenido en otro (subset)
#revisamos si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issubset(pelo_negro))

#peguntar sin un set contiene a otro set (superset)
#revisar si los elementos del primer set estan contenidas dentro del segundo
print(menores_30.issuperset(pelo_negro))

#preguntar si los de pelo negro tienen pelo rubio (distjoin)
print(pelo_negro.isdisjoint(pelo_rubio))