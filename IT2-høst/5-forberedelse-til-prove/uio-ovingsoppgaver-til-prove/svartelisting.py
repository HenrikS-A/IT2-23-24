# Dette er en "mengde", UIO anbefalte å bruke dette. En mengde kan ikke ha kopier.
svarteliste = {23894, 29741, 10961, 22768, 22803, 11993, 24409, 9312, 29405, 6638, 738, 29964, 11967, 13443, 11534, 26228, 6867, 23027, 29137, 14084, 452, 15594, 22765, 25487}

def bestem_laan(liste):
    kunde_id = int(input("Skriv inn din kunde-ID. Den skal bestå av et 5-siffret tall. Skriv inn her: "))
    if kunde_id in liste:
        print("Kan ikke få lån.")
    else:
        print("Kan få lån")
    
bestem_laan(svarteliste)