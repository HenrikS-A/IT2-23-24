
# Åpne og lese fil i Python

fil = open("tullefil.txt", encoding="utf-8") # Åpner fila tullefil.txt med utf8-enkoding (lar oss bruke æ, ø, å)
data = fil.read() # Leser innholdet i fila
fil.close() # Lukker fila -> frigjør minne.

# Alternativt:
with open("tullefil.txt", encoding="utf-8") as fil:
    data = fil.read()
linjer = data.split("\n") # Splitter på ny linje, lager liste der hver linje er et element.
print(linjer)



# Lese json-filer
import json # Importerer json-biblioteket

fil = open("sanger.json", encoding="utf-8") # Åpner fila sanger.json
sanger = json.load(fil) # Leser og tolker innhold i json-format (sanger er her en lise m ordbøker)
fil.close() # Lukker fila

print(sanger[0])

# Alt:
with open("sanger.json", encoding="utf-8") as fil:
    sanger = json.load(fil)

print(sanger[2])
print(len(sanger))


# Eksempeloppgave:

# Hvor mange sanger av artisten The Weeknd er det på topplista?

antall = 0
for sang in sanger:
    if sang["artist"] == "The Weeknd":
        antall += 1
print(antall)
# -----------


# Hvilken artist har flest sanger på topplista
# Du må lage kode, det er ikke lov å telle!

artist_antall = {}
for sang in sanger:
    if sang["artist"] in artist_antall:
        artist_antall[sang["artist"]] += 1
    else:
        artist_antall[sang["artist"]] = 1
print(artist_antall)

hoyeste_artist = ""
hoyeste_antall = -1

for artist, antall_sanger in artist_antall.items():
    if antall_sanger > hoyeste_antall:
        hoyeste_antall = antall_sanger

print(hoyeste_artist, hoyeste_antall)
