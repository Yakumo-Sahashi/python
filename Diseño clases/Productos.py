
class Producto:
    contador_productos = 0
    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
    
    @property
    def precio(self):
        return self._precio
        
    def __str__(self):
        return f'Producto: id: {self._id_producto} Nombre: {self._nombre} Precio: {self._precio}'

if __name__ == '__main__':
    producto1 = Producto('Laptop', 14000.00)
    print(producto1)
    producto2 = Producto('Mouse', 200.00)
    print(producto2)