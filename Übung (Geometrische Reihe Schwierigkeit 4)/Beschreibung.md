# Übung: Geometrische Reihe

Schwierigkeit: 4 von 10

Implementieren Sie ein Programm, welches die Geometrische Reihe errechnet.
Diese bildet sich über die Summe der inverse steigender Zweierpotenzen, was
sie in diesem Wikipedia Artikel sehen können:

https://en.wikipedia.org/wiki/Geometric_series

Sie können dies umsetzen, indem sie 2^-i berechnen, wobei i in jedem
Durchlauf um eins steigt. Führen Sie dies solange aus, bis sich das Ergebnis
nicht länger verändert. Da Gleitkommazahlen nur eine gewisse Genauigkeit aufweisen,
erreichen sie diesen Punkt nach etwas Zeit. Mehr dazu erfahren sie in der
Veranstaltung GdI. Haben sie das Programm korrekt implementiert, so sollte
sich das Ergebnis am Ende der 1 (bzw. 2, falls sie die 2^0 einbeziehen) angenähert haben. 
Geben sie daher das Ergebnis am Ende aus.

Potenzen können sie in Python folgendermaßen errechnen:

ergebnis = 2**-i