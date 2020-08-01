# Übung: Hangman

Schwierigkeit: 5 von 10

Entwickeln Sie ein kleines Hangman Spiel, mit einem einzigen zu erratenen Wort.
Der Spieler hat 10 Leben und muss das vorgegebene Wort Buchstabe für Buchstabe
erraten. Nutzen sie für das zu erratene Wort das Wort "Lottozahlen". Doppelte
Eingaben falscher Buchstaben werden als Fehler gewertet und müssen nicht abgefangen
werden. Großbuchstaben werden nicht beachtet.

Zur Ersetzung eines Buchstabens in einem String können sie folgenden Trick anwenden:
wort = wort[:index] + buchstabe + wort[index + 1:]

Der Ablauf des Spiels soll in etwa so stattfinden:

<pre>
Geraten: ___________  
Fehler: 0 von 10  
Bitte geben sie einen Buchstaben ein: a  
Buchstabe vorhanden!  
Geraten: ______a____  
Fehler: 0 von 10  
Bitte geben sie einen Buchstaben ein: p  
Buchstabe nicht vorhanden!  
Geraten: ______a____  
Fehler: 1 von 10  
Bitte geben sie einen Buchstaben ein: ö  
Buchstabe nicht vorhanden!  
Geraten: ______a____  
Fehler: 2 von 10  
Bitte geben sie einen Buchstaben ein: l  
Buchstabe vorhanden!  
Geraten: l_____a_l__  
Fehler: 2 von 10  
</pre>
