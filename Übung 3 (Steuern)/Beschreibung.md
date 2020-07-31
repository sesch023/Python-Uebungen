# Übung 3: Steuern

Schwierigkeit: 2 von 10

Für das Finanzamt in Iserlohn soll ein Steuerrechner implementiert werden.
Dieser soll anhand der folgenden nicht realen Steuersätzen, anhand Einkommen
und Vermögen, eine jährliche zu bezahlende Steuer errechnen:

Jährliches Einkommen E:

E < 20000 € -> Steuersatz se = 5%
20000 € <= E < 40000 € -> Steuersatz se = 15%
40000 € <= E < 100000 € -> Steuersatz se = 25%
E >= 100000 € -> Steuersatz se = 40%

Vermögen V:

V < 10000 € -> Steuersatz sv = 1%
10000 € <= V < 50000 € -> Steuersatz sv = 3%
50000 € <= V < 200000 € -> Steuersatz sv = 5%
V >= 200000 € -> Steuersatz sv = 10%

Berechnen sie mittels eines Programms auf Basis folgender Formel die Steuer und
geben sie diese mittels der print-Funktion aus:

Steuer = se * E + sv * V

Die Variablen für V und E sind dabei bereits vorgegeben.