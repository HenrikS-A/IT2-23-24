import random
from svikinator import svikinator

def beregn_score(valg_spiller1, valg_spiller2):
    if valg_spiller1 == "samarbeid" and valg_spiller2 == "samarbeid":
        return [3, 3]
    elif valg_spiller1 == "svik" and valg_spiller2 == "samarbeid":
        return [5, 0]
    elif valg_spiller1 == "samarbeid" and valg_spiller2 == "svik":
        return [0, 5]
    elif valg_spiller1 == "svik" and valg_spiller2 == "svik":
        return [1, 1]

    

def strategi_tester(motspillers_valg):
    tilfeldig_valg = random.choice(["samarbeid", "svik"])

    if tilfeldig_valg == "samarbeid":
        return "samarbeid"
    return "svik"

def min_strategi_HENRIK(motspillers_valg, mine_valg):
    if motspillers_valg.count("samarbeid") > mine_valg.count("samarbeid"):
        return "svik"
    elif motspillers_valg.count("svik") > mine_valg.count("svik"):
        return "svik"
    return "samarbeid"

def martin_henrik_strategi(motspillers_valg, mine_valg):
    if len(mine_valg) < 1:
        return "samarbeid"
    
    samarbeid_count = motspillers_valg.count("samarbeid")
    prosentandel = samarbeid_count / len(motspillers_valg)

    siste_svik = motspillers_valg[-10:].count("svik")

    if siste_svik >= 5 or prosentandel >= 0.3:
        return "svik"
    
    return "samarbeid"

def thor_strategi(motspillers_historikk, min_historikk):
    
    # Hvis jeg har sveket fem på rad: samarbeid
    if len(min_historikk) > 5 and "samarbeid" not in min_historikk[-5:]:
        return "samarbeid"

    # tit for tat: herm etter motspillerens siste valg
    if len(motspillers_historikk) > 1:
        return motspillers_historikk[-1]
    # ellers: samarbeid
    return "samarbeid"
    



def utfor_spill():
    spiller1_valg = []
    spiller1_score = 0
    spiller2_valg = []
    spiller2_score = 0

    for _ in range(1000):
        # spiller1 = min_strategi_HENRIK(spiller2_valg, spiller1_valg)
        # spiller1_valg.append(spiller1)

        spiller1 = thor_strategi(spiller2_valg, spiller1_valg)
        spiller1_valg.append(spiller1)

        spiller2 = svikinator(spiller1_valg)
        spiller2_valg.append(spiller2)

        # 

        # martin_henrik_strategi(spiller1_valg, spiller2_valg)
        
    
        score = beregn_score(spiller1, spiller2)
        spiller1_score += score[0]
        spiller2_score += score[1]

    print(f"Thor: {spiller1_score}")
    print(f"Meg: {spiller2_score}")



utfor_spill()
