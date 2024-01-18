# Oppgave 3

"""
Det viktigste mtp. valg av "vasking" av datasettet:
- Jeg fjernet 'landet' nan fra topplista. Nan blir satt som land på alle youtube-kanalene som youtube bruker 
som sine kategorier. Siden dette ikke er et land, valgte jeg å ikke ta med denne.

"""



import json
from matplotlib.pyplot import bar, show, text

with open("Global YouTube Statistics.json", encoding="utf-8") as fil:
    kanaler = json.load(fil)
kanalene = [kanal for kanal in kanaler]


## Del 1:
land_kanaler = {}
for kanal in kanalene:
    land = kanal["Country"]
    if land in land_kanaler.keys():
        land_kanaler[land] += 1
    else:
        land_kanaler[land] = 1

usortert_land_kanal = [{"land": land, "kanaler": kanal} for land, kanal in land_kanaler.items()]
sortert_land_kanal = sorted(usortert_land_kanal, key=lambda kanal: kanal["kanaler"], reverse=True)


# Jeg fjerner nan fra listen
for i, land in enumerate(sortert_land_kanal):
    if land["land"] == "nan":
        del sortert_land_kanal[i]
        break


topp_10_land = [land["land"] for land in sortert_land_kanal[:10]]
topp_10_kanalantall = [land["kanaler"] for land in sortert_land_kanal[:10]]

bar(topp_10_land, topp_10_kanalantall)

for i, verdien in enumerate(topp_10_kanalantall):
    text(i, verdien + 3, str(verdien), horizontalalignment="center")


show()




# Del 2:





