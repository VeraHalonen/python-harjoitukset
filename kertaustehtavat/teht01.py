#Kysytään käyttäjältä halutut muuttujat input toiminnolla
tuntipalkka = float(input('Mikä on tuntipalkkasi? '))
tunnit = float(input('Montako tuntia teit töitä? '))
pvm = input('Mikä viikonpäivä tänään on? ')


#Muodostetaan if-else lauseke. Jos pvm on sunnuntai, tulostetaan tuntipalkka kaksinkertaisena, muulloin 1. kertaisena.
if pvm == 'sunnuntai':
    print('Päivän palkkasi on', 2 * tuntipalkka * tunnit)
else:
    print('Päivän palkkasi on', tuntipalkka * tunnit)