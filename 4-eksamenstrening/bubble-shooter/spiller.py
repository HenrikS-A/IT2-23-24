import pygame
from figur import Figur

class Spiller(Figur):
    def __init__(self, x: int, y: int):
        super().__init__(5, 100, x, y, "white")
        self.vinkel = 90

    def oppdater_posisjon(self):
        self.surface = pygame.transform.rotate(self.surface, self.vinkel)
        self.rect = self.surface.get_rect()

    def flytt_venstre(self):
        self.vinkel += 5
        self.oppdater_posisjon()

    def flytt_hoyre(self):
        self.vinkel -= 5
        self.oppdater_posisjon()

