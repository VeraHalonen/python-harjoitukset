# Luodaan tyhjä lista
lista = []

# Kysytään käyttäjältä arvo
arvo = float(input('Anna arvo, lopeta syättämällä 0: '))

# Luodaan while silmukka, jota toistetaan kunnes käyttäjä antaa arvon 0
while arvo != 0:
    # Lisätään kaikki käyttäjän antamat arvot listaan
    lista.append(arvo)
    # Tulostetaan lista sellaisenaan sekä järjestettynä sorted() komennolla
    print(lista)
    print(sorted(lista))
    arvo = float(input('Anna arvo, lopeta syöttämällä 0: '))

# Kun käyttäjä antaa arvoksi 0, kerrotaan että ohjelma päättyi
print('Ohjelma päättyi')