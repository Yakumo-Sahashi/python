class Monitor:
    contador_monitor = 0
    
    def __init__(self,marca,size):
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self._marca = marca 
        self._size = size
        
    def __str__(self):
        return f"ID: {self._id_monitor}, marca: {self._marca}, size: {self._size}"
    
     
if __name__ == '__main__':
    monitor1 = Monitor('Lennovo',24)
    monitor2 = Monitor('ACER',27)
    print(monitor1)
    print(monitor2)