lista = [6, 3, 2, 7, 8, 1, 9, 4]
for i in range(len(lista)):
    for x in range(len(lista)-1):
        if lista[x] > lista[x + 1]:
            lista[x], lista[x+1] = lista[x+1], lista[x]
print(lista)