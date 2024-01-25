import json
with open("googleplaystore.json", encoding="utf-8") as fil:
    appene = json.load(fil)

kategorier = {}
for app in appene:
    if app["Category"] not in kategorier.keys():
        kategorier[app["Category"]] = 1
    else:
        kategorier[app["Category"]] += 1

sortert_kategorier = sorted(kategorier.items(), key=lambda app:app[1], reverse=True)

topp_3_kategorier = []
for kategori in sortert_kategorier[:3]:
    topp_3_kategorier.append( {"kategori": kategori[0], "antall_apper": kategori[1]} )


for i, kategori in enumerate(topp_3_kategorier):
    sum_rating = 0
    sum_antall_installasjoner = 0 # Fiks dette !!!!!!
    for app in appene:
        if app["Category"] == kategori["kategori"]:
            if app["Rating"] != "NaN":
                sum_rating += float(app["Rating"])

    gjennomsnitt = sum_rating/kategori["antall_apper"]
    topp_3_kategorier[i]["snittrating"] = gjennomsnitt
    pass
