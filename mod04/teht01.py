print('Tässä kaikki kolmella jaolliset luvut välillä 1-1000:')


# Määritetään luku mistä kolmella jaollisten lukujen tulostus aloitetaan
luku = 1

# Tehdään while looppi, joka lisää äsken määritettyyn lukuun yhden
#  niin kauan kun äsken määritetty luku on pienempi tai yhtäsuuri kuin 1000
while luku <= 1000:
    luku += 1

# Koska halutaan ohjelman tulostavan luvuista 1-1000 ainoastaan kolmella jaolliset luvut
# käytetään if-lauseketta toteuttamaan tämä ehto
    if luku % 3 == 0:
        print(luku)

    