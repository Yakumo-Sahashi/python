""" F = []
N = input().split(' ')
S = input().split(' ')

def sobreescribir(a):        
    S[int(a[1])-1] = int(a[2])
    
def obtener_min_max(c):
    mm =  S[(int(c[1])-1):int(c[2])]
    j = 0
    for i in mm:
        mm[j] = int(i)
        j += 1   
    mm.sort() 
    F.append(str(mm[0]) + ' '+ str(mm[len(mm)-1]))

def mostrar_resultado():
    for i in F:
        print(i)

for i in range(int(N[1])):
    if i%2 == 0:
        obtener_min_max(input().split(' '))
    else:
        sobreescribir(input().split(' '))
        
mostrar_resultado() """


texto = ''  
def calcular():  
    n = input().split(' ')
    n[0] = int(n[0])
    n[1] = int(n[1])        
    n.sort()
    m = sum(n)
    for j in range(n[0]+1,n[1]):
        m += j 
    return m
for i in range(int(input())):
    texto += str(calcular()) + '\n'
print(texto)

    

""" cadena= 'Best Tec NM 2.0 7777777a'
final = []
dicconario = {
'A' : 'Alfa ',
'N' : 'November ',
'1' : 'One',
'B' : 'Bravo ',
'O' : 'Oscar ',
'2' : 'Two',
'C' : 'Charlie ',
'P' : 'Papa ',
'3' : 'Three',
'D' : 'Delta ',
'Q' : 'Quebec ',
'4' : 'Four',
'E' : 'Echo ',
'R' : 'Romeo ',
'5' : 'Five',
'F' : 'Foxtrot S',
'S' :'sierra ',
'6' :' Six',
'G' : 'Golf ',
'T' : 'Tango ',
'7' : 'Seven',
'H' : 'Hotel ',
'U' : 'Uniform ',
'8' : 'Eight',
'I' : 'India ',
'V' : 'Victor ',
'9' : 'Nine',
'J' : 'Juliett ',
'W' : 'Whiskey ',
'0' : 'Zero',
'K' : 'Kilo ',
'X' : 'X-Ray ',
'.' : 'Decimal',
'L': 'Lima ',
'Y': 'Yankee',
'M': 'Mike ',
'Z': 'Zulu',
}

code = ['','','double', 'triple', 'quadruple' ,'quintuple']
nueva = {}
valor=''
for i in cadena:
    if i != ' ':
        final.append(dicconario[i.upper()])
        
for j in final: 
    if j in nueva:
        if j == valor:
            nueva[j] += int(1)
    else:
        nueva[j] = int(1)
    valor = j
    
for k,v in nueva.items():
    if v > 1:
        if v > 5:
            print(code[5],k, end= ' ') 
            print(code[int(v)-5],k, end= ' ')
        else:
            print(code[int(v)],k, end= ' ')
    else: 
        print(k, end= ' ') 
         """
    