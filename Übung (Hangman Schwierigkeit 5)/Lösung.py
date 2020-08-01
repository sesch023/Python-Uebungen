wort = "lottozahlen"
geraten = "___________"
fehler = 0

while fehler < 10 and wort != geraten:
    print("Geraten: " + geraten)
    print(f"Fehler: {fehler} von 10")
    buchstabe = input("Bitte geben sie einen Buchstaben ein: ")

    if buchstabe not in geraten and buchstabe in wort:
        for index in range(len(wort)):
            if wort[index] == buchstabe:
                geraten = geraten[:index] + buchstabe + geraten[index + 1:]

        print("Buchstabe vorhanden!")
    else:
        fehler += 1
        print("Buchstabe nicht vorhanden!")

print("Das Wort war: " + wort)
print(f"Fehler: {fehler} von 10")

if fehler < 10:
    print("Sie haben gewonnen!")
else:
    print("Sie haben verloren!")
