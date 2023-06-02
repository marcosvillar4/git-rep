lista = []
suma = 0
with open ('alturas.csv', 'r') as alturas:
    for row in alturas:
        lista.append(float(row) * 100)
for i in range (0, len(lista)):
    suma = suma + lista[i]
print((suma / len(lista))/100)