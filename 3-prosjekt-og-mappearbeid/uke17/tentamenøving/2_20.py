import json

with open("twitter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

# Lagrer alle brukerne i ordboka
brukere = {}
for bruker in data:
    brukere[bruker["username"]] = bruker["followers"]

# Sorterer brukerne i ordboka over etter antall følgere i en ny liste 
sorterte_brukere = sorted(brukere.items(), key=lambda folgere: folgere[1], reverse=True)

# Lager en oversikt over de 10 "topp-brukerne"
topp_brukere = {}
for bruker in sorterte_brukere[:10]:
    topp_brukere[bruker[0]] = {"folgere": bruker[1]}

# Legger inn antall tweets og følger-følgere-forholdet i topp-bruker-oversikten
for b in data:
    if b["username"] in topp_brukere.keys():
        topp_brukere[b["username"]]["tweets"] = b["tweets"]
        topp_brukere[b["username"]]["folger_folgere_forhold"] = round( b["following"]/b["followers"], 5 )   


# Presenterer dataen i terminalen
for brukernavn, innhold in topp_brukere.items():
    print(f"{brukernavn}:")
    print(f"\t- Følgere: {innhold['folgere']}")
    print(f"\t- Antall tweets: {innhold['tweets']}")
    print(f"\t- følger/følgere-forhold: {innhold['folger_folgere_forhold']}")
