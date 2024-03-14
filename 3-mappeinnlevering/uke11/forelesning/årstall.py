# Et program som tar inn alder og printer fødselsår

while True: # En evig løkke.
    try:
        alder = int(input("Hvor gammel blir du i år?\n > "))
        if alder >= 0:
            break # Avslutt løkka og gå videre i koden
        print("Ugyldig tall. Prøv igjen.")
    except:
        print("Ugyldig input. Prøv igjen.")

aar_naa = 2024
fodselsaar = aar_naa - alder
print(f"Du er født i {fodselsaar}")
