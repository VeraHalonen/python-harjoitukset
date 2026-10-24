#Tuodaan ohjelmaan math kirjasto
import math

#Kysytään käyttäjältä kokonaisluku
luku = int(input('Anna kokonaisluku: '))

#Luodaan while silmukka, jota toistetaan niin kauan kunnes käyttäjä antaa luvuksi 0
while luku != 0:
    # Muodostetaan if-else lauseke. Jos luku on pienempi kuin nolla, tulostataan viesti "Virheellinen numero"
    # Muissa tapauksissa tulostetaan käyttäjän syöttämän luvun neliöjuuri
    if luku < 0:
        print('Virheellinen numero')
    else:
        print('Luvun neliöjuuri on', math.sqrt(luku))
    # Tulostuksen jälkeen kysytään luku uudestaan -> silmukka alkaa alusta
    luku = int(input('Anna kokonaisluku: '))

# Jos käyttäjä syöttää luvun 0, ohjelma päättyy
print('Ohjelma päättyi')