import random
from figur import Figur

class Ballong(Figur):
    def __init__(self, x: int, y: int) -> None:
        self.diameter = 50
        farger = ["red", "blue", "orange"]
        self.farge = random.choice(farger)
        super().__init__(self.diameter, self.diameter, x, y, self.farge)
        # Disse skal ikke sendes med til superklassen:
        self.x_fart = 0
        self.y_fart = 0

    def skyt(self):
        self.y_fart = -2
        

    def stopp(self):
        self.y_fart = 0

    def oppdater_posisjon(self):
        self.rect.x += self.x_fart
        self.rect.y += self.y_fart

