#Zahlenraten

import random
zufallszahl =(random.randint(1,100))
fertig = True
titel = "Willkommen beim Zahlen-Rate-Spiel!"
text = "Bitte versuche meine Zahl zwischen 1 und 100 zu erraten."
counter = 0
print(titel)
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
