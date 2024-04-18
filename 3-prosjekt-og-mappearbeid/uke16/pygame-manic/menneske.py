from figur import Figur

class Menneske(Figur):
    def __init__(self) -> None:
        super().__init__(50, 200, "green")
        self.x_fart = 0
        self.y_fart = 0

    def oppdater_posisjon(self):
        self.rect.x += self.x_fart
        self.rect.y += self.y_fart

