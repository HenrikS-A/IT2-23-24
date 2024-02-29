import os
import sys
import json
from politiker import Politiker
from fantasiparti import Fantasiparti

# 1. Oppsett
def rens_terminal():
    # En funksjon som renser terminalen
    # Funksjonen sjeker om vi er på et windows-system eller andre systemer og kjører riktig kommando
    if sys.platform == "Windows" or sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


with open("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
representanter = data["dagensrepresentanter_liste"]

## Lager en politiker-klasse for hver representant på stortinget
politikere = [Politiker(representant) for representant in representanter]


rens_terminal()
print("-- Stortinget fantasy --")
print("Du må stifte et parti for å spille spillet")
print("Hva skal partiet hete")
partinavn = input("> ")

print("Hva heter du?")
partieier = input("> ")

brukerparti = Fantasiparti(partinavn, partieier)

print(f"Gratulerer! {brukerparti.navn} ble opprettet med støtte fra {brukerparti.eier}")
print("Trykk enter for å starte spillet")
input()

# 2. Gameloop
while True:
    rens_terminal()
    print("-- Stortinget fantasy --")
    print(f"Parti: {brukerparti.navn}")
    print(f"Saldo: {brukerparti.saldo}")
    print(f"Antall politikere: {len(brukerparti.politikere)}")
    print() # Tom linje

    print("1: Vis politikeroversikt")
    print("2: Mitt parti")
    print("3: Kjøp politiker")
    print("4: Selg politiker")
    print("5: Avslutt")

    brukervalg = input(" > ")
    
    if brukervalg == "1":
        rens_terminal()
        print("-- Politikeroversikt --")
        for politiker in politikere:
            print(politiker)
        print("Trykk på enter for å gå tilbake til hovedmenyen")
        input() # Pauser koden helt til bruker trykker på enter

    elif brukervalg == "2":
        rens_terminal()
        print("-- Mitt parti --")

        brukerparti.print_politikere()

        print("Trykk på enter for å gå tilbake til hovedmenyen")
        input() # Pauser koden helt til bruker trykker på enter
    
    elif brukervalg == "3":
        rens_terminal()
        print("-- Kjøp politiker --")

        for i in range(10):
            print(f"{i}: {politikere[i]}")

        print("Hvilken politiker vil du kjøpe? (0-9)")
        valgt_politikernummer = int(input("> "))
        valgt_politiker = politikere[valgt_politikernummer] # et politikerobjekt, f.eks: Erna Solberg

        brukerparti.kjøp_politiker(valgt_politiker)

        print("Trykk på enter for å gå tilbake til hovedmenyen")
        input() # Pauser koden helt til bruker trykker på enter
    
    elif brukervalg == "4":
        rens_terminal()
        print("-- Selg politiker --")

        brukerparti.print_politikere()
        print("Hvilken politiker hønsker du å selge?")
        valgt_politikernummer = int(input("> "))
        valgt_politiker = brukerparti.politikere[valgt_politikernummer]

        brukerparti.selg_politiker(valgt_politiker)

        print("Trykk på enter for å gå tilbake til hovedmenyen")
        input() # Pauser koden helt til bruker trykker på enter

    elif brukervalg == "5":
        rens_terminal()
        print("Avslutter")
        break # Hopper ut av løkka (avslutter spillet) 
    
    else:
        rens_terminal()
        print("Ugyldig valg! Trykk enter for å gå tilbake til hovedmenyen")
        input()

print("Takk for nå!")
