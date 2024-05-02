
def sjekk_reise(reise: list[list[str]]):
    gyldig_reise = []
    for i in range(len(reise)):
        if reise[i] != reise[-1]:
            if reise[i][1] == reise[i + 1][0]:
                gyldig_reise.append(True)
            else:
                gyldig_reise.append(False)
    
    if all(gyldig_reise):
        return True
    else:
        return False
            
        

a = sjekk_reise([["Spania", "Frankrike"], ["Frankrike", "Norge"]])
print(a)
b = sjekk_reise([["Russland", "Tyskland"], ["Tyskland", "Sverige"], ["Norge", "Belgia"]])
print(b)
c = sjekk_reise([["Russland", "Tyskland"], ["Norge", "Tyskland"]])
print(c)
