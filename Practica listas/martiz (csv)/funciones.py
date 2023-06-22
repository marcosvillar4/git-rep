def f1(lista):
    listtemp = []
    for i in range(0,len(lista[0])):
        valor = int(input('Valor a sumar a lista temp: '))
        listtemp.append(valor)
    lista.append(listtemp)
    return lista
def f2(lista):
    for i in range(0,len(lista)):
        print(lista[i])
    return lista
def f3(lista):
    listarow = []
    row = int(input('Fila: '))
    col = int(input('columna: '))
    listarow = lista[row - 1]   
    print(listarow[col - 1])
    return lista
def f4(lista):    
    for i in range(0, len(lista)):
        mayor = -999999999
        listtemp = lista[i]
        for val in range(0,len(listtemp)):
            if int(listtemp[val]) > mayor:
                mayor = int(listtemp[val])
        print(f'El mayor de la lista {lista[i]}, es {mayor}')
    return lista
def f5(lista):
    lenmat = len(lista[0])
    for col in range (0,lenmat):
        colact = []
        suma = 0
        prom = 0
        for row in range(0,len(lista)):
            rowactual = lista[row]
            colact.append(int(rowactual[col]))
        for avg in range(0,len(colact)):
            suma = suma + colact[avg]
        prom = suma / len(colact)
        print(f'El promedio de la columna {col}, es {prom}')
    return lista
def f6(lista):
    mayor = -9999999
    for row in range(0,len(lista)):
        listtemp = lista[row]
        for i in range(0,len(listtemp)):
            if int(listtemp[i]) > mayor:
                mayor = int(listtemp[i])
    print(f'El mayor es {mayor}')
    return lista
def f7(lista):
    import random
    templist = []
    for i in range (0, len(lista[0])):
        templist.append(str(random.randint(0,9999)))
    lista.append(templist)
    return lista
def f8(lista):
    lista.reverse()
    return lista