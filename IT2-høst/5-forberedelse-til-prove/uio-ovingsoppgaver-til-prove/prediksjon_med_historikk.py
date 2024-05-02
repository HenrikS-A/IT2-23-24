

def enkel_prediksjon():
    alder = int(input("Alder: Hvor gammel er du? Skriv her: "))
    kjonn = input("Kjønn: Hvilket kjønn? (mann eller kvinne) Skriv her: ")
    sivilstatus = input("Sivilstatus: Er du gift eller singel? Skriv her: ")
    mengde_gjeld = int(input("Gjeld: Hva har du i gjeld nå? Skriv her: "))

    print(f"\nDu er en {sivilstatus} {kjonn} på {alder} år med {mengde_gjeld} kr i gjeld.\n")

    if sivilstatus == "singel" and kjonn == "mann" and alder < 30 and mengde_gjeld > 100_000:
        print("Vil ikke betale.")
    elif kjonn == "mann" and alder < 25 and mengde_gjeld > 200_000:
        print("Vil ikke betale.")
    elif sivilstatus == "singel" and kjonn == "kvinne" and alder < 28 and mengde_gjeld > 300_000:
        print("Vil ikke betale.")
    else:
        print("Vil betale.")


def prediksjon_med_betalingshistorikk():
    utdanningsnivaa_loenn = {
        "ukjent": 300_000,
        "grunnskole": 260_000,
        "hoeyskole": 500_000,
        "universitet": 700_000
    }

    # Henter info om klienten og printer ut
    alder = int(input("Alder: Hvor gammel er du? Skriv her: "))
    kjonn = input("Kjønn: Hvilket kjønn? (mann eller kvinne) Skriv her: ")
    sivilstatus = input("Sivilstatus: Er du gift eller singel? Skriv her: ")
    mengde_gjeld = int(input("Gjeld: Hva har du i gjeld nå? Skriv her: "))

    print(f"\nDu er en {sivilstatus} {kjonn} på {alder} år med {mengde_gjeld} kr i gjeld.\n")

    # Henter betalingshistorikken de 3 forrige månedene og lagrer det i listen betalingshistorikk
    betalingshistorikk = []
    for maaned in range(3):
        maaned_betalingshistorikk = input(f"Betalte du gjelden din for {maaned + 1} mnd. siden? Skriv her: ")
        betalingshistorikk.append(maaned_betalingshistorikk)
    
    # Printer ut betalingshistorikk-listen på en fin måte.
    print(f"\nDin betalingshistorikk:")
    for mnd, historikk in enumerate(betalingshistorikk):
        print(f"{mnd + 1} mnd. siden: {historikk}")

    # Henter inn utdanningsnivå
    utdanningsnivaa = input("\nHva er utdanningsnivået ditt? Skriv her: ")
    if utdanningsnivaa in utdanningsnivaa_loenn.keys():
        loenn = utdanningsnivaa_loenn[utdanningsnivaa]
    else:
        loenn = utdanningsnivaa_loenn["ukjent"]


    # Beregner og skriver ut om du vil eller ikke vil betale
    if kjonn == "mann" and loenn > 3 * mengde_gjeld:
        print("Vil betale.")

    elif "ikke_betalt" in betalingshistorikk:
        print("\nVil ikke betale.")

    elif sivilstatus == "singel" and kjonn == "mann" and alder < 30 and mengde_gjeld > 100_000:
        print("\nVil ikke betale.")
    elif kjonn == "mann" and alder < 25 and mengde_gjeld > 200_000:
        print("\nVil ikke betale.")
    elif sivilstatus == "singel" and kjonn == "kvinne" and alder < 28 and mengde_gjeld > 300_000:
        print("\nVil ikke betale.")
    else:
        print("\nVil betale.")


prediksjon_med_betalingshistorikk()
        


