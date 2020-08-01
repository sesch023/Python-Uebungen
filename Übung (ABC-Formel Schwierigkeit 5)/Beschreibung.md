# Übung: ABC-Formel

Schwierigkeit: 5 von 10

Schreiben Sie ein Programm, in welchem ein Nutzer die Parameter
a,b und c für a*x²+b*x+c einer quadratischen Gleichung übergeben kann. Das
Programm soll dann mittels der ABC-Formel die möglichen Nullstellen errechnen.
Für die ABC-Formel gilt:

https://en.wikipedia.org/wiki/Quadratic_formula

Denken sie an die Sonderfälle. Das a darf für die ABC Formel nicht 0 sein
und die Wurzel in den Lösungsfällen ist für negative Zahlen nicht definiert. 
Dies würde in einer fehlenden Lösung resultieren. Eine Wurzel ziehen können
sie mittels der Funktion "math.sqrt" aus der Bibliothek "math". Importieren sie
diese mittels import math am Anfang der Datei.