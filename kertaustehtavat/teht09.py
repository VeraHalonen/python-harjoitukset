# Luodaan tyhjät listat valmistettaville tuotteille ja kappalemäärille
tuotteet = []
maarat = []

# Kysytään käyttäjältä kysymykset
tuote = input('Mitä tuotetta valmistetaan? ')
kpl = int(input('Kuinka monta kappaletta tuotetta valmistetaan? '))
tuotanto = input('Jatektaanko tuotantoa (Kyllä/Ei)? ')

# Lisätään käyttäjän syöttämät tiedot listoihin
tuotteet.append(tuote)
maarat.append(kpl)

# Luodaan while loop, jossa kysytään samat kysymykset sekä tallennetaan ne listoihin niin kauan
# kun käyttäjä syöttää tuotanto muuttujaan "Kyllä"
while tuotanto == 'Kyllä':

    tuote = input('Mitä tuotetta valmistetaan? ')
    kpl = int(input('Kuinka monta kappaletta tuotetta valmistetaan? '))
    tuotanto = input('Jatektaanko tuotantoa (Kyllä/Ei)? ')
    tuotteet.append(tuote)
    maarat.append(kpl)

# Kun käyttäjä syöttää tuotanto muuttujaan jotain muuta kuin "Kyllä", while silmukasta poistutaan
# Määritetään if-else lauseela, että mikäli käyttäjä syöttää tuotanto muuttujaan arvon "Ei", tuotanto lopetetaan
if tuotanto == 'Ei':
    print('Tuotanto lopetettu!')

    # Luodaan for-toistorakenne ja käydään läpi tuotteet -listan indeksit
    for i in range(len(tuotteet)):
        # Tulostetaan kaikki tuotteet- ja maarat- listojen arvot
        print (tuotteet [i] + ':', maarat[i], 'kpl')

# Else osiossa tulostetaan viesti "Virheellinen komento." jos komento ei ole tehtävänannossa annettu "Kyllä" tai "Ei"
else:
    print('Virheellinen komento.')



