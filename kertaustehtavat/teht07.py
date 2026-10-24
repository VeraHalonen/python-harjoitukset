# Luodaan lista
lista = ['Joey', 'Chandler', 'Ross', 'Rachel', 'Pheope', 'Monica']


muuttuja = 0


print('Yli 5 merkin pituiset sanat ovat: ')

# Tehdään for-silmukka
for sana in lista:
    
    len(sana)

    # Tehdään if-lause. Jos sanan pituus on yli 5 merkkiä, sana tulostetaan
    if len(sana) > 5:
        muuttuja += 1
        print(sana)

print('Listassa on', muuttuja, 'yli 5 merkin pituista sanaa')