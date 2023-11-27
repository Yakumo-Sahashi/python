try:
    archivo = open('prueba.txt','r',encoding='utf8')
    #permite leer el contenido y mostrarlo por terminal
    """ print(archivo.read()) """
    #una vez ejecutado .read() el archivo se cierra
    #sele puede enviar la cantidad de caracteres a mostrar
    """ print(archivo.read(5)) """
    #leer lineas completas
    print(archivo.readline())
    print(archivo.readline())
except Exception as e:
    archivo.close()

