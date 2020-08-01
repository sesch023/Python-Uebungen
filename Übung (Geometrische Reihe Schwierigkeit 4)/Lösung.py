summe = 0.0
vorherige_summe = None
index = 1

while summe != vorherige_summe:
    vorherige_summe = summe
    summe += 2**-index

    index += 1

print("Ergebnis: " + str(summe))
