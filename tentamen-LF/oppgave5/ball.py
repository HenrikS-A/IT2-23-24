from figur import Figur

class Ball(Figur):
    def __init__(self, x: int, y: int):
        super().__init__(10, 10, x, y)
        self.x_fart = 3
        self.y_fart = 3

    def oppdater_posisjon(self, bredde, hoyde):
        if self.rect.right > bredde or self.rect.left < 0:
            self.snu_x()
        if self.rect.bottom < 0:
            self.snu_y()
        self.rect.x += self.x_fart
        self.rect.y += self.y_fart
    
    def snu_x(self):
        self.x_fart *= -1

    def snu_y(self):
        self.y_fart *= -1