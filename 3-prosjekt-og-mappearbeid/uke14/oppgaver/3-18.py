"""
Finner hvor mange formel 1 førere som kommer fra de ulike landene.
Så blir antall britiske og spanske førere vist.
"""

f1_forere = [
    {"navn": "Max Verstappen", "nasjonalitet": "nederlandsk", "team": "Red Bull Racing", "bilnummer": 1},
    {"navn": "Sergio Perez", "nasjonalitet": "meksikansk", "team": "Red Bull Racing", "bilnummer": 11},
    {"navn": "Lewis Hamilton", "nasjonalitet": "britisk", "team": "Mercedes", "bilnummer": 44},
    {"navn": "George Russell", "nasjonalitet": "britisk", "team": "Mercedes", "bilnummer": 63},
    {"navn": "Charles Leclerc", "nasjonalitet": "monegaskisk", "team": "Ferrari", "bilnummer": 16},
    {"navn": "Kevin Magnussen", "nasjonalitet": "dansk", "team": "Haas F1 Team", "bilnummer": 20},
    {"navn": "Nico Hulkenberg", "nasjonalitet": "tysk", "team": "Haas F1 Team", "bilnummer": 27}
]
 
antall_nasjonaliteter = {}
 
# Legger inn de ulike førerens land inn i ordboka, 
# hvis landet allerede finnes, økes antallet fra dette landet
for forer in f1_forere:         
    if forer['nasjonalitet'] not in f1_forere:
        antall_nasjonaliteter[forer['nasjonalitet']] = 1
    else:
        antall_nasjonaliteter[forer['nasjonalitet']] += 1
 
print(antall_nasjonaliteter["britisk"])
print(antall_nasjonaliteter["spansk"])
