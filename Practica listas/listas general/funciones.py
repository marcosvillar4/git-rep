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