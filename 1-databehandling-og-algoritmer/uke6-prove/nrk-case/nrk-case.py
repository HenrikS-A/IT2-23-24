import requests
import json

def bestem_brukertype(bruker: str):
    url = f"https://api.github.com/users/{bruker}"
    
    headers = {
        "Accept": "",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    respons = requests.get(url, headers=headers, timeout=10)
    data = respons.json()

    return data["type"]

def hent_repoer(bruker: str, brukertype):
    if brukertype == "User":
        typen = "users"
    elif brukertype == "Organization":
        typen = "orgs"
    else:
        print("FEIL!")

    url = f"https://api.github.com/{typen}/{bruker}/repos"
    
    headers = {
        "Accept": "",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    respons = requests.get(url, headers=headers, timeout=10)
    data = respons.json()

    return data

bruker = input("Skriv inn et brukernavn eller organisasjonsnavn \n >")
brukertype = bestem_brukertype(bruker) # Eks: "HenrikS-A" / "Microsoft"
repoer = hent_repoer(bruker, brukertype)

print(f"\nRepoene til {bruker}:")
for repo in repoer:
    utskrift_beskrivelser = ["Navn", "URL", "Beskrivelse", "Temaer", "Lisens navn", "Programmeringsspråk"]
    utskrifter = [repo["name"], repo['html_url'], repo['description'], repo['topics'], repo["license"], repo["language"]]
    
    utskrifter = [utskrift if utskrift is not None and utskrift != [] else "-" for utskrift in utskrifter]
    # Dette gjør det samme som one-lineren over:
    # utskrifter_placeholder = []
    # for utskrift in utskrifter:
    #     if utskrift != None and utskrift != []:
    #         utskrifter_placeholder.append(utskrift)
    #     else:
    #         utskrifter_placeholder.append("-")

    for i, utskrift in enumerate(utskrifter):
        if i == 0:
            print(f"\n - {utskrift_beskrivelser[i]}: {utskrift}")
        elif type(utskrift) == dict:
            print(f"\t * {utskrift_beskrivelser[i]}: {utskrift['name']}")
        else:
            print(f"\t * {utskrift_beskrivelser[i]}: {utskrift}")
