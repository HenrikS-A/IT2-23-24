# Oppgave 3

"""
Det viktigste mtp. valg av "vasking" av datasettet:
Jeg fjernet 'landet' nan fra topplista. Nan blir satt som land på alle youtube-kanalene som youtube bruker 
som sine kategorier. Siden dette ikke er et land, valgte jeg å ikke ta med denne.

Merk: Anbefaler å bruke fullskjermsmodus på vinduet jeg plotter og visualiserer dataene i.
"""



import json
import matplotlib.pyplot as plt
import numpy as np

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

# Jeg fjerner "landet" nan fra listen
for i, land in enumerate(sortert_land_kanal):
    if land["land"] == "nan":
        del sortert_land_kanal[i]
        break

topp_10_land = [land["land"] for land in sortert_land_kanal[:10]]
topp_10_kanalantall = [land["kanaler"] for land in sortert_land_kanal[:10]]



# Plotter søylediagram
plt.bar(topp_10_land, topp_10_kanalantall) 

## Viser verdien over søylene:
for i, verdien in enumerate(topp_10_kanalantall):
    plt.text(i, verdien + 3, str(verdien), horizontalalignment="center")

## Diverse utforming
plt.gcf().canvas.manager.set_window_title("Data visualisering (bruk fullskjerm)") # Tittel

plt.title("Topp 10 land med flest YT-kanaler på topplista")
plt.xlabel("Land")
plt.ylabel("Antall kanaler")

plt.show() 



# Del 2:

topp_10_subscriber_avg = []
topp_10_visninger_avg = []

for i, land in enumerate(topp_10_land):
    land_subscribers = 0
    land_visninger = 0
    for kanal in kanalene:
        if kanal["Country"] == land:
            land_subscribers += kanal["subscribers"]
            land_visninger += kanal["video views"]

    sub_avg = land_subscribers / topp_10_kanalantall[i]
    topp_10_subscriber_avg.append(round(sub_avg, 1))

    visning_avg = land_visninger / topp_10_kanalantall[i]
    topp_10_visninger_avg.append(round(visning_avg, 1))



"""
Dette kan jeg gjøre for å få to stolper pr. x-verdi.
Men her fungerer det ikke fordi det er ekstremt mange flere views enn subscribers, så man ser ikke begge stolpene samtidig.
"""
# x_akse = np.arange(len(topp_10_land))

# plt.bar(x_akse - 0.2, topp_10_subscriber_avg, 0.4, label="gjennomsnitt abonnenter") 
# plt.bar(x_akse + 0.2, topp_10_visninger_avg, 0.4, label="gjennomsnitt videovisninger") 

# plt.legend()
# plt.show()



plt.bar(topp_10_land, topp_10_subscriber_avg)
plt.show()

plt.bar(topp_10_land, topp_10_visninger_avg)
plt.show()

