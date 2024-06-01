from figur import Figur
from konstanter import *

class Skudd(Figur):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, "lightgreen")
        self.fart = 1
    
    def flytt(self):
        self.y -= self.fart
        self.oppdater_rect()

