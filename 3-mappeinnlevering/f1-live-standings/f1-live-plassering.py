import requests
import json
from f1_funksjoner import hent_plasseringer, hent_forertall, hent_naaverende_pos, hent_raskeste_runde, hent_forernavn

poengoversikt = {
    "1": 25,
    "2": 18,
    "3": 15,
    "4": 12,
    "5": 10,
    "6": 8,
    "7": 6,
    "8": 4,
    "9": 2,
    "10": 1,
    "11": 0,
    "12": 0,
    "13": 0,
    "14": 0,
    "15": 0,
    "16": 0,
    "17": 0,
    "18": 0,
    "19": 0,
    "20": 0
}

direkte_plasseringer = {}

# Henter poengene fra forrige racehelg og adderer poengene for den direkte stillingen i racet nå/forrige sesjon
# Dvs. at den ikke er riktig før under et race
gammel_forerplassering = hent_plasseringer()
for forer in gammel_forerplassering:
    forertall = hent_forertall(forer)
    naa_posisjon = str(hent_naaverende_pos(forertall))

    naa_poeng = poengoversikt[naa_posisjon]
    
    direkte_plasseringer[forer] = gammel_forerplassering[forer] + naa_poeng

# Legger til poeng for raskeste runde
raskeste_runde_forer = hent_raskeste_runde()
direkte_plasseringer[hent_forernavn(raskeste_runde_forer)] += 1


print(direkte_plasseringer)
