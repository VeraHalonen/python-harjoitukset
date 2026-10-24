# Luodaan lista tuotteiden valmistuskustannuksille
tuote = [12.5, 8.2, 15, 6.5, 10.8]

# Luodaan summamuuttuja, jonka lähtöarvo on nolla
summa = 0

# Luodaan for toistorakenne. 
for hinta in tuote:
    summa += hinta
    print('Tuotteen valmistuskustannus on', hinta)

print('Valmistuskustannukset yhteensä:', summa)