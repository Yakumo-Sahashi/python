from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor

class Computadora:
    
    contador_computadora = 0
    
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadora += 1
        self._id_computadora = Computadora.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        
    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        monitor: {self._monitor}
        teclado: {self._teclado}
        raton: {self._raton}
        '''
        
if __name__ == '__main__':
    teclado1 = Teclado('HP','USB')
    raton1 = Raton('Logitech','USB')
    monitor1 = Monitor('Lennovo',24)
    computadora1 = Computadora('Yakumo',monitor1,teclado1,raton1)
    print(computadora1)
    
    teclado2 = Teclado('Gamer','USB')
    raton2 = Raton('HP','Bluetooth')
    monitor2 = Monitor('ASUS',27)
    computadora2 = Computadora('Haruka',monitor2,teclado2,raton2)
    print(computadora2)