#Luodaan tyhä lista
luvut = []

#Kysytään käyttäjältä luvut 
luku = input('Anna luku tai lopeta painamalla enter:')

#Tehdään while-silmukka, jossa määritellään, että uutta lukua kysytään kunnes syötetään tyhjä merkkijono
while luku != '':
    #Määritetään syötetyiksi arvoiksi float
    luvut.append(float(luku))
    luku = input('Anna luku tai lopeta painamalla enter:')

#Järjestetään luvut suuruusjärjestykseen isoimmasta suurimpaan
luvut.sort(reverse=True)

#Tulostetaan listasta vain 5 isointa lukua
print(luvut[:5])


