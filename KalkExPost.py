#Autor - Mateusz Szynalik
#Program służy do kalkulacji ex post kosztów projektu

import datetime

projekt = "A"
metodaKalkulacji = "ex post"
osobaAkceptujaca = "XYZ"
danePoprzednichProjektow = "nie"
liczbaZdarzenNiepozadanych = 2
przewidywanyKosztMaterialow = 10000
przewidywanyKosztWynagrodzen = 5000
przewidywanyKosztMaszyn = 2000
przewidywanykosztInne = 1000
przewidywanaSumaKosztowBezZdarzen = 18000
przewidywanaSumaZdarzenie1 = 18500
przewidywanaSumaZdarzenie2 = 19000
przewidywanaSumaZdarzenie12 = 19500
przewidywanaDataZakonczeniaBezZdarzen = datetime.date(year=2021, month=7, day=25)
przewidywanaDataZakonczeniaZdarzenie1 = przewidywanaDataZakonczeniaBezZdarzen + datetime.timedelta(days=10)
przewidywanaDataZakonczeniaZdarzenie2 = przewidywanaDataZakonczeniaBezZdarzen + datetime.timedelta(days=5)
przewidywanaDataZakonczeniaZdarzenia12 = przewidywanaDataZakonczeniaBezZdarzen + datetime.timedelta(days=15)

print()
print("W celu kalkulacji kosztów projektu metodą ex post, podążaj zgodnie z instrukcją i wprowadź dane, o które zostaniesz poproszony. Wprowadzaj wyłącznie liczby naturalne lub '0'.")
print()
print("Informacje na temat projektu, które wprowadziłeś na etapie kalkulacji ex ante:")
print()
print(f"Projekt: {projekt} \nDane z poprzednich projektów: {danePoprzednichProjektow} \nOsoba akceptująca wyniki kalkulacji: {osobaAkceptujaca} \nLiczba zdarzeń niepożądanych: {liczbaZdarzenNiepozadanych} \nPrzewidywany koszt Materialow: {przewidywanyKosztMaterialow}zł \nPrzewidywany koszt wynagrodzeń: {przewidywanyKosztWynagrodzen}zł \nPrzewidywany koszt zużycia maszyn: {przewidywanyKosztMaszyn}zł \nPrzewidywana suma innych kosztów: {przewidywanykosztInne}zł \nPrzewidywana suma kosztów bez wystąpienia zdarzeń niepożądanych: {przewidywanaSumaKosztowBezZdarzen}zł \nPrzewidywana suma kosztów przy wystąpieniu 1. zdarzenia niepożadanego: {przewidywanaSumaZdarzenie1}zł \nPrzewidywana suma kosztów przy wystąpieniu 2. zdarzenia niepożądanego: {przewidywanaSumaZdarzenie2}zł \nPrzewidywana suma kosztów przy wystąpieniu wszystkich zdarzeń niepożądanych: {przewidywanaSumaZdarzenie12}zł")
print()
print("Wprowadź dane na temat poniesionych kosztów: ")
kosztMaterialow = int(input("Podaj (w pełnych zł.) sumę kosztów zużycia materiałów poniesionych w procesie realizacji projektu: "))
kosztWynagrodzen = int(input("Podaj (w pełnych zł.) sumę kosztów wynagrodzeń poniesionych w procesie realizacji projektu: "))
kosztMaszyn = int(input("Podaj (w pełnych zł.) sumę kosztów zużycia maszyn poniesionych w procesie realizacji projektu: "))
kosztInne = int(input("Podaj (w pełnych zł.) sumę innych kosztów poniesionych w procesie realizacji projektu: "))
if kosztMaterialow < 0 or kosztWynagrodzen < 0 or kosztMaszyn < 0 or kosztInne < 0:
    print("Wprowadziłeś ujemną wartość jednego lub kilku parametrów. Uruchom ponownie program i wprowadź nieujemne dane.")
else:
    sumaKosztowBezZdarzen = kosztMaterialow + kosztWynagrodzen + kosztMaszyn + kosztInne
    strukturaMaterialow = 0
    strukturaWynagrodzen = 0
    strukturaMaszyn = 0
    strukturaInne = 0
    strukturaZdarzenie1 = 0
    strukturaZdarzenie2 = 0
    odchylenieKosztow = 0

    liczbaZdarzen = int(input("Podaj liczbę zdarzeń niepożądanych, które wystąpiły w trakcie projektu. żaden - 0, tylko pierwsze - 1, tylko drugie - 2, oba - 12: "))
    if liczbaZdarzen == 0:
        kosztProjektu = sumaKosztowBezZdarzen
        strukturaMaterialow = kosztMaterialow / kosztProjektu * 100
        strukturaWynagrodzen = kosztWynagrodzen / kosztProjektu * 100
        strukturaMaszyn = kosztMaszyn / kosztProjektu * 100
        strukturaInne = kosztInne / kosztProjektu * 100
        print()
        struktura = print(f"Struktura kosztów projektu: \nKoszt zużytych materiałów: {strukturaMaterialow}%. \nKoszty Wynagrodzeń: {strukturaWynagrodzen}%. \nKoszty zużycia maszyn: {strukturaMaszyn}%. \nInne koszty: {strukturaInne}%.")
        odchylenieKosztow = kosztProjektu - przewidywanaSumaKosztowBezZdarzen
    elif liczbaZdarzen == 1:
        kosztZdarzenie1 = int(input("Podaj (w pełnych zł.) koszt wystąpienia 1. zdarzenia niepożądanego: "))
        if kosztZdarzenie1 < 0:
            print("Wprowadziłeś ujemną wartość jednego lub kilku parametrów. Uruchom ponownie program i wprowadź nieujemne dane.")
        else:
            kosztProjektu = sumaKosztowBezZdarzen + kosztZdarzenie1
            strukturaMaterialow = kosztMaterialow / kosztProjektu * 100
            strukturaWynagrodzen = kosztWynagrodzen / kosztProjektu * 100
            strukturaMaszyn = kosztMaszyn / kosztProjektu * 100
            strukturaInne = kosztInne / kosztProjektu * 100
            strukturaZdarzenie1 = kosztZdarzenie1 / kosztProjektu * 100
            print()
            struktura = print(f"Struktura kosztów projektu: \nKoszt zużytych materiałów: {strukturaMaterialow}%. \nKoszty Wynagrodzeń: {strukturaWynagrodzen}%. \nKoszty zużycia maszyn: {strukturaMaszyn}%. \nInne koszty: {strukturaInne}%. \nKoszty wystąpienia 1. zdarzenia niepożądanego: {strukturaZdarzenie1}%.")
            odchylenieKosztow = kosztProjektu - przewidywanaSumaZdarzenie1
    elif liczbaZdarzen == 2:
        kosztZdarzenie2 = int(input("Podaj (w pełnych zł.) koszt wystąpienia 2. zdarzenia niepożądanego: "))
        if kosztZdarzenie2 < 0:
            print("Wprowadziłeś ujemną wartość jednego lub kilku parametrów. Uruchom ponownie program i wprowadź nieujemne dane.")
        else:
            kosztProjektu = sumaKosztowBezZdarzen + kosztZdarzenie2
            strukturaMaterialow = kosztMaterialow / kosztProjektu * 100
            strukturaWynagrodzen = kosztWynagrodzen / kosztProjektu * 100
            strukturaMaszyn = kosztMaszyn / kosztProjektu * 100
            strukturaInne = kosztInne / kosztProjektu * 100
            strukturaZdarzenie2 = kosztZdarzenie2 / kosztProjektu * 100
            print()
            struktura = print(f"Struktura kosztów projektu: \nKoszt zużytych materiałów: {strukturaMaterialow}%. \nKoszty Wynagrodzeń: {strukturaWynagrodzen}%. \nKoszty zużycia maszyn: {strukturaMaszyn}%. Inne koszty: {strukturaInne}%. \nKoszty wystąpienia 2. zdarzenia niepożądanego: {strukturaZdarzenie2}%.")
            odchylenieKosztow = kosztProjektu - przewidywanaSumaZdarzenie2
    elif liczbaZdarzen == 12:
        kosztZdarzenie1 = int(input("Podaj (w pełnych zł.) koszt wystąpienia 1. zdarzenia niepożądanego: "))
        kosztZdarzenie2 = int(input("Podaj (w pełnych zł.) koszt wystąpienia 2. zdarzenia niepożądanego: "))
        if kosztZdarzenie1 < 0 or kosztZdarzenie2 < 0:
            print("Wprowadziłeś ujemną wartość jednego lub kilku parametrów. Uruchom ponownie program i wprowadź nieujemne dane.")
        else:
            kosztProjektu = sumaKosztowBezZdarzen + kosztZdarzenie1 + kosztZdarzenie2
            strukturaMaterialow = kosztMaterialow / kosztProjektu * 100
            strukturaWynagrodzen = kosztWynagrodzen / kosztProjektu * 100
            strukturaMaszyn = kosztMaszyn / kosztProjektu * 100
            strukturaInne = kosztInne / kosztProjektu * 100
            strukturaZdarzenie1 = kosztZdarzenie1 / kosztProjektu * 100
            strukturaZdarzenie2 = kosztZdarzenie2 / kosztProjektu * 100
            print()
            struktura = print(f"Struktura kosztów projektu: \nKoszt zużytych materiałów: {strukturaMaterialow}%. \nKoszty Wynagrodzeń: {strukturaWynagrodzen}%. \nKoszty zużycia maszyn: {strukturaMaszyn}%. \nInne koszty: {strukturaInne}%. \nKoszty wystąpienia 1. zdarzenia niepożądanego: {strukturaZdarzenie1}%. \nKoszty wystąpienia 2. zdarzenia niepożądanego: {strukturaZdarzenie2}%.")
            odchylenieKosztow = kosztProjektu - przewidywanaSumaZdarzenie12
    else:
        print("Wprowadziłeś błędną liczbę zdarzeń niepożądanych. Uruchom ponownie program i wprowadź prawidłowe dane.")



    print()
    print("Wprowadź datę zakończenia projektu")
    rok = int(input("Rok zakończenia projektu: "))
    miesiac = int(input("Miesiąc zakończenia projektu (styczeń - 1, luty - 2...): "))
    dzien = int(input("Dzień zakończenia projektu (1 - 31): "))
    komunikatData = "Wprowadziłeś błędną datę. Uruchom ponownie program i wprowadź poprawną datę."
    if miesiac == 1 or miesiac == 3 or miesiac == 5 or miesiac == 7 or miesiac == 8 or miesiac == 10 or miesiac == 12:
        if dzien >= 1 and dzien <= 31:
            dataZakonczenia = datetime.date(year=rok, month=miesiac, day=dzien)

        else:
            print(komunikatData)
    elif miesiac == 4 or miesiac == 6 or miesiac == 9 or miesiac == 11:
        if dzien >= 1 and dzien <= 30:
            dataZakonczenia = datetime.date(year=rok, month=miesiac, day=dzien)

        else:
            print(komunikatData)
    elif miesiac == 2:
        if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0) and dzien >= 1 and dzien <= 29:
            dataZakonczenia = datetime.date(year=rok, month=miesiac, day=dzien)

        elif dzien >= 1 and dzien <= 28:
            dataZakonczenia = datetime.date(year=rok, month=miesiac, day=dzien)

        else:
            print(komunikatData)
    else:
        print(komunikatData)

    if liczbaZdarzen == 0 and dataZakonczenia > przewidywanaDataZakonczeniaBezZdarzen:
        komunikat = print(f"Data zakończenia projektu: {dataZakonczenia}. Projekt zakończył się później niż planowano ({przewidywanaDataZakonczeniaBezZdarzen}).")
    elif liczbaZdarzen == 0 and dataZakonczenia < przewidywanaDataZakonczeniaBezZdarzen:
        komunikat = print(f"Data zakończenia projektu: {dataZakonczenia}. Projekt zakończył się wcześniej niż planowano ({przewidywanaDataZakonczeniaBezZdarzen}).")
    elif liczbaZdarzen == 0 and dataZakonczenia == przewidywanaDataZakonczeniaBezZdarzen:
        komunikat = print(f"Data zakończenia projektu: {dataZakonczenia}. Projekt zakończył się w planowanym terminie ({przewidywanaDataZakonczeniaBezZdarzen}).")
    elif liczbaZdarzen == 1 and dataZakonczenia > przewidywanaDataZakonczeniaZdarzenie1:
        komunikat = print(f"Data zakończenia projektu: {dataZakonczenia}. Projekt zakończył się później niż planowano ({przewidywanaDataZakonczeniaZdarzenie1}).")
    elif liczbaZdarzen == 1 and dataZakonczenia < przewidywanaDataZakonczeniaZdarzenie1:
        komunikat = print(f"Data zakończenia projektu: {dataZakonczenia}. Projekt zakończył się wcześniej niż planowano ({przewidywanaDataZakonczeniaZdarzenie1}).")
    elif liczbaZdarzen == 1 and dataZakonczenia == przewidywanaDataZakonczeniaZdarzenie1:
        komunikat = print(f"Data zakończenia projektu: {dataZakonczenia}. Projekt zakończył się w planowanym terminie ({przewidywanaDataZakonczeniaZdarzenie1}).")
    elif liczbaZdarzen == 2 and dataZakonczenia > przewidywanaDataZakonczeniaZdarzenie2:
        komunikat = print(f"Data zakończenia projektu: {dataZakonczenia}. Projekt zakończył się później niż planowano ({przewidywanaDataZakonczeniaZdarzenie2}).")
    elif liczbaZdarzen == 2 and dataZakonczenia < przewidywanaDataZakonczeniaZdarzenie2:
        komunikat = print(f"Data zakończenia projektu: {dataZakonczenia}. Projekt zakończył się wcześniej niż planowano ({przewidywanaDataZakonczeniaZdarzenie2}).")
    elif liczbaZdarzen == 2 and dataZakonczenia == przewidywanaDataZakonczeniaZdarzenie2:
        komunikat = print(f"Data zakończenia projektu: {dataZakonczenia}. Projekt zakończył się w planowanym terminie ({przewidywanaDataZakonczeniaZdarzenie2}).")
    elif liczbaZdarzen == 12 and dataZakonczenia > przewidywanaDataZakonczeniaZdarzenia12:
        komunikat = print(f"Data zakończenia projektu: {dataZakonczenia}. Projekt zakończył się później niż planowano ({przewidywanaDataZakonczeniaZdarzenia12}).")
    elif liczbaZdarzen == 12 and dataZakonczenia < przewidywanaDataZakonczeniaZdarzenia12:
        komunikat = print(f"Data zakończenia projektu: {dataZakonczenia}. Projekt zakończył się wcześniej niż planowano ({przewidywanaDataZakonczeniaZdarzenia12}).")
    elif liczbaZdarzen == 12 and dataZakonczenia == przewidywanaDataZakonczeniaZdarzenia12:
        komunikat = print(f"Data zakończenia projektu: {dataZakonczenia}. Projekt zakończył się w planowanym terminie ({przewidywanaDataZakonczeniaZdarzenia12}).")

    print()
    print(f"Podsumowanie danych na temat zakończonego projektu: \nSuma poniesionych kosztów: {kosztProjektu}zł. \nOdchylenie sumy kosztów faktycznie poniesionych od wielkości planowanych kosztów - {odchylenieKosztow}zł.")

