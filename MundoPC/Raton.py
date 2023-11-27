from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    #variable de clase
    contador_ratones = 0
    
    def __init__(self,marca,tipoEntrada):
        #accedemos a la varible atraves de la clase
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        super().__init__(marca,tipoEntrada)
    
    def __str__(self):
        return f"ID: {self.id_raton}, marca: {self.marca}, tipo_entrada: {self.tipoEntrada}"
    
    
#validacion para comprobar que se ejecute el programa desde este archivo para evitar problemas de seguridad
if __name__ == '__main__':
    raton1 = Raton('Logitech','USB')
    raton2 = Raton('ACER','Bluetooth')
    print(raton1)
    print(raton2)