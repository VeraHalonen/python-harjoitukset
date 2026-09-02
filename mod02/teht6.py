# Tuodaan random kirjasto

import random

# Määritellään sekä kolminumeroinen, että nelinumeroinen luku
kolminumeroinen_koodi = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
nelinumeroinen_koodi = str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 9))

# Tulostetaan koodit

print('Kolminumeroinen koodi on: ' + kolminumeroinen_koodi)
print('Nelinumeroinen koodi on: ' + nelinumeroinen_koodi)
