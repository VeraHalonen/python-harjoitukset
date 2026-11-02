
# Määritellään funktio, joka palauttaa litramäärän käyttäjän syöttämän gallonamäärän perusteella.
def litrat(gallon):
    litra = gallon * 3.785
    return litra

# Kysytään käyttäjältä gallonamäärä ja tallennetaan se muuttujaan
gallon = float(input('Anna gallonien määrä, lopeta antamalla negatiivinen luku: '))

# Luodaan while looppi, jolla tulostetaan käyttäjän antama gallonamäärä niin kauan, kunnes käyttäjä syöttää negatiivisen luvun
while gallon >= 0:
    print (litrat(gallon))
    gallon = float(input('Anna gallonien määrä, lopeta antamalla negatiivinen luku: '))
    

# Ilmoitetaan käyttäjälle ohjelman loppumisesta
print('Ohjelma loppui.')


