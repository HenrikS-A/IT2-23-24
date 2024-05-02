
def lag_brukernavn(fullt_navn):
    navn = fullt_navn.split()
    brukernavn = navn[0].lower() + navn[1][:3].lower()
    return brukernavn

print(lag_brukernavn("Henrik Strøm-Andersen"))

def lag_epost(fullt_navn, skolenavn):
    brukernavn = lag_brukernavn(fullt_navn)
    skolenavn = skolenavn.lower()
    return f"{brukernavn}@{skolenavn}.viken.no"

print(lag_epost("Henrik Strøm-Andersen", "Sandvika"))

def fjern_falske_brukere(brukernavnsliste, nokkelord):
    for brukernavn in brukernavnsliste:
        if nokkelord in brukernavn:
            brukernavnsliste.remove(brukernavn)
    return brukernavnsliste

print(fjern_falske_brukere(["thorc", "henrikstr", "fredrikg"], "fred"))
