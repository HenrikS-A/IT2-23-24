def beregn_score(valg_spiller1, valg_spiller2):
    if valg_spiller1 == "samarbeid" and valg_spiller2 == "samarbeid":
        return [3, 3]
    elif valg_spiller1 == "svik" and valg_spiller2 == "samarbeid":
        return [5, 0]
    elif valg_spiller1 == "samarbeid" and valg_spiller2 == "svik":
        return [0, 5]
    elif valg_spiller1 == "svik" and valg_spiller2 == "svik":
        return [1, 1]


def spill_snilt(motspillers_valg):
    if motspillers_valg.count("svik") > motspillers_valg.count("samarbeid"):
        return "svik"
    return "samarbeid"

def spill_slemt(motspillers_valg):
    if len(motspillers_valg) <= 5:
        return "samarbeid"
    elif len(motspillers_valg) > 5:
        return "svik"


def utfor_spill():
    spiller1_valg = []
    spiller1_score = 0
    spiller2_valg = []
    spiller2_score = 0

    for _ in range(10):
        spiller1 = spill_snilt(spiller2_valg)
        spiller1_valg.append(spiller1)

        spiller2 = spill_slemt(spiller1_valg)
        spiller2_valg.append(spiller2)
        
    
        score = beregn_score(spiller1, spiller2)
        spiller1_score += score[0]
        spiller2_score += score[1]

    print(f"Spiller 1: {spiller1_score}")
    print(f"Spiller 2: {spiller2_score}")


def utfor_spill_uendelig():
    spiller1_valg = []
    spiller1_score = 0
    spiller2_valg = []
    spiller2_score = 0

    bruker_valg = input("Vil du spille? Skriv 'j' for ja eller 'n' for nei.\n >")

    while bruker_valg != "j" and bruker_valg != "n":
        bruker_valg = input("Vil du spille? Skriv 'j' for ja eller 'n' for nei.\n >")
        
    while bruker_valg == "j":
        spiller1 = spill_snilt(spiller2_valg)
        spiller1_valg.append(spiller1)

        spiller2 = spill_slemt(spiller1_valg)
        spiller2_valg.append(spiller2)
        
        score = beregn_score(spiller1, spiller2)
        spiller1_score += score[0]
        spiller2_score += score[1]


        print(f"Spiller 1: {spiller1_score}")
        print(f"Spiller 2: {spiller2_score}")

        bruker_valg = input("Vil du spille? Skriv 'j' for ja eller 'n' for nei.\n >")

    print("Hade!")



utfor_spill_uendelig()