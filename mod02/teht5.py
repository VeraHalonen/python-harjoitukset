# Määritellään muuttujat

lieviska = int(input('Anna lieviskät: '))
naula = int(input('Anna naulat: '))
luoti = int(input('Anna luodit: '))

# Lasketaan kunkin keskiaikaisen mitan massat

massa_lieviska = lieviska * 20 * 32 * 13.3
massa_naula = naula * 32 * 13.3
massa_luoti = luoti * 13.3

# Lasketaan kokonaismassa nykymittojen mukaan.
# Käytetään // toimointoa, jotta saadaan ensin kilogrammat kokonaislukuna
# Käytetään % toimintoa, jotta saadaan jakojäännös eli grammat kilogrammojen päälle

massa_kg = (massa_lieviska + massa_naula + massa_luoti) // 1000
massa_g = (massa_lieviska + massa_naula + massa_luoti) % 1000

# Tulostetaan lopullinen massa nykymittojen mukaan

print(f'Massa nykymittojen mukaan on: {int(massa_kg)} kilogrammaa ja {massa_g:3.2f} grammaa.')
