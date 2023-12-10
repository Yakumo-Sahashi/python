import logging as log
#level=log.DEBUG indicamos con el nivel a trabajar
#format='%(asctime)s:' agrega el tiempo y fecha al mensaje de log 
#%(levelname)s en que nivel se presento el error 
#%(filename)s:%(lineno)s] el archivo y linea 
#%(message)s el mensaje de error
#,datefmt='%I:%M:%S %p' formato de la hora 
#handlers=[log.FileHandler('capa_datos.log')] permite enviar la informacion a un archivo
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('mensaje a nivel debug')
    log.info('mensaje a nivel info')
    log.warning('mensaje a nivel warning')
    log.error('mensaje a nivel error')
    log.critical('mensaje a nivel critical')
