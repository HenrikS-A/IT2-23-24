
def fjern_utsolgte(handleliste: list[str], utsolgte: list[str]):
    oppdatert_handleliste = []
    for vare in handleliste:
        if vare in utsolgte:
            print(vare)
        else:
            oppdatert_handleliste.append(vare)

    return(oppdatert_handleliste)

a = fjern_utsolgte(["melk", "brus", "pasta"], ["kanel", "brus"])
print(a)