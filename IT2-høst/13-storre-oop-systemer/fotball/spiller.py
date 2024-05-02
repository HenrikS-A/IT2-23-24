
class Spiller():
    def __init__(self, navn: str) -> None:
        self.navn = navn
        self.antall_kamper = 0

    def hent_navn(self) -> str:
        return self.navn
    
    def hent_antall_kamper(self) -> int:
        return self.antall_kamper
    
    def spill_kamp(self):
        self.antall_kamper += 1

    def sjekk_navn(self, navn: str) -> bool:
        # har ikke brydd meg om å sjekke om navn strengen har flere navn
        if navn in self.navn:
            return True
        return False
    