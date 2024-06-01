import random
from konstanter import *
from figur import Figur

class Fiende(Figur):
    def __init__(self) -> None:
        x = random.randint(0, ANTALL_KOLONNER - 1)
        super().__init__(x, MARG_TOPP, "red")
        self.fart = 1

    def flytt(self):
        self.y += 1
        self.oppdater_rect()