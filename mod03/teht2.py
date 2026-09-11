# Määritellään muuttujat

hytti = str(input('Mikä on hyttiluokkasi?'))

# Käytetään if/elif/else toistorakennetta, jotta saadaan jokaiselle hyttiluokalle tulostettua kuvaus

if hytti == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')

elif hytti == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')

elif hytti == 'B':
        print('B on ikkunaton hytti autokannen yläpuolella.')

elif hytti == 'C':
        print('C on ikkunaton hytti autokannen alapuolella.')

else:
    print('Virheellinen hyttiluokka.')