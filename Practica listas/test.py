listav = ['10','5', "50", '58', '124', '3' , '-10' ]
listan = []
resp = ''

listan.append(int(listav[0]))
for p in range(0, len(listav)):
    valor = int(listav[p])
    for i in range(0, len(listan)):
        mayor = False
        if  valor > int(listav[i]):
                print('numero mayor, siguiendo')
                mayor = True
        elif valor < int(listav[i]):
            print('Valor menor, appendeando')
            listan.insert(i, int(valor))
            break
    if mayor == True:
         listan.append(valor)
    print(listav)
    print(listan)

    
