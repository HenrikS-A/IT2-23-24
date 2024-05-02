from lyspaere import Lyspaere

class Rom():
    def __init__(self) -> None:
        self.lyspaerer: list[Lyspaere] = []

    def legg_til_lyspaere(self, paere, antall):
        for _ in range(antall):
            self.lyspaerer.append(paere)
    
    def tenn_lys_nummer(self, n):
        self.lyspaerer[n - 1].tenn()

    def tenn_alle_lys(self):
        for lys in self.lyspaerer:
            lys.tenn()
    
    def slukk_alle_lys(self):
        for lys in self.lyspaerer:
            lys.slukk()

    # Bestemmer hvordan rommet skal vises når det blir printet
    def __str__(self) -> str:
        return f"Rom: Antall lyspærer: {len(self.lyspaerer)}"
        

# Gjør at test-koden ikke kjøres fra andre filer enn bare denne.
if __name__ == "__main__":

    rom_33_06 = Rom()
    rom_33_06.legg_til_lyspaere(Lyspaere(), 3)

    # Tenn lyset i pære nr. 2
    rom_33_06.lyspaerer[1].tenn()
    rom_33_06.tenn_lys_nummer(2)

    # Tenn alle lys i rommet
    rom_33_06.tenn_alle_lys()

    print(rom_33_06)
    print("Hei fra rom.py")
