from AAutom import Autom


'''Az auto.txt forrásállomány, autók adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
Készítsen programot autom.py néven. Olvassa be auto.txt fájlból az auto adatait, tároljaAuto osztály típusú kocsi nevű listában
 a példányokat.
A megoldás mintája:
III/Flotta:
Autók száma: 7.
III/Legfiatalabb
A legfiatalabb autó: Seat Ibiza(2011))

    A. Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a auto.txt fájlból a autók adatait, és
    tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra,
    hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
    B. Készíts függvényt flotta néven, amely visszaadja az autók számát a mintának megfelelően,
    majd írasd ki  a konzolra a mintának megfelelően! (2p)
    C. Add meg az legfiatalabb autó nevét a mintának megfelelően a konzolra írva!! (4p)
    D. Írassa ki konzolra a mintának megfelelően a legöregebb épület
    (ha több is van, akkor az első legöregebb adatait) országát. (4p)'''
auto_lista = []

def fajl_beolvas():
    fajl = open("auto.txt", "r", encoding="utf-8")
    fajl.readline()
    sorok = fajl.readlines()
    fajl.close()

    cv = 0
    while cv < len(sorok):
        sor = sorok[cv].strip().split("$")
        auto_lista.append(Autom(sor))
        cv += 1
    return auto_lista

def flotta(lista):
    print("III/Flotta:")
    print(f"Autók száma: {len(auto_lista)}")

def legfiatalabb(lista):
    i = 0
    minimum_elem = auto_lista[0].gyartasi_ev
    minimum_index = 0
    while i < len(auto_lista):
        if minimum_elem > auto_lista[i].gyartasi_ev:
            minimum_elem = auto_lista[i].gyartasi_ev
            minimum_index = i
            i +=1
        else:
            i += 1
    print("III/Legfiatalabb")
    print(f"A legfiatalabb autó: {auto_lista[minimum_index].nev}({auto_lista[minimum_index].gyartasi_ev}))")


