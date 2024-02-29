import os
import json
from pokemon_klasser import Pokemon
from pokemon_trenere import Trener

# 1. Oppsett
def rens_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


with open("pokemon_oversikt.json", "r", encoding="utf-8") as fil:
    pokemons = json.load(fil)

pokemon_objekter = [Pokemon(pokemon) for pokemon in pokemons]
trener_objekter = []

# 2. Gameloop
while True:
    rens_terminal()
    print("-- Pokemon --")  
    print("1: Se pokemonoversikt")
    print("2: Se treneroversikt")
    print("3: Lag trener")
    print("4: Avslutt")

    brukervalg = input(" > ")
    rens_terminal()
 
    if brukervalg == "1":
        print("-- Pokemonoversikt --")
        for pokemon in pokemon_objekter:
            print(pokemon)
    
    elif brukervalg == "2":
        print("-- Treneroversikt --")
        for trener in trener_objekter:
            print(trener)
    
    elif brukervalg == "3":
        print("-- Lag trener --")
        trenernavn = input("Hva vil du kalle treneren?\n > ")
        trener_objekter.append(Trener(trenernavn))
    
    elif brukervalg == "4":
        print("Avslutter")
        break # bryter ut av while-løkken
    
    else:
        print("Ugyldig valg")

    input("Trykk enter for å gå tilbake til hovedmenyen")

print("Takk for nå!")
