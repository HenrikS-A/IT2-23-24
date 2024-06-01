import pygame
from konstanter import *

class Figur:
    def __init__(self, x: int, y:int, farge: str) -> None:
        self.surface = pygame.Surface((FIGURBREDDE, FIGURBREDDE))
        self.rect = self.surface.get_rect()
        self.x = x
        self.y = y
        self.surface.fill(farge)
        self.oppdater_rect()

    def oppdater_rect(self):
        self.rect.centerx = self.x * CELLEBREDDE + FIGURBREDDE + MARG_VENSTRE
        self.rect.centery = self.y
    
    def tegn(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)
    
    def sjekk_kollisjon(self, figurliste):
        # en metode som tar inn en liste med figurer og returnerer den første figuren som
        # kolliderer med denne figuren (self), hvis ikke den kolliderer med noen i listen
        # returnerer den None
        for figur in figurliste:
            if self.rect.colliderect(figur.rect):
                return figur
        return None
