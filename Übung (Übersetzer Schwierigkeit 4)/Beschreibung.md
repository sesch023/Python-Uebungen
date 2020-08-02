# Übung: Übersetzer

Schwierigkeit: 4 von 10

Nutzen sie ein Dictionary, um mit diesem fünf deutsche Wörter auf Nutzer
eingabe ins Englische übersetzen zu können. Bei einer Eingabe von "ende"
wird das Programm beendet. Ein Beispiel für ein Dictionary mit zwei Wörtern
sieht folgendermaßen aus:

dictionary = {
    "auto": "car",
    "buch": "book"
}

Auf das englische Wort kann dann mit dictionary["auto"] zugegriffen werden.
Setzen sie das Programm für die Wörter Zug, Küche, Hochschule, Computer
und Tisch um.

Mit folgendem Kommando können sie überprüfen, ob ein deutsches Wort also
ein Schlüssel in dem dictionary vorhanden ist:

<pre>
if wort in dictionary:  
    # do something
</pre>