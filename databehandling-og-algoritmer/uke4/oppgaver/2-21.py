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
    sum_installasjoner = 0 # Fiks dette !!!!!!
    for app in appene:
        if app["Category"] == kategori["kategori"]:
            if app["Rating"] != "NaN":
                sum_rating += float(app["Rating"])
            
            installasjoner = app["Installs"]
            installasjoner = installasjoner.replace(",", "")
            installasjoner = installasjoner.replace("+", "")
            sum_installasjoner += int(installasjoner)

    rating_snitt = sum_rating/kategori["antall_apper"]
    topp_3_kategorier[i]["snittrating"] = round(rating_snitt, 2)

    installering_snitt = sum_installasjoner/kategori["antall_apper"]
    topp_3_kategorier[i]["snitt_installasjoner"] = round(installering_snitt, 2)


print(" -- De største kategoriene -- ")
for i, kategori in enumerate(topp_3_kategorier):
    print(f"{i+1}: {kategori['kategori']}")
    print(f"\tAntall apper: {kategori['antall_apper']}")
    print(f"\tSnittrating: {kategori['snittrating']}")
    print(f"\tSnitt antall installasjoner: {kategori['snitt_installasjoner']}")

