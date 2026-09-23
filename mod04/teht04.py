import random

luku = str(random.randint(1, 10))

# Riviä 6 on käytetty tarkistamaan toimiiko koodi oikein.
print(luku)

while True:

    arvaus = input('Arvaa luku väliltä 1-10:')

    if arvaus == luku:
        print('Arvasit oikein!')
        break
    elif arvaus < luku:
        print('Liian pieni arvaus.')
    elif arvaus > luku:
        print('Liian suuri arvaus')