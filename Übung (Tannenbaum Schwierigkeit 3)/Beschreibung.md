# Übung: Tannenbaum

Schwierigkeit: 4 von 10

Nutzen Sie for- oder while-Schleifen, um über das wiederholte ausgeben
des Zeichen # und Leerzeichen einen ASCII-Tannenbaum zu erstellen. 

Dieser soll in etwa so aussehen:

<pre>
         #
       #####
     #########
   #############
 #################
         #
       #####
     #########
   #############
 #################
         #
       #####
     #########
   #############
 #################
        ###
        ###
        ###
</pre>

Beim Rechnen können sie Zahlen mittels der Funktion "math.floor"
aus der Bibliothek "math" abrunden.

In Python können sie eine Menge von gleichen Zeichen folgendermaßen
ausgeben:

print("#" * 5)

Dies kann auch verkettet werden:

print(" " * 5 + "#" * 10)