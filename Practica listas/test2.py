lista = [2,7,4,2,3];
lista2 = [2,7,4,2,3];
ordenado = [];
ordenadomenor = []

while len(lista) != 0:
    mayor = 0;
    menor = 999999
    for i in lista:
        if i > mayor:
            mayor = i;
    ordenado.append(mayor);
    lista.remove(mayor);

    for j in lista2:
        if j < menor:
            menor = j;
    ordenadomenor.append(menor);
    lista2.remove(menor);
print(ordenado);
print(ordenadomenor)