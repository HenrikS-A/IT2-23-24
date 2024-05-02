

def enkel_prediksjon():

    alder = int(input("Alder: Hvor gammel er du? Skriv her: "))
    kjonn = input("Kjønn: Hvilket kjønn? (mann eller kvinne) Skriv her: ")
    sivilstatus = input("Sivilstatus: Er du gift eller singel? Skriv her: ")
    mengde_gjeld = int(input("Gjeld: Hva har du i gjeld nå? Skriv her: "))

    print(f"Du er en {sivilstatus} {kjonn} på {alder} år med {mengde_gjeld} kr i gjeld.")

    if sivilstatus == "singel" and kjonn == "mann" and alder < 30 and mengde_gjeld > 100_000:
        print("Vil ikke betale.")
    elif kjonn == "mann" and alder < 25 and mengde_gjeld > 200_000:
        print("Vil ikke betale.")
    elif sivilstatus == "singel" and kjonn == "kvinne" and alder < 28 and mengde_gjeld > 300_000:
        print("Vil ikke betale.")
    else:
        print("Vil betale.")

enkel_prediksjon()


