eletkor = int(input("Kérem, adja meg az életkorát: "))

# Életkor kategória megállapítása
if eletkor < 0:
    kategoria = "Még nem születtél meg"
elif eletkor < 5:
    kategoria = "Még nem jársz általános iskolába"
elif eletkor < 14:
    kategoria = "általános iskolába jársz"
elif eletkor < 64:
    kategoria = "tanulsz vagy dolgozol"
elif eletkor < 65: 
    