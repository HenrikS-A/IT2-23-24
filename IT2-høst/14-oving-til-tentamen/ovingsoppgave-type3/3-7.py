
def samlet_vaksinasjon(krav_hvert_land: list[list[str]]):
    vaksinekrav = []
    for i in range(len(krav_hvert_land)):
        for krav in krav_hvert_land[i]:
            if krav not in vaksinekrav:
                vaksinekrav.append(krav)

    return vaksinekrav

a = samlet_vaksinasjon([["difteri", "tyfoid"], ["hepatit", "difteri"]])
print(a)