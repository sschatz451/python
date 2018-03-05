#Zahlenraten

import random
fertig = True
titel = "Willkommen beim Zahlen-Rate-Spiel!"
print(titel)
ratens = "Von wo wollen Sie raten?\n"
ratenzs = int(input(ratens))
raten = "Bis wohin wollen Sie raten?\n"
ratenz = int(input(raten))
text = "Bitte versuche meine Zahl zwischen",ratenzs," und ",ratenz," zu erraten."
zufallszahl =(random.randint(ratenzs,ratenz))
counter = 0
print(text)
eingabeText = "Eingabe: "
while (fertig):
    zahl = int(input(eingabeText))
    if (zahl == zufallszahl):
                  print("Gewonnen!")
                  fertig = False
    elif(zahl < zufallszahl):
                        counter = counter = counter + 1
                        print ("Die gesuchte Zahl ist größer als ", zahl)
    else:
                        counter = counter + 1
                        print("Die gesuchte Zahl ist kleiner als ", zahl)

print("\nSie haben ",counter," Versuche benötigt.")
