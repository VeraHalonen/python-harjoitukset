# Luodaan tyhjä lista
tarina = []

# Kyaytään käyttäjältä tarinaan lisättävä sana
sana = input('Anna sana lisättäväksi tarinaan, tulosta tarina kirjoittamalla "loppu": ')

# Luodaan while loop. Kysytään uutta sanaa kunnes käyttäjä antaa sanan "loppu"
while sana != 'loppu':
    # Lisätään jokainen käyttäjän antaja sana listaan
    tarina.append(sana)
    sana = input('Anna sana lisättäväksi tarinaan, tulosta tarina kirjoittamalla "loppu": ')

# Kun käyttäjä on syöttänyt sanan "lopeta", tulostetaan kaikki listaan tallennetut sanat ja liitetään ne yhtee
print(' '.join(tarina))
