# Berechnung eines Rechtecks

# Überschrift
print("Flächenberechnung euines Rechtecks")

# Schreibe ein Programm, dass die Fläche eines Rechtecks berechnet.
# Sooll aus folgenden Schritten bestehen:
#   - Eingabe Länge und Breite
#   - Flächenberechnung und speicherung
#   - Ausgabe (Satz: 'Die Fläche beträgt ___ m^2!' ausgeben)


print( )
laenge = int(input("Was ist die Länge? "))
breite = int(input("Und was die Breite? "))

# Verarbeitung

flaeche = laenge*breite

# Ausgabe

print("Die Fläche beträgt", flaeche ,"cm\u00b2!")


# Umfangsberechnung


answ = input("Möchtest du den Unfang auch bekommen? [Y/N] ")

if answ == "Y":
    umfang = 2*laenge+2*breite
    print("Der Umfang beträgt:", umfang, "cm!")
else:
    print("Bye!")