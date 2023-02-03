import random

'''II/A, B, C:
           	23; 46; 10; 1; 6
II/D, E:
           	Az egyjegyűek száma : 2.  	
A szamok.txt tartalma:
II/F:
A fejek száma: 2. 	
 
    A. Írasson ki a konzolra kötőjellel (-) elválasztva 5 lottószámot véletlen számsorozat alapján a mintának megfelelően! (4p)
    B. A generált értékeket tárolja lista adatszerkezetben! (1p)
    C. A „;” jel csak az értékek között szerepeljen (a végén ne)! (2p)
    D. Írjon függvényt egyjegyuek_szama néven, amiben számolja meg, hogy hány olyan elem van, ami egyjegyű (1). 
    A visszatérési érték legyen egy egész szám! (3p)
    E. A egyjegyuek _szama függvény eredményét írassa ki a mintának megfelelően a konzolra, 
    amit konzol_kiir nevű metódusban fogalmazzon meg! (2p)
    F. A egyjegyuek _szama függvény eredményét írassa ki a mintának megfelelően a szamok.txt nevű fájlba, 
    amit file_kiir nevű metódusban fogalmazzon meg! (2p)'''

def otos_szamsor(): #listát ad vissza
    i = 0
    szamsor =[]
    while i < 5:
        szamsor.append(int(random.random()*98+1))
        i += 1
    return szamsor


def kiir(lista):
    cv = 0
    szoveg = ""
    szoveg2 = ""
    while cv < len(lista)-1:
        szoveg += str(lista[cv]) + "-"
        cv += 1
    szoveg += str(lista[cv])
    print(szoveg)
    cv2 = 0
    while cv2 < len(lista)-1:
        szoveg2 += str(lista[cv2]) + ";"
        cv2 +=1
    szoveg2 += str(lista[cv2])
    print("II/A, B, C:")
    print(szoveg2)


def egyjegyuek_szama(lista): #darabszámot ad vissza
    i = 0
    darab = 0
    while i < len(lista):
        if lista[i] < 10 and lista[i] > 0:
            darab += 1
            i +=1
        else:
            i += 1
    return darab

def konzol_kiir(egyjegyu):
    print("II/D, E:")
    print(f"Az egyjegyűek száma: {egyjegyu}")


def file_kiir(filename, darab):
    file = open(filename, "w", encoding="UTF-8")
    file.write("II/D, E:\n")
    file.write(f"Az egyjegyűek száma: {darab}")






