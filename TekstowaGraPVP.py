#Prosta gra pvp. Zakres normalnego DMG 1-5. Cios krytyczny - 10 DMG. Szansa na cios krytyczny i podwójne uderzenie - 20%
#Autor - Mateusz Szynalik

#Zaimportowanie modułu generującego liczby pseudolosowe
from random import randint

#Zadeklarowanie początkowej ilości HP.
hp1 = 100
hp2 = 100

#Zadeklarowanie walki do momentu spadku ilości życia któregoś z zawodników do 0.
while hp1 > 0 and hp2 > 0:
#losowanie wartości zadanego DMG
    hit1 = randint(2, 5)
    hit2 = randint(2, 5)
#losowanie podwójnego uderzenia z szansą 20%
    speed1 = randint(10, 14)
    speed2 = randint(10, 14)
    if hit1 == 5:
        if hp1 <= 0:
            break
        else:
            hp2 -= 10
            print("Cios krytyczny! Zawodnik 1 zadał cios 10 dmg!")
            print(f"Wynik po uderzeniu - {hp1}hp - {hp2}hp")
            print()
    else:
        if hp1 <= 0:
            break
        else:
#Przykładowa wartość wylosowanej liczby do podjęcia decyzji o podwójnym uderzeniu
            if speed1 == 11:
                hp2 -= hit1
                hp2 -= hit1
                print(f"Speed! Zawodnik 1 dwukrotnie zadał {hit1} dmg.")
            else:
                hp2 -= hit1
                print(f"Zawodnik 1 zadał cios {hit1} dmg.")
            print(f"Wynik po uderzeniu - {hp1}hp - {hp2}hp")
            print()
    if hit2 == 5:
        if hp2 <= 0:
            break
        else:
            hp1 -= 10
            print("Cios krytyczny! Zawodnik 2 zadał 10 dmg!")
            print(f"Wynik po uderzeniu - {hp1}hp - {hp2}hp")
            print()
    else:
        if hp2 <= 0:
            break
        else:
            if speed2 == 11:
                hp1 -= hit2
                hp1 -= hit2
                print(f"Speed! Zawodnik 2 dwukrotnie zadał {hit2}dmg.")
            else:
                hp1 -= hit2
                print(f"Zawodnik 2 zadał cios {hit2} dmg.")
            print(f"Wynik po uderzeniu - {hp1}hp - {hp2}hp")
            print()

#Przedstawienie wyniku bitwy
if hp1 <= 0:
    print(f"Wygrał zawodnik 2. Zostało mu {hp2}hp")
elif hp2 <= 0:
    print(f"Wygrał zawodnik 1. Zostało mu {hp1}hp")
else:
    print("Bitwa trwa dalej...")



