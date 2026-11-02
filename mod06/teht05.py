
# Määritellään funktio, joka palauttaa sille annetusta listasta uuden listan, jossa on alkuperäisen listan parilliset luvut
def parilliset(lista):

    # Luodaan tyhjä lista
    lista2 = []
    # Käydään for-loopilla läpi kaikki alkuperäisen listan alkiot 
    # ja lisätään parilliset luvut uuteen tyhjään listaan append toiminnolla
    for l in lista:
        if l % 2 == 0:
            lista2.append(l)
    return lista2

# Luodaan testiohjelmaa varten lista, jolla kokeillaan toimiiko funktio
lista = [1,8,9,-5,-2,10]

# Tulostetaan sekä alkuperäinen lista, että funktion paöauttama lista
print(lista)
print (parilliset(lista))