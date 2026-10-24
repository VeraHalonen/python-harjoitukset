#Tulostetaan ohjelman alkuun haluttu viesti "Tuote valmistettu!"
print('Tuote valmistettu!')

#Kysytään käyttäjältä jatketaanko tuotantoa
tuotanto = input('Jatketaanko tuotantoa? ')

#Luodaan while-silmukka. Niin kauan, kunnes käyttäjä syöttää arvon "Ei" jatketaan viestin ja kysymyksen tulostusta
while tuotanto != 'Ei':
    print('Tuote valmistettu!')
    tuotanto = input('Jatketaanko tuotantoa? ')
    
#Kun while silmukan ehto ei enään toteudu, tulostetaan haluttu viesti "Tuotanto lopetettu"
print('Tuotanto lopetettu!')