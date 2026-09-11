# Määritellään muuttujat

vuosi = int(input('Anna vuosi:'))

# If lauseessa täyttyy karkausvuosien ehdot. Neljällä, mutta ei sadalla jaollinen vuosi = karkausvuosi
# TAI 400 jaolliset vuodet = karkausvuosi

if vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0:
    print('Vuosi on karkausvuosi.')

else:
    print('Vuosi ei ole karkausvuosi.')