resp = ''
import csv

def func():

    print('Que funcion desea utilizar?')
        
    with open ('funciones.csv', 'r') as texto:
        csvreader = csv.reader(texto)
        for row in csvreader:
            newrow = str(row)
            newrow = newrow.replace('[', '')
            newrow = newrow.replace(']', '')
            newrow = newrow.replace("'", "")

            print(newrow)

    while resp not in ['1',"2",'3','4','5','6','7','8','9','10','11',"S"]:
        resp = str.upper(input('respuesta: '))
        if resp not in ['1',"2",'3','4','5','6','7','8','9','10','11',"S"]:
            print('Valor no valido')

    match resp:
        case '1':
            print(resp)
        case '2':
            print(resp)
        case '3':
            print(resp)
        case '4':
            print(resp)
        case '5':
            print(resp)
        case '6':
            print(resp)
        case '7':
            print(resp)
        case '8':
            print(resp)
        case '9':
            print(resp)
        case '10':
            print(resp)
        case '11':
            print(resp)
        case 's':
            print(resp)


func()