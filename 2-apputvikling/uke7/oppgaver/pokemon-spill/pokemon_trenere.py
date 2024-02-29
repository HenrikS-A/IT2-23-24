from pokemon_klasser import Pokemon

class Trener:
    def __init__(self, navn) -> None:
        self.navn: str = navn
        self.pokemons: list[Pokemon] = []
    
    def legg_til_pokemon(self, pokemon: Pokemon):
        self.pokemons.append(pokemon)
    
    def fjern_pokemon(self, pokemon: Pokemon):
        self.pokemons.remove(pokemon)

    def __str__(self) -> str:
        return f"{self.navn} - Antall pokemons: {len(self.pokemons)}"