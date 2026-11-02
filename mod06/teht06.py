# Tuodaan ohjelmaan math kirjasto
import math

# Määritellään funktio, joka palauttaa pizzan yksikköhinnan
def pizza(halkaisija, hinta):
    ala = (math.pi * (halkaisija/2)**2)/10000
    yksikkö = hinta/ala
    return yksikkö


# Kysytään käyttäjältä kahden pizzan halkaisijat ja hinnat
halkaisija1 = float(input('Anna ensimmäinen halkaisija (cm): '))
hinta1 = float(input('Anna ensimmäinen hinta (€): '))
halkaisija2 = float(input('Anna toinen halkaisija (cm): '))
hinta2 = float(input('Anna toinen hinta (€): '))


# Tulostetaan molempien pizzojen yksikköhinnat pizza funktiota kutsumalla
print('Ensimmäisen pizzan yksikköhinta on', pizza(halkaisija1, hinta1), '€')
print('Toisen pizzan yksikköhinta on', pizza(halkaisija2,hinta2), '€')


#Luodaan lopuksi if lauseke, jossa katsotaan funktion avulla kumman pizzan yksikköhinta on pienempi.
if pizza(halkaisija1, hinta1) < pizza(halkaisija2,hinta2):
    print('Ensimmäisen pizza antaa paremman vastineen rahalle. ')
elif pizza(halkaisija1, hinta1) > pizza(halkaisija2,hinta2):
    print('Toinen pizza antaa paremman vastineen rahalle.')
else:
    print('Molemmat pizzat antavat saman vastineen rahalle,.')

