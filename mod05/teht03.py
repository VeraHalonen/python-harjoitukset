# Kysytään käyttäjältä kokonaisluku
luku = int(input('Anna kokonaisluku:'))

#Määritetään alkuluvun oletus todeksi
alkuluku = True

#Luodaan if-lause, jolla määrittään, että mikäli luku on pienempi kuin 2 se ei ole alkuluku
if luku < 2:
    alkuluku = False

#Luodaan for-loop ja sen sisään if-lauseke, joka jakaa syötetyn luvun kaikilla luvuilla kahdesta syötettyyn lukuun - 1.
#Jos jakojäännös on 0, voidaan luku jakaa muilla kuin yhdellä ja itsellään, jolloin se ei ole alkuluku.
for jakaja in range(2,luku):
    if luku % jakaja == 0:
        alkuluku = False

# Tehdään if lause. Jos alkuluku saa arvon True, luku on alkuluku ja muulloin ei ole alkuluku
if alkuluku == True:
    print('Luku on alkuluku.')
else:
    print('Luku ei ole alkuluku.')