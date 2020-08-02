# Übung: Temperatureinheiten

Erweitern sie die Aufgabe aus der Übung Fahrenheit Nutzereingabe. Der
Nutzer kann vor der Eingabe definieren, ob diese in Celsius, Fahrenheit
oder Kelvin erfolgt. Dies kann beispielsweise folgendermaßen aussehen:

1 - Celsius  
2 - Fahrenheit  
3 - Kelvin  
ende - Beenden

Wird eine 1 eingegeben, so folgt die Eingabe des Temperaturwerts. Danach
kann dieser in die nicht eingegebenen Einheiten umgewandelt werden, welche
im folgende ausgegeben werden:

Fahrenheit: 356.0  
Celsius: 180.0  
Kelvin: 453.15  

Das Programm wird solange wiederholt, bis der Nutzer bei der Auswahl
"ende" eingibt. Für die Umrechnung von Celsius in Fahrenheit gilt:

fahrenheit = (celsius * 9/5) + 32