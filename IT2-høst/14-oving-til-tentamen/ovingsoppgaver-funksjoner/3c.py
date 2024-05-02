
def fjern_vokaler(setning: str, vokal_liste: list[str]):
    ny_setning = ""
    for tegn in setning:
        if tegn not in vokal_liste:
            ny_setning += tegn
    
    return ny_setning


a = fjern_vokaler("ha det fint", ["a", "e", "i", "o", "u", "y"])
print(a)