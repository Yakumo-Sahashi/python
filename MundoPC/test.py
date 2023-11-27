from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden


teclado1 = Teclado('HP','USB')
raton1 = Raton('Logitech','USB')
monitor1 = Monitor('Lennovo',24)
computadora1 = Computadora('Yakumo',monitor1,teclado1,raton1)

teclado2 = Teclado('Gamer','USB')
raton2 = Raton('HP','Bluetooth')
monitor2 = Monitor('ASUS',27)
computadora2 = Computadora('Haruka',monitor2,teclado2,raton2)

teclado3 = Teclado('Gamer','Bluetooth')
raton3 = Raton('Corsait','USB')
monitor3 = Monitor('HP',24)
computadora3 = Computadora('Sakura',monitor3,teclado3,raton3)

computadoras1 = [computadora1,computadora2,computadora3]
orden1 = Orden(computadoras1)
computadoras2 = [computadora2,computadora1]
orden2 = Orden(computadoras2)
print(orden1)
print(orden2)