'''Kérjünk be egy számot, majd ellenőrrizzük hogy az adott szám pozitív vagy negatív illetve páros vagy páratlan szám-e! '''

szam = float(input("Kérem, adjon meg egy számot: "))

if szam > 0:
    print("A megadott szám pozitív.")
elif szam < 0:
    print("A megadott szám negatív.")
else:
    print("A megadott szám nulla.")


paros_szamok = 0 
paratlan_szamok = 0
if szam % 2 == 0:
            paros_szamok += 1
            print("A szám páros!")
else:
    print("A szám páratlan!")