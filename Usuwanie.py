"""
Funkcja Usuwanie usuwa co trzeci element w podanej liście do momentu gdy jej długość wynosi conajmniej 3. Następnie usuwa element drugi, a na końcu pierwszy.
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
print(f"Lista na starcie wygląda tak: {lst}.")

def StanListy():
    print(f"Lista teraz wygląda tak: {lst}.")

def Usuwanie(lst):
    while len(lst) > 0:
        if len(lst) > 2:
            co_druga = lst[2::3]
            print(f"Z listy usunięto liczby: {co_druga}")
            for elem in co_druga:
                if elem in lst:
                    lst.remove(elem)
            StanListy()
        elif len(lst) == 2:
            print(f"Z listy usunięto liczbę {lst[1]}.")
            lst.remove(lst[1])
            StanListy()
        else:
            print(f"Z listy usunięto liczbę {lst[0]}.")
            lst.remove(lst[0])
            print(f"Lista jest już pusta.")

print(Usuwanie(lst))