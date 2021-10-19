#Program imituję gre w lotto - użytkownik wprowadza 6 cyfr z zakresu 1-49, program losuje liczby i informuje użytkownika ile liczb trafił i ile pieniędzy wygrał.
#Autor - Mateusz Szynalik
#Data - 19.10.2021
import random

print("Program symuluję gre w Lotto. Podążaj zgodnie z instrukcjami programu. Zostaniesz poproszony o wprowadzenie 6 wybranych liczb z zakresu 1-49.")
print("Wygrane: 3 trafione - 15 złotych; 4 trafione - 100 złotych; 5 trafionych - 5000 złotych; 6 trafionych - 2 miliony złotych.")

def Informacja():
    print(f"Do tej pory obstawiłeś {ile_liczb} liczb.")
    print(f"Twoje liczby to: {liczby_gracza}.")

def Komunikat(trafione):
    if trafione == 0 or trafione == 1 or trafione == 2:
        print("Niestety, nic nie wygrałeś.")
    elif trafione == 3:
        print("Brawo! Wygrałeś 15 złotych.")
    elif trafione == 4:
        print("Brawo! Wygrałeś 100 złotych.")
    elif trafione == 5:
        print("Brawo! Wygrałeś 5000 złotych.")
    else:
        print("Wow! Wygrałeś główną nagrodę - 2 miliony złotych!")


liczby_gracza = []
ile_liczb = 0
while len(liczby_gracza) != 6:
    liczba_gracza = int(input("Podaj liczbę, z zakresu 1-49, którą chcesz obstawić: "))
    if liczba_gracza not in liczby_gracza and liczba_gracza > 0 and liczba_gracza < 50:
        liczby_gracza.append(liczba_gracza)
        ile_liczb += 1
        Informacja()
    else:
        print("Tę liczbę już obstawiłeś, lub jest ona spoza podanego zakresu. Podaj jakąś inną z zakresu 1-49.")
        Informacja()

wylosowane_liczby = []
while len(wylosowane_liczby) != 6:
    wybor = random.randint(1, 50)
    if wybor not in wylosowane_liczby:
        wylosowane_liczby.append(wybor)
    else:
        continue

lista_trafionych = []
trafione = 0
for elem in liczby_gracza:
    if elem in wylosowane_liczby:
        trafione += 1
        lista_trafionych.append(elem)



print(f"Program wylosował następujące liczby: {sorted(wylosowane_liczby)}. Trafiłeś {trafione} liczb(ę/y). Były to liczby {lista_trafionych}.")
Komunikat(trafione)