from spiller import Spiller

class Lag():
    def __init__(self, navn: str) -> None:
        self.navn = navn
        self.spillere: list[Spiller] = []
        self.antall_seiere = 0
        self.antall_uavgjort = 0
        self.antall_tap = 0

    def hent_navn(self) -> str:
        return self.navn
    
    def hent_poeng(self) -> int:
        return self.antall_seiere * 3 + self.antall_uavgjort
    
    def legg_til_spiller(self, spiller):
        self.spillere.append(spiller)

    def spill_kamp(self):
        for spiller in self.spillere:
            spiller.spill_kamp()
    
    def seier(self):
        self.antall_seiere += 1
        self.spill_kamp()

    def uavgjort(self):
        self.antall_uavgjort += 1
        self.spill_kamp()

    def tap(self):
        self.antall_tap += 1
        self.spill_kamp()

    def finn_spiller(self, navn: str):
        for spiller in self.spillere:
            if navn in spiller.navn:
                return spiller.navn
            return None
