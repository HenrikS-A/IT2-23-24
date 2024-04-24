"""
Det ser ut som at noen av "kanalene" som er listet i json-fila
er kategorier istedenfor kanaler. Disse kategoriene har ikke et land,
så jeg har valgt å utela å ta med disse.

Dette har medført endringer i if-setningen på linje 18 (ca.)

"""

import json


with open("Global YouTube Statistics.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)


kanaloversikt = {}
for kanal in data:
    if kanal["Country"] not in kanaloversikt.keys() and kanal["Country"] != "nan":
        kanaloversikt[kanal["Country"]] = 1
    elif kanal["Country"] in kanaloversikt.keys():
        kanaloversikt[kanal["Country"]] += 1
        
sortert_kanaloversikt = sorted(kanaloversikt.items(), key=lambda antall: antall[1], reverse=True)
topp_10 = [land for land in sortert_kanaloversikt[:10]]



print("Topp-10 land med flest YouTube abonnenter: \n")

for land in topp_10:
    antall_kanaler = land[1]
    abonnenter = 0
    videovisninger = 0

    for k in data:
        if k["Country"] == land[0]:
            abonnenter += k["subscribers"]
            videovisninger += k["video views"]

    gj_abonnenter = abonnenter / antall_kanaler
    gj_videovisninger = videovisninger / antall_kanaler


    print(f"{land[0]}:")
    print(f"\t - Gjennomsnittlig antall abonnenter: {round(gj_abonnenter, 1)}")
    print(f"\t - Gjennomsnittlig videovisninger: {round(gj_videovisninger, 1)}")
