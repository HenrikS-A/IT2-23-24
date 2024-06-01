import pygame
from konstanter import *
from figur import Figur


class Spiller(Figur):
    def __init__(self) -> None:
        super().__init__(1, HOYDE - FIGURBREDDE - 20, "green")

    def venstre(self):
        self.x -= 1
        if self.x < 0:
            self.x = ANTALL_KOLONNER - 1
        self.oppdater_rect()

    def høyre(self):
        self.x += 1
        if self.x >= ANTALL_KOLONNER:
            self.x = 0
        self.oppdater_rect()

    def tastetrykk(self, taster):
        if taster[pygame.K_LEFT]:
            self.venstre()
        if taster[pygame.K_RIGHT]:
            self.høyre()
