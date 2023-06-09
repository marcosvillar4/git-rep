resp = ''
lista = []
import csv
import funciones as f

def func(lista):
    resp = ''
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
            lista = f.func1(lista)
            
            return lista
        case '2':
            lista = f.func2(lista)
            
            return lista
        case '3':
            lista = f.func3(lista)
            
            return lista
            
        case '4':
            lista = f.func4(lista)
            
            return lista
        case '5':
            lista = f.func5(lista)
            
            return lista
        case '6':
            lista = f.func6(lista)
            
            return lista
        case '7':
            lista = f.func7(lista)
            
            return lista
        case '8':
            lista = f.func8(lista)
            return lista
        case '9':
            f.func9(lista)
            
            return lista
        case '10':            
            f.func10(lista)
            return lista
            
        case '11':
            f.func11(lista)
            print(lista)
            return lista
        case 'S':
            stop = True
            lista = ['temp']
            return lista
end = ''
while end != 'N':
    end = ''
    exitco = False
    lista = func(lista)
    if lista == ['temp']:
        break
    
    while end != 'N' and end != 'S':
        print('Desea realizar otra operacion?')
        end = str.upper(str(input('Respuesta: ')))