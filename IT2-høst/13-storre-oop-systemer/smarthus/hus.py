from rom import Rom

class Hus():
    def __init__(self) -> None:
        self.rom: list[Rom] = []

    def legg_til_rom(self, nytt_rom, antall):
        for _ in range(antall):
            self.rom.append(nytt_rom)

    def skru_paa_alt(self):
        for enkeltrom in self.rom:
            enkeltrom.tenn_alle_lys()
    
    def skru_av_alt(self):
        for enkeltrom in self.rom:
            enkeltrom.slukk_alle_lys()

# Testkode
if __name__ == "__main__":
    sandvika = Hus()
    sandvika.legg_til_rom(Rom(), 4)
