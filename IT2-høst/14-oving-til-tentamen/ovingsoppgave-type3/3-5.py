
def forkort_lagliste(lagliste: list[str]):
    ny_liste = []
    for lag in lagliste:
        if lag not in ny_liste:
            ny_liste.append(lag)
    
    return ny_liste

a = forkort_lagliste(["Brann", "Molde", "Brann"])
print(a)