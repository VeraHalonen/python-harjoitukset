#Luodaan tyhä lista
kaupungit = []

#Tehdään for toistorakenne, joka kysyy käyttäjältä kaupungin 5 kertaa ja tallentaa jokaisella kerralla kaupungin listaan
for k in range (1,6):
    kaupunki = input('Anna kaupunki:')
    kaupungit.append(kaupunki)

#Luodaan toinen for toistorakenne
#Kun kaupungit on tallennettu listaan, saadaan ne tulostettua yksitellen for-in rakenteen avulla
for kaupunki in kaupungit:
    print(kaupunki)