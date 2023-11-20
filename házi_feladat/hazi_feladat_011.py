#hazi_feladat_011

"""
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal!
Az #összehasonlítás eredményéről tájékoztassa a felhasználót!
"""

import random

generaltszam = random.randint(1, 3)

szam = int(input("Adjon meg egy számot (1-3 között): "))

if szam == generaltszam:
    print(f"A Tipped helyes volt! {szam} ({generaltszam})")
else:
    print(f"A tipped rossz volt! {szam} ({generaltszam})2")
