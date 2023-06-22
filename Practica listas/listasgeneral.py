resp = ''
lista = []

def func1(lista):
    valor = ''    
    valido = False
    while valido != True:        
        try:
            valor = int(input('Numero para agregar a lista: '))
            print(valor)
            valido = True
            lista.append(valor)
            return lista            
        except:
            print('valor no valido')
            valido = False

def func2(lista):
    valor = ''
    valido = False    
    while valido != True:
        valido = False
        try:
            valor = int(input('Numero para agregar a lista: '))
            pos = int(input('Posicion del valor en la lista (start en 1)'))
            if pos < 1:
                valido = False
                print('Posicion no valida')
            elif pos >= 1:
                valido = True
                lista.insert(pos - 1, valor)
                return lista                
        except:
            print('valor no valido')
            valido = False

def func3(lista):
    listtemp = []
    resp = ''
    while resp != 'N':
        resp = ''
        try:
            valor = int(input('Valor para lista a agregar: '))
            listtemp.append(valor)
        except:
            print('Valor no valido')
        while resp != 'N' and resp != 'S':
            print('Desea realizar agregar otro numero?')
            resp = str.upper(str(input('Respuesta: ')))

    for i in range(0, len(listtemp)):
        lista.append(listtemp[i])

    return lista

def func4(lista):
    if len(lista) != 0:
        ultimapos = len(lista) - 1
        print(ultimapos)
        print(f'El ultimo valor de la lista es {lista[ultimapos]}')
        lista.pop()
        return lista
    else:
        print('No es posible eliminar valores')
        return lista

def func5(lista):
    pos = 0
    valido = False
    print('Que posicion desea eliminar')
    while valido != True:
        try:
            pos = int(input('Posicion: '))
            if pos < len(lista) and pos > 0:
                lista.pop(pos - 1)
                valido = True
            else:
                valido = False
            
        except:
            print('valor no valido')
    return lista

def func6(lista):
    valido = False
    while valido != True:
        try:
            valor = int(input('Valor a buscar: '))
            print(f'La cantidad de veces que {valor} aparece en la lista es: {lista.count(valor)}')
            valido = True
        except:
            print('Valor no valido')
            valido = False

    return lista

def func7(lista):
    valido = False
    valor = 0
    while valido == False:
        try:
            valor = int(input('Valor a buscar posiciones: '))
            print(valor)
            valido = True            
            
        except:
            print('Valor no valido')
            valido = False            
        
        listapos = []
        listtemp = []
        listtemp = lista
        if valido == True:
            if valor not in lista:
                print('Valor no esta en la lista')
                valido = False
                
            else:
                lista.index(valor)
                listapos = []
                listtemp = []
                listtemp = lista.copy()
                print(listtemp)
                for i in range(0, len(lista)):
                    try:
                        posactual = listtemp.index(valor)
                        listapos.append(posactual + 1)
                        listtemp.pop(posactual)
                        listtemp.insert(posactual, 'temp')
                        
                    except:
                        break
        listaposfinal = str(listapos)
        listaposfinal = listaposfinal.replace('[', '')
        listaposfinal = listaposfinal.replace(']', '')

        print(f'El valor {valor}, se encuentra en las posciciones {listaposfinal}')
    
        return lista


def func8(lista):
    print(f'La lista es {lista}')

def func9(lista):
    mayor = -9999999999
    for i in range(0, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
        
    print(f'El mayor es {mayor}')

def func10(lista):
    menor = 9999999999
    for i in range(0, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
        
    print(f'El menor es {menor}')

def func11(lista):
    resp = ''
    print('Como desea ordenar (1 = menor a mayor, 2 = mayor a menor)')
    while resp != 1 and resp != 2:
        try:
            resp = int(input("Respuesta: "))
        except:
            print('Valor no valido')
            resp = 0

    if resp == 1:
        lista.sort()
    if resp == 2:
        lista.sort()
        lista.reverse()

    return lista

def func(lista):
    resp = ''
    print('Que funcion desea utilizar?')
        
    print("1. Agregar numero a la lista: Me pide un numero de la lista y lo agrega al final de la lista.")
    print("2. Agregar numero de la lista en una posicion: Me pide un numero y una posicion y si la posicion existe en la lista lo agreaga a ella (la posicion se pide a partir de 1).")
    print("3. Agregar un conjunto de datos a lista.")
    print("4. Eliminar el ultimo numero: Muestra el ultimo numero de la lista y lo borra.")
    print("5. Eliminar un numero: Pide una posicion y si la posicion existe en la lista lo borra de ella (la posicion se pide a partir de 1).")
    print("6. Contar numeros: Te pide un numero y te dice cuantas apariciones hay en la lista.")
    print("7. Posiciones de un numero: recibe un numero y te dice en que posiciones está (contando desde 1).")
    print("8. Mostrar lista: Muestra los numeros de la lista")
    print("9. buscar el mayor de la lista ")
    print("10. buscar el menor de la lista")
    print("11. ordenar por burbuja")
    print("S. Salir")

    while resp not in ['1',"2",'3','4','5','6','7','8','9','10','11',"S"]:          #chequeamos que la respuesta no tenga estos items      
        resp = str.upper(input('respuesta: '))                                      #Definimos la respuesta como este item
        if resp not in ['1',"2",'3','4','5','6','7','8','9','10','11',"S"]:         #Si la respuesta no esta en estos items, que repita el ciclo
            print('Valor no valido')
    
    match resp:                                                                     #Chequeamos la respuesta y ejecutamos la funcion correspondiente (match y case funciona como un if else largo)
        case '1':
            lista = func1(lista)
            
            return lista
        case '2':
            lista = func2(lista)
            
            return lista
        case '3':
            lista = func3(lista)
            
            return lista
            
        case '4':
            lista = func4(lista)
            
            return lista
        case '5':
            lista = func5(lista)
            
            return lista
        case '6':
            lista = func6(lista)
            
            return lista
        case '7':
            lista = func7(lista)
            
            return lista
        case '8':
            lista = func8(lista)
            return lista
        case '9':
            func9(lista)
            
            return lista
        case '10':            
            func10(lista)
            return lista
            
        case '11':
            func11(lista)
            print(lista)
            return lista
        case 'S':
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