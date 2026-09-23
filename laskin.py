# Tulostetaan käyttäjälle tieto siitä, mihin ohjelmaan hän on saapunut

print("---------TERVETULOA LASKINOHJELMAAN----------")

# Luodaan while-looppi, jonka ideana on kysyä käyttäjältä haluttu laskutoimitus uudestaan
# niin kauan kunnes käyttäjä lopettaa ohjelman

while True:
    print("Valitse mitä toimintoa haluat käyttää:")
    print("A: Yhteenlasku, B: Vähennyslasku, C: Kertolasku, D: Jakolasku, Q = Lopeta ohjelma")

    # Kysytään käyttäjältä haluttu laskutoimitus, käytetään .upper() metodia, jotta käyttäjän
    # mahdollisesti syöttämät pienet kirjaimet muunnetaan isoiksi kirjaimiksi

    valinta = input("Anna valintasi: ").upper()

    #Määritellään if-lausetta käyttäen, että mikäli käyttäjän antama arvo on 'Q', ohjelma lopetetaan
    if valinta == "Q":
        print("Poistutaan...")
        break

# Määritellään toisella if-lauseella, että jos muuttuja valinta ei ole mikään pyydetyistä vaihtoehdoista, 
# tulostuu virheilmoitus ja ohjelma palaa takaisin while-loopin alkuun. Jotta ohjelma palaa while loopin
# alkuun, käytetään continue toimintoa.

    if valinta not in ["A", "B", "C", "D"]:
        print("Virheellinen valinta.")
        continue      

# Kysytään käyttäjältä luvut a ja b, joiden avulla tehdään pyydetyt laskutoimitukset

    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

# Käytetään if/elif rakennetta tulostamaan kullekin käyttäjän antamalle toiminnolle laskutoimitus
# käyttäjän annettujen lukujen perusteella

    if valinta == "A":
        print(f"Lukujen {a} ja {b} summa on {a+b}.")
    elif valinta == "B":
        print(f"Lukujen {a} ja {b} erotus on {a-b}.")
    elif valinta == "C":
        print(f"Lukujen {a} ja {b} tulo on {a*b}.")
    elif valinta == "D":
        print(f"Lukujen {a} ja {b} osamäärä on {a/b}.")

print("Ohjelma päättynyt.")

#Keksi parempi kohta ilmoittaa virheellisestä valinnasta
#Kommentoi koodi - mitä se tekee missäkin kohdassa?