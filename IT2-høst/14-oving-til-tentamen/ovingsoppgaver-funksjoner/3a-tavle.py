# Oversikt over hva oppgaven går ut på:

# Lage en funksjon som returnerer antall dager en person skal være i karantene

# if person vaksinert, returner 0
# if person uvaksinert og vært i land rød/oransje, returner 10
# if person uvaksinert og vært i land grønn, returner 3


def karantene(vaksinert: bool, farge: str):
    if vaksinert:
        return 0
    
    elif not vaksinert and (farge == "roed" or farge == "oransje"):
        return 10
    elif not vaksinert and farge == "groenn":
        return 3

    # elif not vaksinert:
    #     if farge == "roed" or farge == "oransje":
    #         return 10
    #     elif farge == "groenn":
    #         return 3
    

karantenedager = karantene(False, "oransje")
print(karantenedager)
