from Productos import Producto
from Orden import Orden

producto1 = Producto('Laptop', 14000.00)
producto2 = Producto('Mouse', 200.00)
producto3 = Producto('Monitos', 2000.00)
producto4 = Producto('Teclado', 800.00)
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
print(orden1)
print(f'Total orden 1: {orden1.calcular_total()}')
orden2 = Orden(productos2)
orden2.agregar_producto(producto1)
orden2.agregar_producto(producto2)
print(orden2)
print(f'Total orden 2: {orden2.calcular_total()}')