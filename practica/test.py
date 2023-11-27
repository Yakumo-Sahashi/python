""" def solution(year):
    siglo_inicio = 0
    siglo_fin = 100    
    for i in range(22):        
        if siglo_inicio > year < siglo_fin:
            return i
        if i == 0:
            siglo_inicio = 1
            siglo_fin += 1
        siglo_inicio += 100
        siglo_fin += 100
print(f'El siglo es: {solution(1905)}') """


""" def solution(inputString):
    palindromo = inputString[::-1]
    if inputString == palindromo:
        return True
    else:
        return False
        
solution('aabaa') """

inputArray = [-23, 4, -3, 8, -12]
mayor = -100
for i in range(len(inputArray)):
    if i < len(inputArray) - 1:
        producto = inputArray[i] * inputArray[i+1]
    if producto > mayor:
        mayor = producto
print(mayor)