"""
Jeg oppdaget at det tredje og fjerde mest brukte 
transaksjonsstedet har samme antall kjøp.

I dette programmet gjør jeg ikke noe i forhold til dette.

"""

import json


with open("transaksjoner.json", "r", encoding="utf-8") as fil:
    transaksjoner = json.load(fil)

antall_transaksjoner = {}
dato_transaksjoner = {}

for transaksjon in transaksjoner:
    # Legger inn i antall_transaksjoner:
    if transaksjon["beskrivelse"] not in antall_transaksjoner.keys():
        antall_transaksjoner[transaksjon["beskrivelse"]] = 1
    else:
        antall_transaksjoner[transaksjon["beskrivelse"]] += 1

    # Legger inn i dato_transaksjoner:
    if transaksjon["kjopsdato"] not in dato_transaksjoner.keys():
        dato_transaksjoner[transaksjon["kjopsdato"]] = abs( float(transaksjon["belop"]) )
    else:
        dato_transaksjoner[transaksjon["kjopsdato"]] += abs( float(transaksjon["belop"]) )


sorterte_transaksjoner = sorted(antall_transaksjoner.items(), key=lambda kjop: kjop[1], reverse=True)
topp_3_steder = [transaksjon for transaksjon in sorterte_transaksjoner[:3]]

sorterte_datoer = sorted(dato_transaksjoner.items(), key=lambda kjop: kjop[1], reverse=True)
topp_3_datoer = [transaksjon for transaksjon in sorterte_datoer[:3]]


print("\n -- Oversikt over de tre mest brukte transaksjonsstedene --")
for kjop in topp_3_steder:
    sted = kjop[0]
    antall = kjop[1]
    penger_brukt = 0

    for transaksjon in transaksjoner:
        if transaksjon["beskrivelse"] == sted:
            penger_brukt += abs( float(transaksjon["belop"]) )
    
    print(f"\n{sted}:")
    print(f"\t- Antall transaksjoner: {antall}")
    print(f"\t- Penger brukt: {penger_brukt} kr")


print("\n\n -- Oversikt over de tre datoene der det ble brukt mest penger --")
for dato in topp_3_datoer:
    datoen = dato[0]
    penger_brukt = dato[1]
    antall_kjop = 0

    for transaksjon in transaksjoner:
        if transaksjon["kjopsdato"] == datoen:
            antall_kjop += 1

    print(f"\n{datoen}:")
    print(f"\t- Antall transaksjoner: {antall_kjop}")
    print(f"\t- Penger brukt: {penger_brukt} kr")
