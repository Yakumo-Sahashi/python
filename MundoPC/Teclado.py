from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclado = 0
    
    def __init__(self,marca,tipo_entrada):
        Teclado.contador_teclado += 1
        self.id_teclado = Teclado.contador_teclado
        super().__init__(marca,tipo_entrada)
        
    def __str__(self):
        return f"ID: {self.id_teclado}, marca: {self.marca}, tipo_entrada: {self.tipoEntrada}"
    
    
if __name__ == '__main__':
    teclado1 = Teclado('GamerFactory','USB')
    teclado2 = Teclado('HP','Bluetooth')
    print(teclado1)
    print(teclado2)
    