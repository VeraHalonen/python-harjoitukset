# Muodostetaan while looppi

while True:

    # Kysytään käyttäjältä tuumamitta input toiminnolla.

    tuuma = float(input('Anna tuumamäärä:'))

    # Muodostetaan if-lauseke, jolla määritellään ohjelma loppumaan jos käyttäjä antaa negatiivisen tuumamäärän

    if tuuma < 0:
        break

    # Muussa tapauksessa tulostetaan tuumamäärä senttimetreiksi
    else:
        print(tuuma * 2.54, 'cm')
        
        