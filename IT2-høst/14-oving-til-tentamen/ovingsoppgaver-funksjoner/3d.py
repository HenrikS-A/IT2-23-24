
def summer_rabatt(vareliste: list, forpris, nypris): 
    rabatt_sum = 0
    for vare in vareliste:
        penger_spart = forpris[vare] - nypris[vare]
        rabatt_sum += penger_spart
    
    return rabatt_sum


a = ["laptop", "ryggsekk"]
b = {
    "laptop": 5000,
    "ryggsekk": 900,
}
c = {
    "laptop": 4000,
    "ryggsekk": 600
}

hei = summer_rabatt(a, b, c)
print(hei)
