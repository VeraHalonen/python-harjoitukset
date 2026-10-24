#Kysytään käyttäjältä kokonaisluku input toiminnolla
luku = int(input('Anna kokonaisluku: '))

#If-elif-toiminnolla pyydetään ohjelmaa tulostamaan halutut tulokset
if luku % 3 == 0 and luku % 5 == 0:
    print('jaollinen molemmilla luvuilla')
elif luku % 3 == 0:
    print('kolmella jaollinen')
elif luku % 5 == 0:
    print('viidellä jaollinen')
else:
    print('Ei jaollinen kolmella eikä viidellä')