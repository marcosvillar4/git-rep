lista = []
listasum = 0



for i in range (0, int(input('longitud de la lista'))):
    lista.append(int(input('valor: ')))
    listasum = listasum + lista[i]
    print(listasum)