
oikea_kayttaja = 'KarriKoira'
oikea_salasana = 'Pyöräilykypärä!'
yritykset = 0


while yritykset < 5:
    kayttaja = str(input('Anna käyttäjätunnus:'))
    salasana = str(input('Anna salasana:'))

    if kayttaja == oikea_kayttaja and salasana == oikea_salasana:
        print('Tervetuloa!')
        break

    else:
        print('Käyttäjätunnus tai salasana on virheellinen')
        yritykset += 1

    if yritykset == 5:
        print('Pääsy evätty!')


        
        