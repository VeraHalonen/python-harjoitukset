# Määritellään muuttujat

kanta = float(input('Anna suorakulmion kanta: '))
korkeus = float(input('Anna suorakulmion korkeus: '))

# Lasketaan piiri ja pinta-ala

piiri = 2 * (kanta + korkeus)
ala = kanta * korkeus

# Tulostetaan tulokset

print('Suorakulmion piiri on: ' + str(piiri))
print('Suorakulmion pinta-ala on: ' + str(ala))