try:
    archivo = open('prueba.txt','r',encoding='utf8')
    #leer linea a linea el contenido del archivo mediante un for
    """ for linea in archivo:
        print(linea) """
        
    #lee el archivo y regresa cada linea en una posicion de un arreglo (lista)
    """ print(archivo.readlines()) """
    #acceder a una linea especifica
    """ print(archivo.readlines()[0]) """
    #copiar un archivo
    archivo2 = open('copia.txt','a',encoding='utf8')
    archivo2.write(archivo.read())
except Exception as e:
    print(f"{e}")
finally:
    archivo.close()
    archivo2.close()
    print("Se ha terminado de leer y copiar el contenido de los archivos")
