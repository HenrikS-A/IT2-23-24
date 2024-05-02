from oppg1 import Person

class Elev(Person):
    def __init__(self, navn: str, etternavn: str, fodselsaar: int):
        super().__init__(navn, etternavn, fodselsaar)
        self.brukernavn = self.fornavn.lower() + self.etternavn[:3].lower()
        self.mail = self.brukernavn + "@viken.no"
        
    def finn_trinn(self):
        if self.fodselsaar == 2005:
            return "VG3"
        elif self.fodselsaar == 2006:
            return "VG2"
        elif self.fodselsaar == 2007:
            return "VG1"


ravi = Elev("Ravi", "Manikarnika", 2006)
print( ravi.finn_trinn() )
print( ravi.brukernavn )
print( ravi.mail )

print(ravi.beregn_alder())