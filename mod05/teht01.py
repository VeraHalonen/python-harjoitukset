#Tuodaan ohjelmaan random kijrasto
import random

#Kysytään input toiminnolla käyttäjältä montako noppaa heitetään
noppa = int(input('Montako noppaa heitetään?'))

#Määritellään summa muuttuja, johon lisätään kunkin heitetyn nopan silmäluku
summa = 0

#Tehdään for-silmukka, jossa arvotaan käyttäjän antaman määrän verran lukuja välillä 1-6
for n in range(noppa):
    luku = random.randint(1,6)
    summa += luku

#Tulostetaan pyydettyjen noppien summa
print(summa)


