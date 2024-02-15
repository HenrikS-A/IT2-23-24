# Oppgave 2

import json
with open("imdb-top-250.json", encoding="utf-8") as fil:
    filmer = json.load(fil)


## Del 1:
from operator import itemgetter

# Sorterer listen etter verdien av nøkkelen "karakter" for hver film
filmer_sortert = sorted(filmer, key=itemgetter("karakter"), reverse=True) # Høyeste rangering først.

overste_film = []
for i, film in enumerate(filmer_sortert):
    overste_film.append(film)
    
    film_karakter = film["karakter"]
    if film_karakter > filmer_sortert[i+1]["karakter"]:
        break

for film in overste_film:
    regissorer = ""
    for regissor in film["regissører"]:
        regissorer += regissor
    print(f"{film['navn']} - {regissorer}")
pass  


## Del 2:
karakterer = []
for film in filmer:
    karakterer.append(film["karakter"])
gjennomsnitt = sum(karakterer)/len(karakterer)
print("Gjennomsnittskarakter:", round(gjennomsnitt, 3))


## Del 3:
karakterer = []
for film in filmer_sortert[:11]:
    karakterer.append(film["karakter"])
gjennomsnitt = sum(karakterer)/len(karakterer)
print("Top 10 gjennomsnittskarakter:", round(gjennomsnitt, 3))


## Del 4:
regissor_antall_filmer = {}
for film in filmer:
    for regissor in film["regissører"]:
        if regissor in regissor_antall_filmer.keys():
            regissor_antall_filmer[regissor] += 1
        else:
            regissor_antall_filmer[regissor] = 1

flest_filmer = 0
regissorer = []
for regissor, antall_filmer in regissor_antall_filmer.items():
    if antall_filmer > flest_filmer:
        flest_filmer = antall_filmer
        regissorer = [regissor]
    elif antall_filmer == flest_filmer:
        regissorer.append(regissor)

regissorene = []
for regissor in regissorer:
    print(f"{regissor} har {flest_filmer} filmer på topplista")

