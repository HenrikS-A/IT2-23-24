from figur import Figur

class Troll(Figur):
    def __init__(self, x:int, y:int):
        super().__init__(x, y, "green")
        self.fart = 1
        self.retning = [0, 0]

    def oppdater_posisjon(self):
        self.rect.x += self.fart * self.retning[0]
        self.rect.y += self.fart * self.retning[1]

