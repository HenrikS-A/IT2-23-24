import random

class Bil:
    def __init__(self, merke: str, modell: str, aar: int) -> None:
        self.merke = merke
        self.modell = modell
        self.aar = aar
        self.nummerskilt = "BU" + str(random.randint(10000, 99999))
        self.km = 0

    def kjor(self, km):
        self.km += km

class Elbil(Bil):
    def __init__(self, merke: str, modell: str, aar: int, ladetype: str) -> None:
        super().__init__(merke, modell, aar)
        self.ladetype = ladetype
        self.batteriprosent = 100

    def lad(self):
        self.batteriprosent = 100

    def kjor(self, km):
        super().kjor(km)
        self.batteriprosent -= 0.3 * km

class Bensinbil(Bil):
    def __init__(self, merke: str, modell: str, aar: int, girkasse: str, antall_gir: int, drivstoff: str) -> None:
        super().__init__(merke, modell, aar)
        self.girkasse = girkasse
        self.antall_gir = antall_gir
        self.drivstoff = drivstoff
        self.fyllgrad = 100

    def fyll(self):
        self.fyllgrad = 100

    def kjor(self, km):
        super().kjor(km)
        self.fyllgrad -= 0.8 * km



henriks_bil = Bil("Bugatti", "Chiron Super Sport", 2023)
martins_bil = Bil("Chevrolet", "Camaro", 2023)

bmw_ix = Elbil("BMW", "IX", "USB-C")
bmw_m2 = Bensinbil("BMW", "M2", 2023, "manuell", 6, "bensin")


bmw_m2.kjor(100)



