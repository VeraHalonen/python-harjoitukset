# Tuodaan ohjelmaan random kirjasto
import random

# Määritellään funktio, joka palauttaa ailmaluku muuttujaan arvotun arvon (nopan silmäluku)
def noppa ():
    silmaluku = random.randint(1,6)
    return silmaluku

# Määritetään heitto -muuttuja. Muuttuja saa arvon äsken määritellystä funktiosta. Tulostetaan saatu arvo.
heitto = noppa()
print(heitto)

# Luodaan while looppi. Muuttujalle "heitto" annetaan uusi arvo niin kauan kunnes se saa arvon 6. Kaikki arvot tulostetaan
while heitto != 6:
    heitto = noppa()
    print(heitto)
    
