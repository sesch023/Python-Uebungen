import random

zahl = random.randrange(0, 101)
fehler = 0
limit = 10

while fehler < limit:
    print(f"Fehler: {fehler} von {limit}")
    eingabe = int(input("Bitte erraten Sie eine Zahl zwischen 0 und 100: "))

    if eingabe < zahl:
        print("Eingabe ist zu klein!")
        fehler += 1
    elif eingabe > zahl:
        print("Eingabe ist zu groß!")
        fehler += 1
    else:
        print("Sie haben gewonnen!")
        break
