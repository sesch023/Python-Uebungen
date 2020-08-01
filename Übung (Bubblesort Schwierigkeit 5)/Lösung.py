eingabe = input("Bitte geben sie eine Zahl oder ende ein: ")
eingaben = []

while eingabe != "ende":
    eingaben.append(float(eingabe))
    eingabe = input("Bitte geben sie eine Zahl oder ende ein: ")

print("Eingaben: " + str(eingaben))

vertauscht = True
while vertauscht:
    vertauscht = False
    for index in range(len(eingaben) - 1):
        if eingaben[index] < eingaben[index + 1]:
            wert = eingaben[index]
            eingaben[index] = eingaben[index + 1]
            eingaben[index + 1] = wert
            vertauscht = True

print("Sortiert: " + str(eingaben))
