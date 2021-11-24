lista = [6, 3, 2, 7, 8, 1, 9, 4, 0, 100, 11, 5]
for i in range(len(lista)-1):
    minimum = min(lista[i:])
    min_index = lista.index(minimum)
    if minimum < lista[i]:
        lista[i], lista[min_index] = lista[min_index], lista[i]
    print(lista, "min = ", minimum)
print(lista)