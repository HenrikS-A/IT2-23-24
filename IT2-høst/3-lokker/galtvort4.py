elever = [
    {"navn": "Harry", "hus": "Griffing", "patronus": "Hjort"},
    {"navn": "Hermine", "hus": "Griffing", "patronus": "Oter"},
    {"navn": "Ronny", "hus": "Griffing", "patronus": "Jack Russel Terrier"},
    {"navn": "Draco", "hus": "Smygard", "patronus": None}
]

print(elever[2]["hus"])

for elev in elever:
    print(elev["navn"])

for elev in elever:
    print(elev["navn"], elev["hus"], elev["patronus"], sep=", ")