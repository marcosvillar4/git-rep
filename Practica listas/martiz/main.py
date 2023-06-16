resp = ''
matriz = []
import csv
import funciones as func
with open ('listaini.csv', 'r') as listaini:
    reader = csv.reader(listaini)
    for row in reader:
        matriz.append(row)
while resp != 'N':
    with open ('opciones.csv', 'r') as opciones:
        readerop = csv.reader(opciones)
        for row in readerop:
            print(row)
    resp = int(input('Que opcion desea usar: '))
    match resp:
        case 1:
            matriz = func.f1(matriz)        
        case 2:
            matriz = func.f2(matriz)        
        case 3:
            matriz = func.f3(matriz)        
        case 4:
            matriz = func.f4(matriz)        
        case 5:
            matriz = func.f5(matriz)            
        case 6:
            matriz = func.f6(matriz)        
        case 7:
            matriz = func.f7(matriz)        
        case 8:
            matriz = func.f8(matriz)
        case 9:
            break
    while resp != 'N' and resp != 'S':
        resp = str.upper(input('Desea realizar otra operacion?: '))