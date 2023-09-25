'''Kérjünk be egy hőmérséklet értéket a felhasználótól Celsiusban!
És ellenőrizzük a hőmérsékletet és adjunk a program válaszoljon rá! Adjon meg válaszokat a Hőmérséklettől függően!'''

hofok = float(input("Adja meg a jelenlegi hőmérsékletet: "))

if hofok < 0:
    print("Hideg idő van.")
elif hofok >= 0 and hofok <= 25:
    print("Meleg idő van. Tökéletes az idő egy kirándulásra! ")
else:
    print("Forró nyári idő van.")