vec1 = []
vec2 = []

for i in range (0,20):
    check = False
    while check != True:
        try:
            valor = int(input(f'Valor vec1 en posicion {i}: '))
            vec1.append(valor)
            check = True
        except:
            print('valor no valido, solo se admiten numeros enteros')


for i in range (0,20):
    check = False
    while check != True:
        try:
            valor = int(input(f'Valor vec2 en posicion {i}: '))
            vec2.append(valor)
            check = True
        except:
            print('valor no valido, solo se admiten numeros enteros')

for i in range (0, len(vec1)):
    if vec1[i] == vec2[i]:
        valido = True
    else:
        valido = False
        break

if valido == False:
    print('las listas no son iguales')
elif valido == True:
    print('las listas son iguales')
