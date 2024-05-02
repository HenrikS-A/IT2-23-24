
class Pokemon():
    def __init__(self, nummer: int, navn: str, type_1: str, hp: int, angrep: int, forsvar: int) -> None:
        self.nummer = nummer
        self.navn = navn
        self.type1 = type_1
        self.hp = hp 
        self.angrep = angrep 
        self.forsvar = forsvar

    def angrip(self, motstander):
        print(f"{self.navn} angriper {motstander.navn}")

        # Pokemon spill-logikk:
        if self.type1 == "Fire" and motstander.type1 == "Grass":
            print("Det var supereffektivt!")
            motstander.hp -= self.angrep * 2 - motstander.forsvar
        else:
            motstander.hp -= self.angrep - motstander.forsvar
            
        print(f"{motstander.navn} har nå {motstander.hp} hp igjen!")

    def __str__(self):
        return f"{self.navn} ({self.hp})"


if __name__ == "__main__":
    bulbasaur = Pokemon(1, "Bulbasaur", "Grass", 45, 49, 49)
    charmander = Pokemon(4, "Charmander", "Fire", 39, 52, 43)
    print(bulbasaur)


    charmander.angrip(bulbasaur)
    bulbasaur.angrip(charmander)
    print(bulbasaur)