def delení(delitel, jmenovatel):
    if jmenovatel != 0:
        vysledek = delitel/jmenovatel
        return vysledek
    else:
        print("Nelze dělit nulou")

x = int(input("Zadejte proměnnou a:"))
y = int(input("Zadejte proměnnou b:"))

print("Výsledek je: ", deleni(x,y))