import json

with open("transaksjoner.json", encoding="utf-8") as fil:
    transaksjoner = json.load(fil)

# Deloppgaver 1 og 2

transaksjoner_antall = {}

for transaksjon in transaksjoner:
    beskrivelse = transaksjon["beskrivelse"]
    if beskrivelse not in transaksjoner_antall:
        transaksjoner_antall[beskrivelse] = {
            "penger": float(transaksjon["belop"]),
            "antall": 1
        }
    else:
        transaksjoner_antall[beskrivelse]["penger"] += float(transaksjon["belop"])
        transaksjoner_antall[beskrivelse]["antall"] += 1

sortert_transaksjoner = sorted(transaksjoner_antall.items(), key=lambda trans: trans[1]["antall"], reverse=True)

print()
print("Salgsteder med høyest antall transaksjoner")
for i in range(3):
    print(f"{i + 1}: {sortert_transaksjoner[i][0]}; antall: {sortert_transaksjoner[i][1]['antall']}; beløp: {sortert_transaksjoner[i][1]['penger']}")

# Deloppgave 3
datoer_antall = {}
for transaksjon in transaksjoner:
    dato = transaksjon["kjopsdato"]
    if dato not in datoer_antall:
        datoer_antall[dato] = {
            "antall": 1,
            "beløp": float(transaksjon["belop"])
        }
    else:
        datoer_antall[dato]["antall"] += 1
        datoer_antall[dato]["beløp"] += float(transaksjon["belop"])

sortert_datoer = sorted(datoer_antall.items(), key=lambda dato: dato[1]["beløp"])

print()
print("Datoer med høyest forbruk")
for i in range(3):
    print(f"{i + 1}: {sortert_datoer[i][0]}; antall: {sortert_datoer[i][1]['antall']}; beløp: {sortert_datoer[i][1]['beløp']}")

