import random

eingaben = []
gueltig = range(1, 50)

while len(eingaben) < 6:
    eingabe = int(input(f"Bitte geben sie Zahl {len(eingaben)+1} von 6 an: "))

    if eingabe in eingaben or eingabe not in gueltig:
        print("Ungültige Eingabe, bitte probieren Sie es nochmal.")
    else:
        eingaben.append(eingabe)

print("Ihre Eingaben: " + str(eingaben))

lotto_zahlen = []

while len(lotto_zahlen) < 6:
    rand = random.randrange(1, 50)
    if rand not in lotto_zahlen:
        lotto_zahlen.append(rand)

print("Die Lottozahlen: " + str(lotto_zahlen))

correct = 0
for element in eingaben:
    if element in lotto_zahlen:
        correct += 1

print("Anzahl Richtige: " + str(correct))
