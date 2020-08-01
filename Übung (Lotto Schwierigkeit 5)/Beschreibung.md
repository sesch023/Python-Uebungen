# Übung: Lotto

Schwierigkeit: 5 von 10

Erlauben Sie 6 Nutzereingaben zwischen 1 und 49. Speichern Sie diese in eine
Liste. Schreiben Sie danach einen kleinen Lottogenerator, welcher 6 Zahlen zwischen
1 bis 49 zieht. Die Zahlen werden danach mit den Nutzereingaben abgeglichen
und die Anzahl der richtigen Stellen ausgegeben.

Bedenken Sie, dass in der Eingabe und im Generator keine Zahl doppelt vorkommen darf.
Für die Bestimmung zufälliger Integer, verwenden sie die Funktion random.randrange(start, stop)
mit den Werten 1 für start und 50 für stop. Dies resultiert in einer zufälligen Zahl zwischen
1 und 49. Zur Verwendung der Funktion müssen sie die Bibliothek random über import random am
Anfang des Skriptes importieren.