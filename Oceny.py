# Autor - Mateusz Szynalik
# Program służy przechowywaniu ocen ucznia, ich sumy, liczby i średniej, a także przechowywaniu informacji o tym czy uczeń jest zwolniony z danego przedmiotu.

print("W tym programie możesz przechowywać swoje oceny.")
# Poniżej przedstawiono nazewnictwo przedmiotów w programie, aby użytkownik wiedział dokładnie jak wpisać nazwę danego przedmiotu.
print("Nazwy przedmiotów: 'polski', 'matematyka', 'angielski', 'wf', 'religia', 'historia', 'geografia' ")
print()
polski = []
liczbaOcenPolski = 0
sumaPolski = 0
sredniaPol = 0
polskiZw = False

matematyka = []
liczbaOcenMatematyka = 0
sumaMatematyka = 0
sredniaMat = 0
matematykaZw = False

angielski = []
liczbaOcenAngielski = 0
sumaAngielski = 0
sredniaAng = 0
angielskiZw = False

wf = []
liczbaOcenWf = 0
sumaWf = 0
sredniaWf = 0
wfZw = False

religia = []
liczbaOcenReligia = 0
sumaReligia = 0
sredniaRel = 0
religiaZw = False

historia = []
liczbaOcenHistoria = 0
sumaHistoria = 0
sredniaHis = 0
historiaZw = False

geografia = []
liczbaOcenGeografia = 0
sumaGeografia = 0
sredniaGeo = 0
geografiaZw = False

liczbaWszystkich = 0
sumaWszystkich = 0


stop = "x"
# Zmienna clear utworzona w celu braku jakiejkolwiek akcji przy wystąpieniu warunku 'else'
clear = 0
while stop != "stop":
    stop = input("Z jakiego przedmiotu jesteś zwolniony? wpisz nazwę lub 'stop': ")
    if stop == "stop":
        break
    elif stop == "polski":
        polskiZw = True
    elif stop == "matematyka":
        matematykaZw = True
    elif stop == "angielski":
        angielskiZw = True
    elif stop == "wf":
        wfZw = True
    elif stop == "religia":
        religiaZw = True
    elif stop == "historia":
        historiaZw = True
    elif stop == "geografia":
        geografiaZw = True
    else:
        print("Wpisałeś złą nazwę przedmiotu, wpisz nazwę lub 'stop': ")
print()
zatrzymaj = "x"
while zatrzymaj != "stop":
    zatrzymaj = input("Z jakiego przedmiotu chcesz dopisać ocenę? wpisz nazwę lub 'stop': ")
    if zatrzymaj == "stop":
        break
    elif zatrzymaj == "polski":
        if polskiZw == False:
            ocenaPol = int(input("Wpisz ocenę: "))
            polski.append(ocenaPol)
            liczbaOcenPolski += 1
            sumaPolski += ocenaPol
            sredniaPol = sumaPolski / liczbaOcenPolski
        else:
            print("Jesteś zwolniony z polskiego!")
    elif zatrzymaj == "matematyka":
        if matematykaZw == False:
            ocenaMat = int(input("Wpisz ocenę: "))
            matematyka.append(ocenaMat)
            liczbaOcenMatematyka += 1
            sumaMatematyka += ocenaMat
            sredniaMat = sumaMatematyka / liczbaOcenMatematyka
        else:
            print("Jesteś zwolniony z matematyki!")
    elif zatrzymaj == "angielski":
        if angielskiZw == False:
            ocenaAng = int(input("Wpisz ocenę: "))
            angielski.append(ocenaAng)
            liczbaOcenAngielski += 1
            sumaAngielski += ocenaAng
            sredniaAng = sumaAngielski / liczbaOcenAngielski
        else:
            print("Jesteś zwolniony z angielskiego!")
    elif zatrzymaj == "wf":
        if wfZw == False:
            ocenaWf = int(input("Wpisz ocenę: "))
            wf.append(ocenaWf)
            liczbaOcenWf += 1
            sumaWf += ocenaWf
            sredniaWf = sumaWf / liczbaOcenWf
        else:
            print("Jesteś zwolniony z wf!")
    elif zatrzymaj == "religia":
        if religiaZw == False:
            ocenaRel = int(input("Wpisz ocenę: "))
            religia.append(ocenaRel)
            liczbaOcenReligia += 1
            sumaReligia += ocenaRel
            sredniaRel = sumaReligia / liczbaOcenReligia
        else:
            print("Jesteś zwolniony z religii!")
    elif zatrzymaj == "historia":
        if historiaZw == False:
            ocenaHis = int(input("Wpisz ocenę: "))
            historia.append(ocenaHis)
            liczbaOcenHistoria += 1
            sumaHistoria += ocenaHis
            sredniaHis = sumaHistoria / liczbaOcenHistoria
        else:
            print("Jesteś zwolniony z historii!")
    elif zatrzymaj == "geografia":
        if geografiaZw == False:
           ocenaGeo = int(input("Wpisz ocenę: "))
           geografia.append(ocenaGeo)
           liczbaOcenGeografia += 1
           sumaGeografia += ocenaGeo
           sredniaGeo = sumaGeografia / liczbaOcenGeografia
        else:
            print("Jesteś zwolniony z geografii!")
    else:
        print("Wpisałeś złą nazwę przedmiotu!")
print()
liczbaWszystkich = liczbaOcenPolski + liczbaOcenMatematyka + liczbaOcenAngielski + liczbaOcenWf + liczbaOcenReligia + liczbaOcenHistoria + liczbaOcenGeografia
sumaWszystkich = sumaPolski + sumaMatematyka + sumaAngielski + sumaWf + sumaReligia + sumaHistoria + sumaGeografia
sredniaWszystkich = sumaWszystkich / liczbaWszystkich
print("Oto lista ocen i ich podsumowanie: ")
print()
if polskiZw == False:
    polski.sort()
    print(f"polski: {polski}")
    print(f"Liczba ocen z polskiego: {liczbaOcenPolski}")
    print(f"Suma ocen z polskiego: {sumaPolski}")
    print(f"Średnia ocen z polskiego: {sredniaPol}")
    print()
else:
    clear = 0

if matematykaZw == False:
    matematyka.sort()
    print(f"matematyka: {matematyka}")
    print(f"Liczba ocen z matematyki: {liczbaOcenMatematyka}")
    print(f"Suma ocen z matematyki: {sumaMatematyka}")
    print(f"Średnia ocen z matematyki: {sredniaMat}")
    print()
else:
    clear = 0

if angielskiZw == False:
    angielski.sort()
    print(f"angielski: {angielski}")
    print(f"Liczba ocen z angielskiego: {liczbaOcenAngielski}")
    print(f"Suma ocen z angielskiego: {sumaAngielski}")
    print(f"Średnia ocen z angielskiego: {sredniaAng}")
    print()
else:
    clear = 0

if wfZw == False:
    wf.sort()
    print(f"WF: {wf}")
    print(f"Liczba ocen z WF: {liczbaOcenWf}")
    print(f"Suma ocen z WF: {sumaWf}")
    print(f"Średnia ocen z WF: {sredniaWf}")
    print()
else:
    clear = 0

if religiaZw == False:
    religia.sort()
    print(f"religia: {religia}")
    print(f"Liczba ocen z religii: {liczbaOcenReligia}")
    print(f"Suma ocen z religii: {sumaReligia}")
    print(f"Średnia ocen z religii: {sredniaRel}")
    print()
else:
    clear = 0

if historiaZw == False:
    historia.sort()
    print(f"historia: {historia}")
    print(f"Liczba ocen z historii: {liczbaOcenHistoria}")
    print(f"Suma ocen z historii: {sumaHistoria}")
    print(f"Średnia ocen z historii: {sredniaHis}")
    print()
else:
    clear = 0

if geografiaZw == False:
    geografia.sort()
    print(f"geografia: {geografia}")
    print(f"Liczba ocen z geografii: {liczbaOcenGeografia}")
    print(f"Suma ocen z geografii: {sumaGeografia}")
    print(f"Średnia ocen z geografii: {sredniaGeo}")
    print()
else:
    clear = 0
print()
print(f"Liczba wszystkich ocen: {liczbaWszystkich}")
print(f"Suma wszystkich ocen: {sumaWszystkich}")
print(f"Średnia wszystkich ocen: {sredniaWszystkich}")

