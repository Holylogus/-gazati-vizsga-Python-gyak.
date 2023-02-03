import datetime

'''I/A:
Autó  neve: Opel Corsa
Gyártási dátum: 2022
 
I/B:
Ez az Opel Corsa átlagos korú.
    A. Kérje be az alábbi adatokat a fenti mintának megfelelően:
Autó  neve és gyártás éve! (2p)
    B. A program az adatbekérés után írasson ki egy szöveget az alábbiak alapján!
Amennyiben az autó gyártási éve ez évi, akkor írja ki, „friss gyártás”.
 Amennyiben 2000 előtt gyártották az autót, írja ki: „öreg autó”
Minden más esetben: „Átlagos korú”. (4p)
A mintának megfelelően jelenítette meg az eredményt, és kérte be az adatokat. (1p)'''

def auto_kor():
    auto_nev = input("Adja meg az autó nevét: ")
    gyartasi_ev = int(input("Adja meg az autó gyártási évét: "))
    date = datetime.datetime.now()

    print("I/A:")
    print(f"Autó  neve: {auto_nev}")
    print(f"Gyártási dátum: {gyartasi_ev}")

    print("I/B:")
    if gyartasi_ev == date.year:
        print(f"Ez az {auto_nev} friss gyártás")
    elif gyartasi_ev < 2000:
        print(f"Ez az {auto_nev} öreg autó")
    else:
        print(f"Ez az {auto_nev} Átalgos korú")




