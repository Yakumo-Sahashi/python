#metodo "open": permite abrir archivos y en caso de no existir este, lo crea automaticamente
#se utiliza try porque el uso del metodo puede generar excepciones
try:
    #w = escribir informacion y crear
    #w+ = para leer y escribir 
    #r = leer
    #r+ = leer y escribir
    #a = anexa informacion en lugar de sobreescribir
    #x = crea el archivo en caso de no existir manda un error
    # tipos de archivo
    #t = texto
    #b = binario, img
    #encoding se utiliza para especificar el tipo de caracteres que se utilizara
    archivo = open('prueba.txt','w',encoding='utf8')
    #write permite escribir contenido en el archivo, sobreescribe el archivo en caso de tener datos
    archivo.write('Informacion del archivo...\n')
    archivo.write('Adiós')
except Exception as e:
    print(e)
finally:
    #utilizamos el bloque finally porque este siempre se ejecuta
    #cerrar el archivo abierto previamente
    archivo.close()
    #una vez cerrado el archivo no se puede hacer ninguna modificacion en este
    print("Archivo cerrado!")