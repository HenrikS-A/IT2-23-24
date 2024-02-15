# 1. Oppsett


# 2. Gameloop
while True:
    print("-- Stortinget fantasy --")
    print() # Tom linje
    print("1: Vis politikeroversikt")
    print("2: Avslutt")

    brukervalg = input(" > ")
    
    if brukervalg == "1":
        print("-- Politikeroversikt --")
        print("Trykk på enter for å gå tilbake til hovedmenyen")
        input() # Pauser koden helt til bruker trykker på enter
    
    elif brukervalg == "2":
        print("Avslutter")
        break

print("Takk for nå!")
