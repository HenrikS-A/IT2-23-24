# Oppgave 1

import json
with open("spotify-weekly-top-songs-global.json",encoding="utf-8") as fil:
    sanger = json.load(fil)


## Del 1:
hoyeste_antall_uker = 0
sangene = []
for sang in sanger:
    if sang["uker_paa_listen"] > hoyeste_antall_uker:
        hoyeste_antall_uker = sang["uker_paa_listen"]
        sangene = [sang]
    elif sang["uker_paa_listen"] == hoyeste_antall_uker:
        sangene.append(sang)

for sang in sangene:
    print(f"{sang['artist']}: {sang['navn']}, {hoyeste_antall_uker} uker")


## Del 2:
taylor_streams = 0
for sang in sanger:
    if sang["artist"] == "Taylor Swift":
        taylor_streams += sang["antall_streams"]
print(f"{taylor_streams} streams")


## Del 3:
flest_antall_plasser = -999999
sangene = []
for sang in sanger:

    if sang["forrige_plassering"] == -1:
        sang["forrige_plassering"] = 251

    plass_delta = sang["forrige_plassering"] - sang["plassering"]
    
    if plass_delta > flest_antall_plasser:
        flest_antall_plasser = plass_delta
        sangene = [sang]
    elif plass_delta == flest_antall_plasser:
        sangene.append(sang)

for sang in sangene:
    print(f"{sang['artist']}: {sang['navn']}, {flest_antall_plasser} plasser opp")
