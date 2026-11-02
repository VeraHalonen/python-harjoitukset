# Tuodaan ohjelmaan random kirjasto
import random

# Määritellään funktio, joka palauttaa silmaluku muuttujaan arvotun arvon. Arvo arvotaan numeroiden 1 ja käyttäjän
# syöttämän maksimiluvun väliltä.
def noppa (yht):
    silmaluku = random.randint(1,yht)
    return silmaluku

# Kysytään käyttäjältä nopan tahkojen lukumäärä ja tallennetaan se yht -muuttujaan
yht = int(input('Anna nopan tahkojen määrä: '))

# Määritetään heitto -muuttuja. Muuttuja saa arvon äsken määritellystä funktiosta. Tulostetaan saatu arvo.
heitto = noppa(yht)
print(heitto)

# Luodaan while looppi. Muuttujalle "heitto" annetaan uusi arvo niin kauan kunnes se saa
# käyttäjän antaman tahkohen lukumäärän ts. isoimman mahdollisen luvun. Kaikki arvot tulostetaan.
while heitto != yht:
    heitto = noppa(yht)
    print(heitto)