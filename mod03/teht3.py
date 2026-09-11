# Määritellään muuttujat

skpl = str(input('Mikä on biologinen sukupuolesi (nainen/mies)?'))
BHb = float(input('Mikä on hemoglobiinisi (g/l)?'))

# Käytetään if/elif/else ketjurakennetta määrittämään kullekin muuttujien yhdistelmälle haluttu tulostus

if skpl == 'nainen' and 117 <= BHb <= 175:
    print('Hemoglobiinisi on normaali.')

elif skpl == 'nainen' and BHb < 117:
    print('Hemoglobiinisi on alhainen.')

elif skpl == 'nainen' and BHb > 175:
    print('Hemoglobiinisi on korkea.')

elif skpl == 'mies' and 134 <= BHb >= 195:
    print('Hemoglobiinisi on normaali.')

elif skpl == 'mies' and BHb < 134:
    print('Hemoglobiinisi on alhainen.')

elif skpl == 'mies' and BHb > 195:
    print('Hemoglobiinisi on alhainen')

# Käytetään else toimintoa tulostamaan virheilmoitus, mikäli syötetyt arvot ei ole haluttuja

else:
    print('Tapahtui virhe.')