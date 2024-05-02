# Oppg. 3.1
def alminnelig_inntektsskatt(inntekt: int, fylke: str) -> int:
    if fylke.lower() == "troms og finnmark":
        skatt = round(inntekt * 18.5/100)
    else:
        skatt = round(inntekt * 22.0/100)
    return skatt

# print(alminnelig_inntektsskatt(100_000, "Agder"))
# print(alminnelig_inntektsskatt(100_000, "TroMs og FinnMark"))


# Oppg. 3.2
def trinnskatt(inntekt: int) -> int:
    if 0 <= inntekt <= 198_349:
        skatt = 0
    elif 198_350 <= inntekt <= 279_149:
        skatt = round(inntekt * 1.7/100)
    elif 179_150 <= inntekt <= 642_949:
        skatt = round(inntekt * 4.0/100)
    elif 642_950 <= inntekt <= 926_799:
        skatt = round(inntekt * 13.5/100)
    elif 926_800 <= inntekt <= 1_499_999:
        skatt = round(inntekt * 16.5/100)
    elif inntekt >= 1_500_000:
        skatt = round(inntekt * 17.5/100)
    return skatt

# print(trinnskatt(50_000))
# print(trinnskatt(200_000))
# print(trinnskatt(300_000))
# print(trinnskatt(700_000))
# print(trinnskatt(1_000_000))
# print(trinnskatt(2_000_000))


# Oppg. 3.3
def totalskatt(inntekt: int, fylke: str) -> int:
    return alminnelig_inntektsskatt(inntekt, fylke) + trinnskatt(inntekt)

# print(totalskatt(400_000, "Troms og Finnmark"))
# print(totalskatt(400_000, "Viken"))


# Oppg. 3.4
def maks_skatt(inntektsliste: list[int]) -> int:
    antall_hoyeste_skatteprosenter = 0
    for inntekt in inntektsliste:
        if inntekt > 1_500_000:
            antall_hoyeste_skatteprosenter += 1
    return antall_hoyeste_skatteprosenter

# print(maks_skatt([100_000, 900_000, 2_300_000, 1_600_000]))


# Oppg. 3.5
def lav_skatt(personliste: list[dict]) -> list[dict]:
    personer_lav_skatt = []
    for person in personliste:
        skatt = totalskatt(person["inntekt"], person["fylke"])
        if skatt < 25_000:
            personer_lav_skatt.append(person)
    return personer_lav_skatt


# personer = [
#     {"navn": "WW", "inntekt": 125_000, "fylke": "Troms og Finnmark"},
#     {"navn": "JP", "inntekt": 100_000, "fylke": "Trøndelag"},
#     {"navn": "SW", "inntekt": 600_000, "fylke": "Troms og Finnmark"},
#     {"navn": "HS", "inntekt": 600_000, "fylke": "Viken"}
# ]
# print(lav_skatt(personer))

