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