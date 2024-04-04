class Hund:
    """
    Klasse for en hund.
    
    attributter
        navn (str): Navnet på hunden
        alder (int): Alderen til hunden
        rase (str): Rasen til hunden (eks: Schäfer)
    
    metoder
        bjeff(): Et bjeff printes ut som en melding
        vift_på_halen(): Får hunden til å vifte på halen. Printes som en melding.
        info(): Printer ut en infomelding om hunden. Navn, alder og rase blir presentert.
    """
    def __init__(self, navn: str, alder: int, rase: str):
        self.navn = navn
        self.alder = alder
        self.rase = rase

    def bjeff(self):
        return f"{self.navn} sier: Woof!"

    def vift_på_halen(self):
        return f"{self.navn} vifter på halen!"

    def info(self):
        return f"{self.navn} er en {self.alder} år gammel {self.rase}."

# Test av klassen
if __name__ == "__main__":
    min_hund = Hund("Rex", 5, "Schäfer")
    print(min_hund.bjeff())
    print(min_hund.vift_på_halen())
    print(min_hund.info())
