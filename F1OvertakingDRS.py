#Program sprawdza czy nastąpi wyprzedzanie przy użyciu DRS.
#Autor - Mateusz Szynalik

print("Program ma za zadanie oszacować czy nastąpi wyprzedzanie pomiędzy dwoma bolidami F1 na prostej przy użyciu systemu DRS.")
dl_prostej = int(input("Podaj długość prostej w metrach: "))
predkosc1 = int(input("Podaj prędkość 1. samochodu na linii DRS w km/h: "))
predkosc2 = int(input("Podaj prędkość 2. samochodu na linii DRS w km/h: "))
odleglosc = int(input("Podaj odległość między samochodami w metrach: "))

if dl_prostej < 300:
    predkosc2 = predkosc2 * 1.04
elif dl_prostej < 600:
    predkosc2 = predkosc2 * 1.07
elif dl_prostej < 1000:
    predkosc2 = predkosc2 * 1.1

predkosc1_w_ms = predkosc1 * 1000 / 3600
predkosc2_w_ms = predkosc2 * 1000 / 3600
czasPrzejazdu1 = (dl_prostej - odleglosc) / predkosc1_w_ms
czasPrzejazdu2 = dl_prostej / predkosc2_w_ms
roznica = 0

if czasPrzejazdu1 < czasPrzejazdu2:
    print(f"Samochód nr 1 utrzyma pozycję.")
    roznica = round(czasPrzejazdu2 - czasPrzejazdu1, 2)
    print(f"Przewaga samochodu 1. po prostej wynosi: {roznica} s.")
elif czasPrzejazdu1 > czasPrzejazdu2:
    print(f"Samochód nr 2 wyprzedzi samochód nr 1. ")
    roznica = round(czasPrzejazdu1 - czasPrzejazdu2, 2)
    print(f"Przewaga samochodu 2. po prostej wynosi: {roznica} s.")
else:
    print(f"Samochody zrównają się.")