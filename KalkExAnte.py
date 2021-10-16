#Autor - Mateusz Szynalik
#Program służy do kalkulacji ex ante kosztów projektu

import datetime

projekt = "A"
metodaKalkulacji = "ex ante"
danePoprzednichProjektow = "nie"
liczbaZdarzenNiepozadanych = 2
osobaAkceptujaca = "XYZ"
dataZakonczenia = datetime.date(year=2021, month=7, day=25)

print()
print("W celu kalkulacji kosztów projektu metodą ex ante, podążaj zgodnie z instrukcją i wprowadź dane, o które zostaniesz poproszony. Wprowadzaj wyłącznie liczby naturalne lub '0'.")
print()
print("Informacje na temat projektu, które wprowadziłeś w zakładce Kalkuluj koszty projektu:")
print()
print(f"Projekt: {projekt} \nMetoda kalkulacji: {metodaKalkulacji} \nDane z poprzednich projektów: {danePoprzednichProjektow} \nLiczba zdarzeń niepożądanych: {liczbaZdarzenNiepozadanych} \nOsoba akceptująca wyniki kalkulacji: {osobaAkceptujaca} \nPrzewidywany termin zakończenia projektu: {dataZakonczenia}")
print()
print()

kosztMaterialow = int(input("Podaj przewidywany koszt (w zł) zużycia materiałów w trakcie projektu: "))
kosztWynagrodzen = int(input("Podaj przewidywany koszt (w zł) wynagrodzeń członków zespołu projektowego: "))
kosztMaszyn = int(input("Podaj przewidywany koszt (w zł) zużycia maszyn i urządzeń: "))
kosztInne = int(input("Podaj przewidywaną wartość (w zł) innych, nieujętych w poprzednich zapytaniach kosztów: "))
Zdarzenie1 = int(input("Podaj przewidywany koszt (w zł) wystąpienia 1. zdarzenia niepożądanego: "))
Zdarzenie1Szansa = int(input("Podaj, wyrażoną w procentach, szansę na wystąpienie 1. zdarzenia niepożądanego: "))
Zdarzenie1Dni = int(input("Szacowana liczba dni opóźnienia prac ze względu na wystąpienie 1. zdarzenia niepożądanego: "))
Zdarzenie2 = int(input("Podaj przewidywany koszt (w zł) wystąpienia 2. zdarzenia niepożądanego: "))
Zdarzenie2Szansa = int(input("Podaj, wyrażoną w procentach, szansę na wystąpienie 2. zdarzenia niepożądanego: "))
Zdarzenie2Dni = int(input("Szacowana liczba dni opóźnienia prac ze względu na wystąpienie 2. zdarzenia niepożądanego: "))

sumaKosztowBezZdarzen = kosztMaterialow + kosztWynagrodzen + kosztMaszyn + kosztInne
kosztZdarzenie1 = Zdarzenie1 * (Zdarzenie1Szansa/100)
sumaKosztowZdarzenie1 = sumaKosztowBezZdarzen + kosztZdarzenie1
kosztZdarzenie2 = Zdarzenie2 * (Zdarzenie2Szansa/100)
sumaKosztowZdarzenie2 = sumaKosztowBezZdarzen + kosztZdarzenie2
sumaKosztowZdarzenie12 = sumaKosztowBezZdarzen + kosztZdarzenie1 + kosztZdarzenie2
sumaKosztZdarzenie1 = sumaKosztowBezZdarzen + Zdarzenie1
sumaKosztZdarzenie2 = sumaKosztowBezZdarzen + Zdarzenie2
sumaKosztZdarzenie12 = sumaKosztowBezZdarzen + Zdarzenie1 + Zdarzenie2
koniec1 = dataZakonczenia + datetime.timedelta(days=Zdarzenie1Dni)
koniec2 = dataZakonczenia + datetime.timedelta(days=Zdarzenie2Dni)
koniec12 = dataZakonczenia + datetime.timedelta(days=(Zdarzenie1Dni + Zdarzenie2Dni))
strukturaMaterialy = kosztMaterialow / sumaKosztowBezZdarzen * 100
strukturaWynagrodzenia = kosztWynagrodzen / sumaKosztowBezZdarzen * 100
strukturaMaszyny = kosztMaszyn / sumaKosztowBezZdarzen * 100
strukturaInne = kosztInne / sumaKosztowBezZdarzen * 100
print()
if kosztMaterialow < 0 or kosztWynagrodzen < 0 or kosztMaszyn < 0 or kosztInne < 0 or Zdarzenie1 < 0 or Zdarzenie1Szansa < 0 or Zdarzenie1Dni < 0 or Zdarzenie2 < 0 or Zdarzenie2Szansa < 0 or Zdarzenie2Dni < 0:
    if Zdarzenie1Szansa >= 100 or Zdarzenie2Szansa >= 100:
        print("Prawdopodobieństwo wystąpienia zdarzenia niepożądanego nie może być większe lub równe 100 procent. Uruchom ponownie program i wprowadź poprawne dane.")
    else:
        print("Wprowadziłeś ujemną wartość jednego lub kilku parametrów. Uruchom ponownie program i wprowadź nieujemne dane.")
else:
    if Zdarzenie1Szansa >= 100 or Zdarzenie2Szansa >= 100:
        print("Prawdopodobieństwo wystąpienia zdarzenia niepożądanego nie może być większe lub równe 100 procent. Uruchom ponownie program i wprowadź poprawne dane.")
    else:
        print()
        print("Wyniki procesu kalkulacji: ")
        print(f"Przewidywana suma kosztów projektu bez wystąpienia zdarzeń niepożądanych: {sumaKosztowBezZdarzen}zł \nPrzewidywana suma kosztów projektu z uwzględnieniem prawdopodobieństwa wystąpienia 1. zdarzenia niepożądanego: {sumaKosztowZdarzenie1}zł \nPrzewidywana suma kosztów projektu z uwzględnieniem prawdopodobieństwa wystąpienia 2. zdarzenia niepożądanego: {sumaKosztowZdarzenie2}zł \nPrzewidywana suma kosztów projektu z uwzględnieniem prawodopodobieństwa wystąpienia obu zdarzeń niepożądanych: {sumaKosztowZdarzenie12}zł \nPrzewidywana suma kosztów projektu przy wystąpieniu 1. zdarzenia niepożądanego: {sumaKosztZdarzenie1}zł \nPrzewidywana suma kosztów projektu przy wystąpieniu 2. zdarzenia niepożądanego: {sumaKosztZdarzenie2}zł \nPrzewidywana suma kosztów projektu przy wystąpieniu wszystkich zdarzeń niepożądanych: {sumaKosztZdarzenie12}zł \n\nPrzewidywany termin ukończenia prac: {dataZakonczenia} \nPrzewidywany termin ukończenia prac przy wystąpieniu 1. zdarzenia niepożądanego: {koniec1} \nPrzewidywany termin ukończenia prac przy wystąpieniu 2. zdarzenia niepożądanego: {koniec2} \nPrzewidywany termin ukończenia prac przy wystąpieniu wszystkich zdarzeń niepożądanych: {koniec12} \n\nStruktura kosztów przy braku wystąpienia zdarzeń niepożądanych: \nZużycie materiałów: {strukturaMaterialy}% \nKoszty wynagrodzeń: {strukturaWynagrodzenia}% \nZużycie maszyn: {strukturaMaszyny}% \nInne koszty: {strukturaInne}%")




