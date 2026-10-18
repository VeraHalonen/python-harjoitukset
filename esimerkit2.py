ostoslista = ["maito", "leipä", "juusto", "omena", "kahvi"]

while len(ostoslista) > 0:
    print("Ostoslistalla:", ostoslista)

    tuote = input("Minkä tuotteen ostat? ")

    if tuote in ostoslista:
        ostoslista.remove(tuote)
        print("Tuote poistettu ostoslistalta.")
        print("Jäljellä olevat tuotteet:", ostoslista)
    else:
        print("Tuotetta ei ole ostoslistalla!")

print("Kaikki tuotteet on ostettu!")