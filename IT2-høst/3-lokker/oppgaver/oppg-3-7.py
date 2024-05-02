flaggOrdbok = {
    "norge": ["rødt", "hvitt", "blått"],
    "sverige": ["blått", "gult"],
    "danmark": ["rødt", "hvitt"],
    "finland": ["hvitt", "blått"],
    "japan": ["rødt", "hvitt"],
    "gabon": ["grønt", "gult", "blått"],
    "storbritannia": ["rødt", "blått", "hvitt"],
    "chile": ["blått", "hvitt", "rødt"],
    "polen": ["hvitt", "rødt"]
}


def flaggfarger(land):
    if land in flaggOrdbok.keys():
        return flaggOrdbok[land]
    else:
        return None

land = input("Skriv inn et land: ").lower()

if flaggfarger(land) != None:
    for farge in flaggfarger(land):
        print(farge)


