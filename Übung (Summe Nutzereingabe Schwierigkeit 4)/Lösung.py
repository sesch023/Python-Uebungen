eingabe = input("Bitte geben sie eine Zahl oder ende ein: ")
eingaben = []

while eingabe != "ende":
    eingaben.append(float(eingabe))
    eingabe = input("Bitte geben sie eine Zahl oder ende ein: ")

print("Eingaben: " + str(eingaben))

sum = 0
for element in eingaben:
    sum += element

print("Summe: " + str(sum))
