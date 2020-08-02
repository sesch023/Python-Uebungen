# Übung: Tic-Tac-Toe Feld Ausgeben

Schwierigkeit: 3 von 10

Geben sie ein Tic-Tac-Toe Feld in der Konsole aus. Definieren Sie dieses
vorher in einem eindimensionalen oder zweidimensionalen Liste. Die
ist eine Vorbereitung für eine spätere Aufgabe, in welcher Tic-Tac-Toe 
implementiert wird.

Das Feld sollte in etwa so aussehen:

<pre>
+---+  
|x  |  
|oxo|  
| xo|  
+---+  
</pre>

Die Randzeichen sollen dabei nicht in der Liste definiert, sondern
bei den Ausgaben hinzugefügt werden. Um eine Ausgabe ohne eine neue 
Zeile zu tätigen, können sie der print-Funktion mit dem Parameter "end"
ein anderes Endezeichen definieren:

print('Text', end='')