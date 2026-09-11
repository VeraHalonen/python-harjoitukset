# Määritellään muuttujat

kuha = float(input('Kuinka pitkä kuhasi on (cm)?'))

# Muodostetaan if lause, joka pyytää kalastajaa päästämään kuhan takaisin järveen jos se on liian lyhyt

if kuha < 37:
    print('Kuha on', float(37-kuha) ,'cm alle sallitun pyyntimitan.', 'Laske kuha takaisin järveen.')

#Käytetään else toimintoa tulostamaan onnitteluteksti, jos kuha on sallituissa mitoissa

else:
    print('Hieno saalis!')
