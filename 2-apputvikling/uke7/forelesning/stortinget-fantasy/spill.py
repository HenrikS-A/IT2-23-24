import os
import sys
import json
from politiker import Politiker

# 1. Oppsett
def rens_terminal():
    # En funksjon som renser terminalen
    # funksjonen sjeker om vi er på et windows-system eller andre systemer
    # og kjører riktig kommando
    if sys.platform == "Windows" or sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


with open("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
representanter = data["dagensrepresentanter_liste"]

## Lager en politiker-klasse for hver representant på stortinget
politikere = [Politiker(representant) for representant in representanter]


# 2. Gameloop
while True:
    rens_terminal()
    print("-- Stortinget fantasy --")
    print() # Tom linje
    print("1: Vis politikeroversikt")
    print("2: Avslutt")

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
        print("Avslutter")
        break # Hopper ut av løkka (avslutter spillet)
    
    else:
        rens_terminal()
        print("Ugyldig valg! Trykk enter for å gå tilbake til hovedmenyen")
        input()

print("Takk for nå!")
