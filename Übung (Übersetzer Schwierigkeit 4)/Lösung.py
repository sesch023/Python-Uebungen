dictionary = {
    "Zug": "train",
    "Hochschule": "university",
    "Küche": "kitchen",
    "Tisch": "table",
    "Computer": "computer"
}

eingabe = input("Bitte geben sie ein Wort zum Übersetzen ein: ")

while eingabe != "ende":
    if eingabe in dictionary:
        print(f"{eingabe} -> {dictionary[eingabe]}")
    else:
        print("Wort nicht im dictionary vorhanden! Versuchen sie es nochmal!")

    eingabe = input("Bitte geben sie ein Wort zum Übersetzen ein: ")
